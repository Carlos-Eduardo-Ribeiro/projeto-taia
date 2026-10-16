"""Desenha o grafo da rede (neurônios + conexões + pesos) e o histórico.

Cada camada ocupa uma coluna; cada peso é uma aresta colorida pelo sinal
(verde = positivo, vermelho = negativo) e com espessura proporcional à
magnitude. Assim é possível acompanhar o ajuste dos pesos durante as épocas.
"""

from __future__ import annotations

import numpy as np

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    HAS_MPL = True
except Exception:  # pragma: no cover
    HAS_MPL = False


def _posicoes_camada(n_neurons: int, camada: int, max_mostrar: int | None = None):
    n = min(n_neurons, max_mostrar) if max_mostrar else n_neurons
    y = np.linspace(-1, 1, n)
    return np.column_stack([np.full(n, camada), y])


def plot_network(
    model,
    ax=None,
    title: str = "Grafo da Rede Neural (pesos)",
    max_mostrar: int | None = None,
    max_edges: int = 2500,
):
    """Plota neurônios (nós) e pesos (arestas) da MLP em `ax`.

    Se houver mais conexões que `max_edges`, as arestas são amostradas
    aleatoriamente para evitar sobreposição ilegível em redes muito grandes.
    """
    if not HAS_MPL:
        raise ImportError("matplotlib é necessário para a visualização.")

    if ax is None:
        _, ax = plt.subplots(figsize=(max(6, 2.2 * model.n_layers), 6))

    layer_sizes = model.layer_sizes
    posicoes = [
        _posicoes_camada(n, l, max_mostrar=max_mostrar)
        for l, n in enumerate(layer_sizes)
    ]

    rng = np.random.default_rng(0)
    desenhar_tudo = sum(
        layer_sizes[l] * layer_sizes[l + 1] for l in range(model.n_layers)
    ) <= max_edges

    for l in range(model.n_layers):
        W = model.W[l]
        pos_a = posicoes[l]
        pos_b = posicoes[l + 1]
        amplitude = float(np.max(np.abs(W))) if W.size else 1.0
        amplitude = max(amplitude, 1e-6)

        pares = [(i, j) for i in range(pos_a.shape[0]) for j in range(pos_b.shape[0])]
        if not desenhar_tudo and len(pares) > max_edges:
            pares = rng.choice(pares, size=max_edges, replace=False)

        for ia, ib in pares:
            peso = W[ib, ia]
            largura = 0.5 + 2.0 * abs(peso) / amplitude
            cor = "#2e9e46" if peso >= 0 else "#d64550"
            ax.plot(
                [pos_a[ia, 0], pos_b[ib, 0]],
                [pos_a[ia, 1], pos_b[ib, 1]],
                color=cor,
                linewidth=largura,
                alpha=0.45,
                solid_capstyle="round",
            )

    for l, pos in enumerate(posicoes):
        cor_nos = "#1f6feb" if l == 0 else "#f5a623" if l < len(layer_sizes) - 1 else "#111111"
        ax.scatter(pos[:, 0], pos[:, 1], s=(60 if layer_sizes[l] <= 20 else 14), c=cor_nos, zorder=5, edgecolors="white", linewidths=0.6)

    for l, n in enumerate(layer_sizes):
        x = l
        rotulos = {
            0: f"Entrada\n({n})",
            len(layer_sizes) - 1: f"Saída\n({n})" + ("\n(sigmoid)" if model.is_binary else ""),
        }
        if l in rotulos:
            ax.text(x, 1.16, rotulos[l], ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_xlim(-0.6, len(layer_sizes) - 0.4)
    ax.set_ylim(-1.5, 1.6)
    ax.axis("off")
    ax.set_title(title, fontsize=11)

    legenda = [
        Line2D([0], [0], color="#2e9e46", lw=3, label="Peso positivo"),
        Line2D([0], [0], color="#d64550", lw=3, label="Peso negativo"),
    ]
    ax.legend(handles=legenda, loc="lower center", ncol=2, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.22))
    return ax.figure


def plot_history(history: list[dict], axs=None):
    """Plota loss e acurácia de treino/validação ao longo das épocas."""
    if not HAS_MPL:
        raise ImportError("matplotlib é necessário para a visualização.")

    epochs = [h["epoch"] for h in history]
    train_loss = [h["loss"] for h in history]
    train_acc = [h["accuracy"] for h in history]
    val_loss = [h.get("val_loss") for h in history]
    val_acc = [h.get("val_accuracy") for h in history]

    if axs is None:
        _, axs = plt.subplots(1, 2, figsize=(11, 4))

    axs[0].plot(epochs, train_loss, label="Treino", color="#1f6feb")
    if val_loss:
        axs[0].plot(epochs, val_loss, label="Validação", color="#d64550")
    axs[0].set_title("Loss")
    axs[0].set_xlabel("Época")
    axs[0].legend()
    axs[0].grid(alpha=0.3)

    axs[1].plot(epochs, train_acc, label="Treino", color="#1f6feb")
    if val_acc:
        axs[1].plot(epochs, val_acc, label="Validação", color="#d64550")
    axs[1].set_title("Acurácia")
    axs[1].set_xlabel("Época")
    axs[1].legend()
    axs[1].grid(alpha=0.3)

    for a in axs:
        a.tick_params(labelsize=8)
    plt.tight_layout()
    return axs[0].figure