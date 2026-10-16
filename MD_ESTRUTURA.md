# Workspace Multi-Projeto

Este repositório é um **contêiner de projetos**. Cada `projeto_N/` é um projeto
independente, e tudo que é **global/compartilhado** vive na raiz:

```
projeto_taia/                       # raiz (nível GLOBAL)
├── .venv/                          # ambiente virtual global (compartilhado)
├── requirements.txt                # dependências globais
├── .gitignore                      # regras globais (recursivas)
├── README.md                       # este arquivo: define a arquitetura
├── GIT_WORKFLOW.md                 # fluxo de versionamento (vale para todos)
├── INSTRUCOES_PESSOAIS.md          # lembrete pessoal do usuário
├── MD_OVERLEAF.md                  # conexão com o Overleaf + artigos + fluxo
├── contexto_projeto_mlp.md         # contexto da disciplina (Projeto 1)
├── .agents/                        # skills/config do harness (streamlit)
└── projeto_1/                      # MLP do Zero — AI4Good (Prática MLP-1)
    ├── app/                        # interface Streamlit
    ├── notebooks/                  # pipeline de dados
    ├── data/                       # raw/ (brutos) + processed/ (gerados)
    ├── scripts/                    # gerador do notebook
    └── src/                        # código-fonte (data, model, viz)
#   ├── projeto_2/  (futuro)
#   └── projeto_3/  (futuro)
```

## Arquitetura

- **Global (raiz):** ambiente (`requirements.txt`, `.venv/`), documentação e
  configuração (`.gitignore`, `.md`). Vale para todos os projetos.
- **Projeto (`projeto_N/`):** apenas o código e os dados do projeto. Cada projeto
  resolve seus caminhos de forma **relativa à própria pasta**
  (`src/config.py` usa `Path(__file__).parent.parent`), então os módulos continuam
  funcionando sem alteração de código após o movimento.

### Regras de uso

1. Crie sempre o novo projeto como `projeto_NN/` dentro da raiz.
2. Não duplique o ambiente: instale uma única vez na raiz (`.venv` global).
3. Documentação geral vai na raiz; o que é específico de um projeto pode entrar no
   próprio `projeto_N/` (gitignorado por padrão via `*.md`).
4. Comandos que dependem do cwd devem ser executados de dentro do projeto
   (ver abaixo).

## Configuração do ambiente (uma única vez)

```bash
# na raiz do repositório
python3 -m venv .venv
# (se o pip não for criado junto no Python 3.14, executar uma vez:)
.venv/bin/python3 <(curl -sS https://bootstrap.pypa.io/get-pip.py)
.venv/bin/pip install -r requirements.txt
```

## Projetos

### Projeto 1 — MLP do Zero (AI4Good, Prática MLP-1)

Rede MLP construída 100% do zero em Python (feed-forward, back-propagation e
gradiente descendente manuais, sem TensorFlow/PyTorch). Entregáveis: notebook de
pipeline de dados e interface Streamlit com controle total de
arquitetura/hiperparâmetros, execução por época e grafo da rede com os pesos.

**Execução** (sempre a partir da pasta `projeto_1/`):

```bash
# notebook (pipeline)
cd projeto_1
../.venv/bin/jupyter nbconvert --to notebook --execute notebooks/01_pipeline_dados.ipynb --inplace

# interface Streamlit
../.venv/bin/streamlit run app/streamlit_app.py
```

> O ponto de entrada da aplicação e o `src/config.py` resolvem os caminhos de dados
> relativos à própria `projeto_1/`, então funcionam mesmo executados a partir da
> raiz: `.venv/bin/streamlit run projeto_1/app/streamlit_app.py`.

**Notas técnicas:** inicialização He (ReLU) / Xavier (sigmoid/tanh); saída sigmoide +
BCE; back-propagation validado por gradiente numérico (erro ~1e-10); `Trainer`
restaura os pesos da melhor época e guarda o histórico.

**Bases:** `heart.csv` (principal, 80/20) e `diabetic_data.csv` +
`IDS_mapping.csv` (desafio).

## Artigos científicos (Overleaf)

Todo projeto que envolva artigo de referência publica seu **artigo científico** (LaTeX
LNCS) no Overleaf via `MD_OVERLEAF.md` (credenciais, procedimento de criar →
compilar → validar → push, e atualizações do artigo vigente). Os `main documents`
ficam na raiz do repositório Overleaf; o restante é organizado por conteúdo
(classe do template em `template_llncs/`, figuras por projeto). Artigos publicados:

- Projeto 1: `artigo_mlp_do_zero.tex` (figuras em `projeto_1_mlp_do_zero/figs/`).
- Projeto 2: `artigo_ae_do_zero.tex` (figuras em `projeto_2_ae_anomalias/figs/`).

Os `.tex` vivem no **clone Overleaf** (em `/tmp/opencode/overleaf/` durante as
sessões); o relatório-fonte fica em `projeto_N/report/relatorio_tecnico.md`.