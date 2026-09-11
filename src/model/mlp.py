"""MLP construída do zero: inicialização, feed-forward e back-propagation.

A rede é representada como uma lista de camadas; cada camada guarda
uma matriz de pesos W (número_de_neuronios x entradas) e um vetor de
bias b. O grafo da rede (nós = neurônios, arestas = pesos) utilizado na
visualização é derivado diretamente desta estrutura.
"""

from __future__ import annotations

import numpy as np

from src.model.activations import get_activation


def _inicializa_pesos(fan_in: int, fan_out: int, ativacao: str, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    if ativacao == "relu":
        limite = np.sqrt(2.0 / fan_in)  # He
    else:
        limite = np.sqrt(1.0 / fan_in)  # Xavier
    W = rng.normal(0.0, limite, size=(fan_out, fan_in))
    b = np.zeros(fan_out)
    return W, b


class MLP:
    """Perceptron Multicamadas com arquitetura e ativações configuráveis.

    Parâmetros:
        layer_sizes: lista [n_entradas, n_ocultas_1, ..., n_saidas].
        hidden_activation: ativação das camadas ocultas (relu | sigmoid | tanh).
        output_activation: ativação da saída (sigmoid para binária).
        seed: semente de inicialização dos pesos.
    """

    def __init__(
        self,
        layer_sizes: list[int],
        hidden_activation: str = "relu",
        output_activation: str = "sigmoid",
        seed: int = 42,
    ):
        if len(layer_sizes) < 2:
            raise ValueError("A rede precisa de ao menos entrada e saída.")
        self.layer_sizes = list(layer_sizes)
        self.hidden_activation = hidden_activation
        self.output_activation = output_activation
        self.activations = [hidden_activation] * (len(layer_sizes) - 1)
        self.activations[-1] = output_activation

        self.W: list[np.ndarray] = []
        self.b: list[np.ndarray] = []
        for l in range(len(layer_sizes) - 1):
            W, b = _inicializa_pesos(
                layer_sizes[l], layer_sizes[l + 1], self.activations[l], seed=seed + l
            )
            self.W.append(W)
            self.b.append(b)

        self.cache_z: list[np.ndarray] = []
        self.cache_a: list[np.ndarray] = []

        self.is_binary = layer_sizes[-1] == 1

    # ------------------------------------------------------------------ #
    # Camada de ativação configurável
    # ------------------------------------------------------------------ #
    def _aplicar_ativacao(self, l: int, z: np.ndarray) -> np.ndarray:
        nome = self.activations[l]
        if self.activations[l] == "sigmoid":
            from src.model.activations import sigmoid

            return sigmoid(z)
        if nome == "tanh":
            from src.model.activations import tanh

            return tanh(z)
        if nome == "relu":
            from src.model.activations import relu

            return relu(z)
        return z  # softmax tratada apenas na saída

    # ------------------------------------------------------------------ #
    # Feed-forward
    # ------------------------------------------------------------------ #
    def forward(self, X: np.ndarray) -> np.ndarray:
        """Propaga X (m x n_entradas) pela rede e devolve a saída.

        As ativações intermediárias ficam armazenadas para o back-propagation.
        """
        a = np.asarray(X, dtype=float)
        self.cache_a = [a]
        self.cache_z = []
        for l in range(len(self.W)):
            z = a @ self.W[l].T + self.b[l]
            self.cache_z.append(z)
            if l == len(self.W) - 1 and self.activations[l] == "softmax":
                from src.model.activations import softmax

                a = softmax(z)
            else:
                a = self._aplicar_ativacao(l, z)
            self.cache_a.append(a)
        return a

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Retorna rótulos previstos (0/1 para binária, índice da classe no resto)."""
        out = self.forward(np.asarray(X, dtype=float))
        if self.is_binary:
            return (out > 0.5).astype(int).ravel()
        return np.argmax(out, axis=-1).ravel()

    # ------------------------------------------------------------------ #
    # Back-propagation
    # ------------------------------------------------------------------ #
    def backward(self, y: np.ndarray, out: np.ndarray) -> tuple[list[np.ndarray], list[np.ndarray]]:
        """Calcula os gradientes médios de W e b sobre o lote.

        delta da saída:
            binária (sigmoid + BCE): out - y
            multiclasse (softmax + CE): out - one_hot(y)
        """
        m = out.shape[0]
        if self.is_binary:
            delta = (out.ravel().reshape(-1, 1) - y.reshape(-1, 1)) / m
        else:
            y_onehot = np.eye(self.layer_sizes[-1])[y.astype(int)]
            delta = (out - y_onehot) / m

        grad_W: list[np.ndarray] = []
        grad_b: list[np.ndarray] = []
        for l in reversed(range(len(self.W))):
            a_prev = self.cache_a[l]  # ativação da camada anterior
            grad_W.insert(0, delta.T @ a_prev)
            grad_b.insert(0, delta.sum(axis=0))
            if l > 0:
                derivada = self._derivada_ativacao(l - 1, self.cache_a[l])
                delta = (delta @ self.W[l]) * derivada
        return grad_W, grad_b

    def _derivada_ativacao(self, l: int, a: np.ndarray) -> np.ndarray:
        nome = self.activations[l]
        if nome == "sigmoid":
            from src.model.activations import sigmoid_derivative

            return sigmoid_derivative(a)
        if nome == "tanh":
            from src.model.activations import tanh_derivative

            return tanh_derivative(a)
        from src.model.activations import relu_derivative

        return relu_derivative(a)

    # ------------------------------------------------------------------ #
    # Atualização dos pesos (gradiente descendente)
    # ------------------------------------------------------------------ #
    def update(self, lr: float, grad_W: list[np.ndarray], grad_b: list[np.ndarray]) -> None:
        for l in range(len(self.W)):
            self.W[l] = self.W[l] - lr * grad_W[l]
            self.b[l] = self.b[l] - lr * grad_b[l]

    # ------------------------------------------------------------------ #
    # Utilitários
    # ------------------------------------------------------------------ #
    @property
    def n_layers(self) -> int:
        return len(self.W)

    def info(self) -> dict:
        return {
            "architecture": " | ".join(str(n) for n in self.layer_sizes),
            "activation": self.activations,
            "output_activation": self.output_activation,
            "weights": [w.shape for w in self.W],
        }

    def set_weights(self, W: list[np.ndarray], b: list[np.ndarray]) -> None:
        self.W = [np.array(w, dtype=float) for w in W]
        self.b = [np.array(bv, dtype=float) for bv in b]

    def get_weights(self) -> tuple[list[np.ndarray], list[np.ndarray]]:
        return self.W, self.b

    def copy(self) -> "MLP":
        novo = MLP(self.layer_sizes, self.hidden_activation, self.output_activation)
        novo.set_weights(self.W, self.b)
        return novo