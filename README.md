# MLP do Zero — AI4Good (Prática MLP-1)

Rede neural **MLP (Multi-Layer Perceptron) construída 100% do zero em Python**:
feed-forward, back-propagation e gradient descent implementados manualmente com
`numpy` (sem TensorFlow, PyTorch ou scikit-learn). Bibliotecas de dados
(`pandas`/`numpy`) são usadas apenas para o pré-processamento.

Entregáveis: **notebook** que documenta o pipeline de dados e uma **interface
Streamlit** com controle total da arquitetura/hiperparâmetros, execução passo a
passo, grafo da rede com os pesos e relatório no padrão da disciplina.

## Estrutura

```
projeto_taia/
├── app/
│   └── streamlit_app.py        # interface interativa (etapa B)
├── notebooks/
│   └── 01_pipeline_dados.ipynb # pipeline completo (etapa A)
├── data/
│   ├── raw/                    # bases brutas (heart, diabetic, IDS_mapping)
│   └── processed/              # artefatos processados (gerados)
├── scripts/
│   └── gerar_notebook.py       # regenera o notebook (opcional)
├── src/
│   ├── config.py               # caminhos e constantes
│   ├── data/                   # load_data.py e preprocess.py
│   ├── model/                  # activations.py, mlp.py, trainer.py
│   └── viz/                    # graph_plot.py (grafo da rede + curvas)
├── requirements.txt
└── README.md
```

## Configuração do ambiente

```bash
# na raiz do projeto, criar o venv e instalar as dependências
python3 -m venv .venv
# (se o pip não for criado junto no Python 3.14, executar uma vez:)
.venv/bin/python3 <(curl -sS https://bootstrap.pypa.io/get-pip.py)
.venv/bin/pip install -r requirements.txt
```

> No Python 3.14 o módulo `ensurepip` pode não estar disponível; o passo do
> `get-pip.py` garante o pip dentro do venv. As versões em `requirements.txt`
> foram validadas neste Python.

## Execução

1. **Notebook (pipeline de dados)**

   Abra `notebooks/01_pipeline_dados.ipynb` no VS Code e selecione o kernel do
   `.venv`, ou execute por linha de comando:

   ```bash
   .venv/bin/jupyter nbconvert --to notebook --execute notebooks/01_pipeline_dados.ipynb --inplace
   ```

2. **Interface Streamlit**

   ```bash
   .venv/bin/streamlit run app/streamlit_app.py
   ```

   Acesse o endereço indicado (padrão `http://localhost:8501`).

## Uso da interface

- **Sidebar** — autor/equipe, base de dados, quantidade de camadas ocultas e
  neurônios por camada, ativação (relu/sigmoid/tanh), learning rate, épocas,
  batch size, tratamento de outliers, padronização e seed.
- **Treinar** executa todas as épocas de uma vez.
- **Avançar 1 época** executa o treino passo a passo, atualizando o grafo da
  rede (arestas = pesos) e as curvas de loss/acurácia a cada época.
- **Resetar modelo** reinicia os pesos.
- Ao final, o **relatório do melhor modelo** exibe acurácia, learning rate,
  ativação, arquitetura, pré-processamento, comentários e o grafo dos pesos
  finais (padrão do exercício).

## Bases de dados

- `heart.csv` — Heart Disease (base principal). Split **80% treino / 20% teste**.
- `diabetic_data.csv` + `IDS_mapping.csv` — Diabetes 130-US Hospitals (desafio);
  o IDS_mapping é usado para interpretar os IDs de admissão/alta/origem.

## MLP do zero — notas técnicas

- Inicialização He (ReLU) / Xavier (sigmoid/tanh).
- Saída sigmoide + Binary Cross-Entropy (classificação binária).
- Back-propagation validado por **gradiente numérico** (erro ~1e-10 nas
  ativações relu/sigmoid/tanh).
- O `Trainer` restaura os pesos da melhor época (menor loss de validação) e
  guarda o histórico completo para as curvas.