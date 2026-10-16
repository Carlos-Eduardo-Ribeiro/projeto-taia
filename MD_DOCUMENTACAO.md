# MD_DOCUMENTACAO — Regras de Documentação

Documento de instrução do workspace `projeto_taia`. Define o que a IA deve documentar
e como deve organizar os documentos gerados.

## 1. Princípio

> Toda entrega deve ser rastreável: código → dados → fontes → resultados.

A IA deve documentar:

1. o que foi solicitado;
2. o que foi feito (implementação);
3. como validou (testes);
4. quais fontes foram consultadas (artigos, datasets, repositórios);
5. quais números são do artigo e quais são da reprodução/experimento.

## 2. Onde documentar

### Global (raiz `projeto_taia/`)

- `MD_MESTRE.md`, `MD_ESTRUTURA.md`, `MD_GITFLOW.md`, `MD_OVERLEAF.md`,
  `MD_TESTES.md`, `MD_DOCUMENTACAO.md` — regras comuns a todos os projetos.

### Por projeto (`projeto_N/`)

- `README.md` — visão geral, como rodar, estrutura de pastas.
- `contexto*.md` — o enunciado da atividade.
- `artigo/referencia.md` — identificação e fontes do artigo usado.
- `report/relatorio_tecnico.md` — relatório da tarefa.
- `data/README.md` — origem e descrição dos dados.
- `results/` — artefatos de resultado (`.npz`, `.json`, figuras) com um resumo.

### Artigo científico publicado (Overleaf)

- Todo projeto que envolva artigo de referência gera/publica no **Overleaf** o
  `.tex` do artigo próprio (LNCS). Procedimento e publicações: `MD_OVERLEAF.md`
  (Etapa 5.1 do `MD_MESTRE.md`). O Overleaf compila sozinho após o push; o PDF
  publicado é o artefato final revisado.

## 3. Proibições

- **Nunca inventar** autores, DOIs, datasets, links, métricas, quantidades de
  parâmetros, arquiteturas ou resultados.
- Nunca apresentar hipótese como fato. Separar:
  - **Dado documentado** (o artigo informa X);
  - **Resultado obtido** (na reprodução obteve-se Y);
  - **Interpretação** (uma possível explicação é Z).
- Quando não for possível verificar: escrever *informação não verificada* ou
  *não foi possível confirmar essa informação na fonte consultada*.
- Documentação sempre em Português, exceto nomes próprios e termos técnicos.

## 4. Formato

- Arquivos `.md` legíveis, com títulos e tabelas simples.
- Figuras em `results/figs/` referenciadas por caminho relativo.
- Tabelas de comparação quantitativa com fonte da evidência indicada.