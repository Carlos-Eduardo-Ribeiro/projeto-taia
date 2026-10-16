"""Funções de ativação e suas derivadas, implementadas do zero."""

import numpy as np

EPS = 1e-12


def sigmoid(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, -500, 500)
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_derivative(a: np.ndarray) -> np.ndarray:
    return a * (1.0 - a)


def tanh(x: np.ndarray) -> np.ndarray:
    return np.tanh(x)


def tanh_derivative(a: np.ndarray) -> np.ndarray:
    return 1.0 - a**2


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, x)


def relu_derivative(a: np.ndarray) -> np.ndarray:
    return (a > 0).astype(float)


def softmax(x: np.ndarray) -> np.ndarray:
    """Softmax estável (por linha)."""
    x = x - np.max(x, axis=-1, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=-1, keepdims=True)


def binary_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """BCE média para saída sigmoide binária."""
    y_pred = np.clip(y_pred, EPS, 1 - EPS)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def cross_entropy(y_onehot: np.ndarray, y_pred: np.ndarray) -> float:
    """Cross-entropy categórica para saída softmax."""
    y_pred = np.clip(y_pred, EPS, 1.0)
    return -np.mean(np.sum(y_onehot * np.log(y_pred), axis=-1))


def accuracy_binary(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_pred > 0.5).astype(int) == y_true))


def accuracy_multiclass(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.argmax(y_pred, axis=-1) == y_true))


ATIVACOES = {
    "relu": (relu, relu_derivative),
    "sigmoid": (sigmoid, sigmoid_derivative),
    "tanh": (tanh, tanh_derivative),
}


def get_activation(nome: str):
    """Retorna (função, derivada) pelo nome."""
    if nome not in ATIVACOES:
        raise ValueError(
            f"Ativação '{nome}' não suportada. Opções: {sorted(ATIVACOES)}"
        )
    return ATIVACOES[nome]