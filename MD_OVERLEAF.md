# Conexão com o Overleaf

Este documento define como a IA deve **criar, compilar e publicar no Overleaf** o
artigo científico de cada projeto, incluindo atualizações do artigo vigente.

Token (usado como senha do git):

`olp_0LLg2W8q8S4Hu8OiEdrbFRVV7mFZsw14lt28`

Clone do projeto (usuário `git`, senha = token acima):

```bash
git clone https://git@git.overleaf.com/6a920bb7b8e36eb1e2f1804c
```

**Aviso de segurança:** o token fica gravado nos remotes do clone local
(`git remote -v` mostra a URL com senha). Não commitar/pushar esse token em nenhum
repositório público; nunca commitá-lo no repositório do GitHub.

## Estrutura do repositório Overleaf

Os `main documents` (`artigo_*.tex`) ficam **na raiz** do repositório Overleaf
(exigência do Overleaf para compilar corretamente), e o restante é organizado por
conteúdo em pastas:

```
├── artigo_mlp_do_zero.tex         # Projeto 1 — MLP do Zero (main document)
├── artigo_ae_do_zero.tex          # Projeto 2 — AE / Detecção de Anomalias (main document)
├── README.md                      # estrutura do repositório Overleaf
├── template_llncs/                # classe LNCS + material do template (Springer)
│   ├── llncs.cls                  # classe (referenciada pelos artigos)
│   ├── splncs04.bst               # estilo BibTeX (sample)
│   ├── samplepaper.tex            # artigo de exemplo do template
│   ├── fig1.eps                   # figura de exemplo do template
│   ├── readme.txt                 # readme do pacote LNCS
│   ├── history.txt                # histórico de versões do pacote
│   └── llncsdoc.pdf               # documentação da classe
├── projeto_1_mlp_do_zero/figs/    # figuras do artigo do Projeto 1
└── projeto_2_ae_anomalias/figs/   # figuras do artigo do Projeto 2
```

A classe é referenciada nos artigos como
`\documentclass[runningheads]{template_llncs/llncs}` e as figuras por caminho
relativo à raiz (o Overleaf compila com o diretório de trabalho na raiz).

## Fluxo obrigatório (Etapa 5.1 do MD_MESTRE)

Sempre que um `projeto_N/` que envolva artigo de referência for concluído (ou o
artigo vigente for alterado), executar, nesta ordem:

### 1. Gerar o `.tex` do artigo do projeto vigente

- Fonte dos textos: `projeto_N/report/relatorio_tecnico.md`.
- Figuras: copiar as necessárias de `projeto_N/results/figs/` para a pasta de
  figuras do Overleaf do projeto correspondente (ex.: `projeto_1_mlp_do_zero/figs/`
  para o Projeto 1, `projeto_2_ae_anomalias/figs/` para o Projeto 2).
- Formato: **LNCS** (`\documentclass[runningheads]{template_llncs/llncs}`), em
  português.
- Pacotes obrigatórios: `graphicx`, `amsmath`, `booktabs`, `cite` (necessário para o
  Multi-cite `\cite{a, b}` funcionar com a classe `llncs` — sem o `cite`, a 2ª chave
  não resolve e gera `[?]`) e `hyperref` (hidelinks).
- Reaproveitar o padrão dos artigos já publicados (`artigo_mlp_do_zero.tex`,
  `artigo_ae_do_zero.tex`).

### 2. Compilar localmente

```bash
cd <clone_overleaf>                                    # a partir da raiz (como o Overleaf)
pdflatex -interaction=nonstopmode artigo_<projeto>.tex   # repetir 2–3x
```

Corrigir erros até gerar PDF.

### 3. Validar o PDF

- Gerado sem `! LaTeX Error` / `Fatal error`;
- Sem citações `[?]` (undefined) — exige o pacote `cite` para Multi-cite;
- Conteúdo conferido (páginas, métricas do relatório, diagrama de arquitetura).

### 4. Push no Overleaf

```bash
git pull --rebase origin main        # antes de push (Overleaf pode ter autocommit "Update on Overleaf")
git add artigo_<projeto>.tex projeto_<N>_<tema>/ README.md
git commit -m "feat: adicionar artigo cientifico <projeto> (<tema>)"
git push origin main
```

O Overleaf compila o PDF automaticamente após o push.

### 5. Atualização do artigo vigente

Se o `projeto_N/` vigente **já tiver artigo publicado** e o relatório/resultados
mudarem (novas métricas, figuras, texto), repetir os passos 1–4 — **editando o mesmo
`.tex`** (não criar duplicado), com mensagem de commit indicando a atualização
(ex.: `docs: atualizar artigo AE (AUC 86.8, MSE novo)`) e novo push.

## Documentos publicados neste projeto Overleaf (template LNCS)

| Arquivo (raiz) | Projeto | Figuras | Notas |
|---|---|---|---|
| `artigo_mlp_do_zero.tex` | Projeto 1 — MLP do Zero | `projeto_1_mlp_do_zero/figs/` (fig_curvas, fig_grafo, fig_comparativo) | Primeiro artigo publicado |
| `artigo_ae_do_zero.tex` | Projeto 2 — AE/Detecção de Anomalias | `projeto_2_ae_anomalias/figs/` (curvas_treino, curvas_roc, scores_distribuicao, reconstrucoes, score_amostras, latente_pca, treino_modificado) | Requer pacote `cite`; 8 páginas validado localmente |

> Ao adicionar um novo projeto com artigo, incluir nova linha nesta tabela.