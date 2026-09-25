"""Interface Streamlit para treinar e inspecionar a MLP do zero.

Execução (a partir da raiz do projeto):
    streamlit run app/streamlit_app.py
"""

import sys
from pathlib import Path

import streamlit as st

PROJETO = Path(__file__).resolve().parent.parent
if str(PROJETO) not in sys.path:
    sys.path.insert(0, str(PROJETO))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from src.config import RANDOM_STATE  # noqa: E402
from src.data.load_data import load_diabetic, load_heart, load_ids_mapping  # noqa: E402
from src.data.preprocess import (  # noqa: E402
    PreprocessDiabetic,
    StandardScaler,
    clip_outliers,
    preprocess_heart,
    split_train_test,
)
from src.model.mlp import MLP  # noqa: E402
from src.model.trainer import Trainer  # noqa: E402
from src.viz.graph_plot import plot_history, plot_network  # noqa: E402

st.set_page_config(page_title="MLP do Zero — AI4Good", layout="wide")

ATIVACOES = ["relu", "sigmoid", "tanh"]
DATASETS = ["Heart Disease (heart.csv)", "Diabetes 130-US (diabetic_data.csv)"]
COMENTARIO_PADRAO = (
    "MLP codificada do zero como grafo, com feed-forward e back-propagation manuais. "
    "Redes maiores chegaram a boa acurácia no treino, mas caíam no teste por overfitting; "
    "a arquitetura enxuta generalizou melhor."
)


# --------------------------------------------------------------------------- #
# Dados (cache)
# --------------------------------------------------------------------------- #
@st.cache_data(show_spinner="Carregando e pré-processando dados...")
def preparar_dados(dataset: str, clip: bool, standardize: bool, seed: int):
    ids = None
    if dataset.startswith("Heart"):
        X, y = preprocess_heart(load_heart())
        if clip:
            X = clip_outliers(X, ["age", "trestbps", "chol", "thalach", "oldpeak"])
        nomes = list(X.columns)
    else:
        ids = load_ids_mapping()
        X, y = PreprocessDiabetic(binary_target=True).transform(load_diabetic(), ids)
        if clip:
            X = clip_outliers(
                X,
                ["time_in_hospital", "num_lab_procedures", "num_medications", "number_diagnoses"],
            )
        nomes = list(X.columns)

    X_tr, X_te, y_tr, y_te = split_train_test(X, y, random_state=seed)

    scaler = None
    X_tr_n, X_te_n = np.asarray(X_tr, float), np.asarray(X_te, float)
    if standardize:
        scaler = StandardScaler().fit(X_tr_n)
        X_tr_n = scaler.transform(X_tr_n)
        X_te_n = scaler.transform(X_te_n)

    return {
        "X_train": X_tr_n,
        "X_test": X_te_n,
        "y_train": y_tr.to_numpy() if hasattr(y_tr, "to_numpy") else np.asarray(y_tr),
        "y_test": y_te.to_numpy() if hasattr(y_te, "to_numpy") else np.asarray(y_te),
        "n_features": X_tr_n.shape[1],
        "feature_names": nomes,
        "scaler": scaler,
        "target_desc": (
            "1 = doença cardíaca presente; 0 = ausente"
            if dataset.startswith("Heart")
            else "1 = readmitido em <30 dias; 0 = caso contrário"
        ),
    }


# --------------------------------------------------------------------------- #
# Construção do modelo a partir dos controles
# --------------------------------------------------------------------------- #
def montar_modelo(n_features: int, ocultas: list[int], ativacao: str) -> MLP:
    camadas = [n_features] + ocultas + [1]
    return MLP(camadas, hidden_activation=ativacao, output_activation="sigmoid", seed=RANDOM_STATE)


def retomar_trainer(modelo: MLP, lr: float, batch_size: int | None, seed: int) -> Trainer:
    treinador = Trainer(modelo, lr=lr, batch_size=batch_size, seed=seed)
    treinador.history = list(st.session_state.get("history", []))
    if st.session_state.get("best_metrics"):
        treinador.best_metrics = dict(st.session_state["best_metrics"])
    w = st.session_state.get("best_W")
    b = st.session_state.get("best_b")
    if w and b:
        treinador._best_W = w
        treinador._best_b = b
    return treinador


def salvar_melhor(treinador: Trainer) -> None:
    st.session_state["best_metrics"] = treinador.best_metrics
    if treinador._best_W is not None:
        st.session_state["best_W"] = treinador._best_W
        st.session_state["best_b"] = treinador._best_b


# --------------------------------------------------------------------------- #
# Sidebar — controles
# --------------------------------------------------------------------------- #
with st.sidebar:
    st.header("Configuração")
    autor = st.text_input("Nome do Autor/Equipe", value="Carlos Eduardo")

    dataset = st.selectbox("Base de dados", DATASETS, index=0)

    st.subheader("Arquitetura")
    n_ocultas = st.number_input("Camadas ocultas", min_value=1, max_value=5, value=2, step=1)
    ocultas = []
    for i in range(int(n_ocultas)):
        ocultas.append(
            st.number_input(f"Neurônios da camada oculta {i + 1}", min_value=1, max_value=64, value=8, step=1)
        )
    ativacao = st.selectbox("Ativação das camadas ocultas", ATIVACOES, index=0)

    st.subheader("Hiperparâmetros")
    lr = st.number_input("Learning rate", min_value=0.0001, max_value=1.0, value=0.05, step=0.005, format="%.4f")
    epochs = st.slider("Épocas", min_value=1, max_value=500, value=100, step=1)
    batch_size = st.selectbox("Batch size", ["Gradiente completo", 16, 32, 64, 128, 256], index=1)
    batch_size = None if batch_size == "Gradiente completo" else int(batch_size)

    st.subheader("Pré-processamento")
    clip = st.checkbox("Tratar outliers (winsorização IQR)", value=True)
    standardize = st.checkbox("Padronizar (z-score)", value=True)
    seed = st.number_input("Seed (split/inicialização)", min_value=0, max_value=9999, value=RANDOM_STATE, step=1)

    st.subheader("Execução")
    col_a, col_b = st.columns(2)
    treinar_full = col_a.button("Treinar", type="primary", width="stretch")
    passo = col_b.button("Avançar 1 época", width="stretch")
    reset = st.button("Resetar modelo", width="stretch")

# --------------------------------------------------------------------------- #
# Estado e carregamento
# --------------------------------------------------------------------------- #
params = (dataset, int(n_ocultas), tuple(int(v) for v in ocultas), ativacao, float(lr), batch_size, clip, standardize, int(seed))

if "last_params" not in st.session_state or st.session_state["last_params"] != params:
    st.session_state["last_params"] = params
    st.session_state["dados"] = preparar_dados(dataset, clip, standardize, int(seed))
    st.session_state["modelo"] = montar_modelo(st.session_state["dados"]["n_features"], [int(v) for v in ocultas], ativacao)
    st.session_state["history"] = []
    st.session_state["best_metrics"] = None

dados = st.session_state["dados"]

if reset:
    st.session_state["modelo"] = montar_modelo(dados["n_features"], [int(v) for v in ocultas], ativacao)
    st.session_state["history"] = []
    st.session_state["best_metrics"] = None
    st.session_state["best_W"] = None
    st.session_state["best_b"] = None
    st.rerun()

modelo: MLP = st.session_state["modelo"]

treinador = retomar_trainer(modelo, lr, batch_size, int(seed))

if treinar_full:
    with st.spinner(f"Treinando por {epochs} épocas..."):
        hist = treinador.fit(
            dados["X_train"], dados["y_train"],
            dados["X_test"], dados["y_test"],
            epochs=int(epochs), lr=float(lr), seed=int(seed),
        )
    st.session_state["history"] = treinador.history
    salvar_melhor(treinador)

if passo:
    ep = len(st.session_state.get("history", [])) + 1
    with st.spinner(f"Treinando época {ep}..."):
        metrica_ep = treinador.train_one_epoch(
            dados["X_train"], dados["y_train"],
            dados["X_test"], dados["y_test"],
            lr=float(lr), seed=int(seed) + ep,
        )
    metrica_ep["epoch"] = ep
    historico_atual = list(st.session_state.get("history", []))
    historico_atual.append(metrica_ep)
    st.session_state["history"] = historico_atual
    salvar_melhor(treinador)

historico = st.session_state.get("history", [])
best_metrics = st.session_state.get("best_metrics")

# --------------------------------------------------------------------------- #
# Corpo principal
# --------------------------------------------------------------------------- #
st.title("Rede Neural MLP do Zero")
st.caption("Implementação manual em numpy: feed-forward, back-propagation e gradient descent — sem TensorFlow/PyTorch.")
st.caption(f"Target: {dados['target_desc']} | Features: {dados['n_features']} | Base: {dataset}")

if not historico:
    st.info("Configure o modelo na barra lateral e pressione **Treinar** (ou avance época por época).")
else:
    col_graf, col_curva = st.columns([3, 2])
    with col_graf:
        fig_rede = plot_network(
            modelo,
            title=f"Grafo da Rede — arquitectura {modelo.info()['architecture']} — época {len(historico)}",
        )
        st.pyplot(fig_rede, width="stretch")
    with col_curva:
        fig_hist = plot_history(historico)
        st.pyplot(fig_hist, width="stretch")

    ep_atual = historico[-1]["epoch"]
    m3 = st.columns(4)
    m3[0].metric("Época", int(ep_atual))
    m3[1].metric("Loss (treino)", f"{historico[-1]['loss']:.4f}")
    m3[2].metric("Acurácia (treino)", f"{historico[-1]['accuracy']:.4f}")
    m3[3].metric("Acurácia (teste)", f"{historico[-1].get('val_accuracy', 0):.4f}")

    st.divider()
    st.subheader("Relatório do melhor modelo")

    if best_metrics:
        acc_final = best_metrics.get("val_accuracy", best_metrics.get("accuracy", 0))
        st.markdown(
            f"### **{acc_final:.4f}** : {autor}",
            unsafe_allow_html=False,
        )
        st.write("**accuracy**:", f"{acc_final:.4f}")
        st.write("**learning rate**:", f"{lr:.4f}")
        st.write("**activation**:", ativacao)
        st.write("**architecture**:", modelo.info()["architecture"])
        st.write("**pre-processing**:", "standardize" if standardize else "sem padronização")
        comentario = st.text_area("comentários", value=COMENTARIO_PADRAO, height=90)
        st.write("**Grafo dos Pesos Finais**")
        fig_final = plot_network(
            modelo,
            title=f"Pesos finais ({modelo.info()['architecture']})",
            max_mostrar=None,
        )
        st.pyplot(fig_final, width="stretch")

    acc_teste = treinador._accuracy(dados["X_test"], dados["y_test"])
    st.download_button(
        "Baixar histórico (CSV)",
        pd.DataFrame(historico).to_csv(index=False).encode("utf-8"),
        file_name="historico_treino.csv",
        mime="text/csv",
    )

st.divider()
st.subheader("Testar modelo no conjunto de teste (20%)")
if st.button("Calcular acurácia no teste", width="stretch"):
    acc = treinador._accuracy(dados["X_test"], dados["y_test"])
    st.success(f"Acurácia no teste (20%): **{acc:.4f}**")