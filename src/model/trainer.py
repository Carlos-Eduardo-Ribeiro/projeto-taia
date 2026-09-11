"""Treinamento da MLP: gradiente descendente (batch / mini-batch) manual.

Controla épocas, embaralhamento, histórico de loss/accuracy (treino e
validação) e guarda os melhores pesos encontrados (menor loss de validação).
"""

from __future__ import annotations

import numpy as np

from src.config import RANDOM_STATE
from src.model.activations import (
    accuracy_binary,
    accuracy_multiclass,
    binary_cross_entropy,
    cross_entropy,
)


class Trainer:
    def __init__(self, model, lr: float = 0.01, batch_size: int | None = None, seed: int = RANDOM_STATE):
        self.model = model
        self.lr = lr
        self.batch_size = batch_size
        self.seed = seed
        self.history: list[dict] = []
        self.best_metrics: dict | None = None
        self._best_W: list[np.ndarray] | None = None
        self._best_b: list[np.ndarray] | None = None

    # ------------------------------------------------------------------ #
    # Métricas e loss
    # ------------------------------------------------------------------ #
    def _loss(self, X: np.ndarray, y: np.ndarray) -> float:
        out = self.model.forward(X)
        if self.model.is_binary:
            return binary_cross_entropy(y.ravel(), out.ravel())
        y_onehot = np.eye(self.model.layer_sizes[-1])[y.astype(int)]
        return cross_entropy(y_onehot, out)

    def _accuracy(self, X: np.ndarray, y: np.ndarray) -> float:
        out = self.model.forward(X)
        if self.model.is_binary:
            return accuracy_binary(y.ravel(), out.ravel())
        return accuracy_multiclass(y.astype(int), out)

    def _avalia(self, X, y) -> dict:
        return {"loss": self._loss(X, y), "accuracy": self._accuracy(X, y)}

    @staticmethod
    def _cria_batches(indices: np.ndarray, batch_size: int) -> list[np.ndarray]:
        if batch_size is None:
            return [indices]
        return [
            indices[i : i + batch_size] for i in range(0, len(indices), batch_size)
        ]

    # ------------------------------------------------------------------ #
    # Uma época
    # ------------------------------------------------------------------ #
    def train_one_epoch(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_val: np.ndarray | None = None,
        y_val: np.ndarray | None = None,
        lr: float | None = None,
        seed: int | None = None,
    ) -> dict:
        """Executa uma única época (feed-forward + back-prop + update) e avalia."""
        lr = self.lr if lr is None else lr
        rng = np.random.default_rng(self.seed if seed is None else seed)
        m = X_train.shape[0]

        indices = rng.permutation(m)
        for batch in self._cria_batches(indices, self.batch_size):
            Xb = X_train[batch]
            yb = y_train[batch]
            out = self.model.forward(Xb)
            grad_W, grad_b = self.model.backward(yb, out)
            self.model.update(lr, grad_W, grad_b)

        metrics = self._avalia(X_train, y_train)
        if X_val is not None and y_val is not None:
            val = self._avalia(X_val, y_val)
            metrics.update({f"val_{k}": v for k, v in val.items()})

        # Guarda a melhor época (baseada em loss de validação quando disponível)
        chave = "val_loss" if "val_loss" in metrics else "loss"
        if self.best_metrics is None or metrics[chave] <= self.best_metrics[chave]:
            self.best_metrics = dict(metrics)
            self._best_W, self._best_b = self.model.get_weights()

        return metrics

    # ------------------------------------------------------------------ #
    # Treinamento completo
    # ------------------------------------------------------------------ #
    def fit(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_val: np.ndarray | None = None,
        y_val: np.ndarray | None = None,
        epochs: int = 10,
        lr: float | None = None,
        seed: int | None = None,
    ) -> list[dict]:
        self.history = []
        self.best_metrics = None
        for ep in range(1, epochs + 1):
            metrics = self.train_one_epoch(
                X_train, y_train, X_val, y_val, lr=lr, seed=(seed or self.seed) + ep
            )
            metrics["epoch"] = ep
            self.history.append(metrics)
        # Restaura os melhores pesos encontrados
        if self._best_W is not None:
            self.model.set_weights(self._best_W, self._best_b)
        return self.history