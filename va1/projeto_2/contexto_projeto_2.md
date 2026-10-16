# AUTOENCODER (AE)

## 1. Objetivo geral

Realizar a prática da disciplina **Tópicos em IA — AI4Good**, cujo objetivo é selecionar uma rede neural existente, reproduzi-la em uma base de dados existente, modificar sua arquitetura, retreiná-la e comparar quantitativamente e qualitativamente os resultados antes e depois da modificação.

### Tipo de rede obrigatório
A rede escolhida deve ser um **Autoencoder (AE)**.

Não utilizar CNN, RNN, LSTM ou GNN como modelo principal. O projeto deve permanecer centrado em uma arquitetura de Autoencoder.

---

## 2. Requisitos da atividade

A solução final deve atender aos seguintes requisitos:

1. Selecionar um artigo científico publicado **a partir de 2023**.
2. O artigo deve utilizar uma arquitetura baseada em **Autoencoder (AE)**.
3. O artigo deve ser localizado/confirmado por meio do **Google Scholar (Google Acadêmico)**.
4. Identificar a base de dados utilizada pelo trabalho.
5. Localizar o código da implementação original ou uma implementação oficial/reproduzível associada ao artigo.
6. Baixar/obter o código e os dados necessários.
7. Fazer a implementação funcionar localmente.
8. Executar a inferência do modelo original.
9. Modificar substancialmente a arquitetura do Autoencoder.
10. Retreinar o modelo modificado utilizando a **mesma base de dados**.
11. Executar a inferência do modelo modificado.
12. Comparar o modelo original e o modificado quantitativamente.
13. Comparar os modelos qualitativamente.
14. Produzir um relatório técnico contendo metodologia, motivação, implementação e resultados.
15. O relatório deve ser revisado criticamente para evitar afirmações sem evidência, números inventados ou informações não verificadas.

### Desafio opcional da disciplina

Caso seja viável, considerar posteriormente:

- executar o modelo em um segundo dataset;
- aplicar uma segunda técnica nos dois datasets;
- comparar os resultados.

A segunda técnica deve ser uma técnica de referência/estado da arte adequada ao problema e aos datasets.

O desafio opcional não deve comprometer a entrega principal.

---

## 3. Fonte do artigo

### Regra obrigatória

O artigo deve ser pesquisado no **Google Scholar / Google Acadêmico**.

Não escolher um artigo simplesmente porque apareceu em uma busca comum. A LLM deve:

1. pesquisar no Google Scholar por trabalhos de 2023 em diante;
2. verificar título, autores, ano e publicação;
3. confirmar que o trabalho realmente utiliza Autoencoder;
4. verificar se o dataset utilizado está disponível;
5. verificar se existe código reproduzível;
6. verificar se a arquitetura pode ser executada e modificada;
7. verificar se há métricas suficientes para comparar o modelo original e o modificado.

### Critérios para seleção do artigo

Priorizar artigos que possuam:

- publicação em 2023 ou posterior;
- Autoencoder como componente central;
- dataset público;
- código público no GitHub, página oficial, repositório dos autores ou fonte equivalente;
- arquitetura claramente descrita;
- métricas de avaliação reproduzíveis;
- quantidade de dados e custo computacional compatíveis com um projeto acadêmico;
- possibilidade real de modificar a arquitetura sem descaracterizar o modelo.

Evitar artigos que:

- não disponibilizem dados;
- utilizem datasets impossíveis de obter;
- dependam de infraestrutura inacessível;
- tenham código inexistente ou impossível de reproduzir;
- utilizem AE apenas como componente secundário;
- não permitam uma comparação clara antes/depois.

---

## 4. Processo de pesquisa do artigo

Primeiro faça uma busca ampla no Google Scholar.

Sugestões de consultas:

- `"autoencoder" "2023" anomaly detection`
- `"autoencoder" "2024" dataset GitHub`
- `"autoencoder" "2025" deep learning dataset`
- `"autoencoder" anomaly detection public dataset`
- `"deep autoencoder" 2023 anomaly detection`
- `"denoising autoencoder" 2023 dataset`

Depois filtre os resultados pelos critérios desta especificação.

Para cada candidato, registre:

- título;
- autores;
- ano;
- periódico/conferência;
- DOI ou identificador;
- problema abordado;
- tipo de Autoencoder;
- dataset;
- métricas;
- disponibilidade do código;
- disponibilidade do dataset;
- dificuldade estimada de reprodução;
- possibilidade de modificação arquitetural.

Não invente nenhuma dessas informações.

---

## 5. Escolha do problema

A aplicação pode ser, por exemplo:

- detecção de anomalias;
- reconstrução de dados;
- redução de dimensionalidade;
- representação latente;
- compressão;
- detecção de outliers;
- classificação baseada em representação aprendida.

A escolha deve ser determinada principalmente pela existência de artigo, dataset e código reproduzíveis.

Se houver mais de um candidato viável, apresentar os candidatos com seus fatos verificáveis e escolher aquele que melhor atende aos requisitos técnicos da atividade, sem inventar disponibilidade de código ou dados.

---

## 6. Modelo base

Depois de selecionar o artigo, reproduzir o máximo possível da arquitetura original.

Documentar:

- entrada;
- pré-processamento;
- Encoder;
- dimensão do espaço latente;
- Decoder;
- funções de ativação;
- função de perda;
- otimizador;
- learning rate;
- batch size;
- número de épocas;
- critérios de parada;
- divisão treino/validação/teste;
- métricas;
- threshold, caso exista;
- demais hiperparâmetros relevantes.

A arquitetura original deve ser representada visualmente ou em uma descrição equivalente.

Exemplo conceitual:

```text
Entrada
   ↓
Encoder
   ↓
Espaço Latente / Bottleneck
   ↓
Decoder
   ↓
Reconstrução
```

Não assumir que a arquitetura acima corresponde ao artigo escolhido. Adaptar a descrição ao artigo real.

---

## 7. Reprodução do modelo original

Antes de modificar qualquer coisa:

1. preparar o ambiente;
2. instalar dependências;
3. baixar/preparar o dataset;
4. executar o pré-processamento;
5. executar o treinamento;
6. salvar o modelo;
7. executar a inferência;
8. calcular as métricas;
9. gerar os gráficos/resultados necessários;
10. registrar problemas de reprodução.

A inferência do modelo original deve estar funcionando antes da alteração arquitetural.

### Evidência obrigatória

A apresentação deve conseguir mostrar:

- código executando;
- modelo original treinado;
- inferência funcionando;
- resultados obtidos;
- dados utilizados.

---

## 8. Modificação da arquitetura

A modificação deve ser **substancial e tecnicamente justificável**.

Possíveis modificações, dependendo da arquitetura original:

- adicionar/remover camadas;
- alterar profundidade do Encoder;
- alterar profundidade do Decoder;
- alterar dimensão do bottleneck;
- alterar número de neurônios;
- adicionar Dropout;
- adicionar Batch Normalization;
- alterar funções de ativação;
- alterar a simetria Encoder/Decoder;
- adicionar conexões residuais, se fizer sentido;
- alterar a estratégia de compressão;
- alterar outro componente estrutural relevante.

Não alterar apenas hiperparâmetros e apresentar isso como mudança de arquitetura.

A modificação deve possuir uma **motivação técnica**.

Exemplo:

> A arquitetura foi modificada para aumentar/reduzir a capacidade de representação do modelo, buscando verificar se uma representação latente diferente melhora a reconstrução/detecção de anomalias no dataset utilizado.

A justificativa final deve ser específica ao artigo e aos resultados observados.

---

## 9. Experimento controlado

Sempre que possível, manter constantes os fatores que não fazem parte da modificação arquitetural.

Por exemplo:

- mesmo dataset;
- mesmo pré-processamento;
- mesma divisão dos dados;
- mesmo número de épocas;
- mesmo batch size;
- mesmo otimizador;
- mesmo learning rate;
- mesma métrica;
- mesmo procedimento de avaliação.

Se algum parâmetro precisar ser alterado, registrar explicitamente:

- o que mudou;
- por que mudou;
- qual impacto isso pode causar na comparação.

O objetivo é permitir uma comparação justa entre:

**AE original × AE modificado**

---

## 10. Comparação quantitativa

A comparação deve utilizar métricas adequadas ao problema do artigo.

Dependendo da tarefa, podem ser utilizadas:

- MSE;
- MAE;
- RMSE;
- erro de reconstrução;
- Accuracy;
- Precision;
- Recall;
- F1-score;
- ROC-AUC;
- PR-AUC;
- tempo de treinamento;
- número de parâmetros;
- tamanho do modelo;
- tempo de inferência.

Não utilizar métricas apenas porque são comuns. Escolher métricas coerentes com a tarefa.

Para cada métrica, explicar:

- o que ela mede;
- por que ela é relevante;
- resultado do modelo original;
- resultado do modelo modificado.

---

## 11. Comparação qualitativa

Além dos números, analisar visualmente o comportamento dos modelos.

Exemplos:

- reconstrução original versus reconstrução modificada;
- exemplos corretamente reconstruídos;
- exemplos com maior erro;
- gráficos de loss;
- curvas de treinamento/validação;
- distribuição do erro de reconstrução;
- exemplos de anomalias detectadas;
- casos de falso positivo/falso negativo, quando aplicável.

Toda interpretação deve estar relacionada aos resultados realmente observados.

---

## 12. Controle contra alucinações

A LLM deve seguir estas regras durante todo o projeto:

### Nunca inventar

Não inventar:

- artigos;
- autores;
- DOI;
- datasets;
- links;
- resultados;
- métricas;
- quantidade de parâmetros;
- arquitetura;
- código;
- experimentos;
- citações.

### Separar evidência de interpretação

Diferenciar claramente:

**Dado documentado**
> O artigo informa X.

**Resultado obtido no experimento**
> Na reprodução realizada, foi obtido Y.

**Interpretação**
> Uma possível explicação para Y é Z.

Não apresentar uma hipótese como fato.

### Caso não seja possível verificar

Escrever:

> Informação não verificada.

ou:

> Não foi possível confirmar essa informação na fonte consultada.

Não preencher a lacuna com conhecimento inventado.

---

## 13. Relatório técnico

O relatório final deve conter, no mínimo:

### 1. Introdução

- problema;
- contexto;
- objetivo;
- importância da tarefa.

### 2. Artigo selecionado

- título;
- autores;
- ano;
- publicação;
- problema;
- contribuição principal;
- arquitetura AE utilizada.

### 3. Dataset

- nome;
- origem;
- quantidade de dados;
- características;
- divisão utilizada;
- pré-processamento.

### 4. Metodologia

- arquitetura original;
- treinamento;
- métricas;
- ambiente;
- implementação.

### 5. Modificação proposta

- alteração realizada;
- arquitetura antes/depois;
- motivação;
- hipótese experimental.

### 6. Resultados

- modelo original;
- modelo modificado;
- métricas;
- gráficos;
- exemplos;
- comparação.

### 7. Discussão

Explicar:

- o que mudou;
- por que os resultados mudaram;
- possíveis causas;
- limitações;
- efeitos de overfitting/underfitting, quando observados.

### 8. Conclusão

Apresentar somente conclusões sustentadas pelos experimentos.

### 9. Referências

Utilizar as referências reais consultadas.

---

## 14. Entregáveis esperados

Ao final do trabalho, organizar:

```text
projeto/
├── README.md
├── contexto.md
├── artigo/
│   ├── referencia.md
│   └── artigo.pdf                 # se permitido/disponível
├── data/
│   └── README.md
├── src/
│   ├── modelo_original/
│   └── modelo_modificado/
├── notebooks/
├── experiments/
├── results/
│   ├── original/
│   └── modified/
└── report/
    └── relatorio_tecnico.md
```

A estrutura pode ser adaptada ao repositório real.

---

## 15. Fluxo de execução obrigatório

Siga esta ordem:

```text
1. Ler este contexto
        ↓
2. Pesquisar artigos no Google Scholar
        ↓
3. Filtrar artigos de 2023+
        ↓
4. Confirmar que o modelo é AE
        ↓
5. Verificar dataset público
        ↓
6. Verificar código reproduzível
        ↓
7. Selecionar artigo
        ↓
8. Registrar referência e fontes
        ↓
9. Obter dataset
        ↓
10. Reproduzir modelo original
        ↓
11. Executar inferência original
        ↓
12. Registrar resultados
        ↓
13. Projetar modificação arquitetural
        ↓
14. Implementar modificação
        ↓
15. Retreinar AE modificado
        ↓
16. Executar inferência modificada
        ↓
17. Comparar quantitativamente
        ↓
18. Comparar qualitativamente
        ↓
19. Analisar resultados
        ↓
20. Produzir relatório técnico
        ↓
21. Revisar evidências e referências
        ↓
22. Organizar entrega
```

Não pular diretamente para a implementação antes de confirmar artigo, dataset e código.

---

## 16. Regra sobre ferramentas de pesquisa

Quando houver acesso à internet:

- usar Google Scholar para localizar o artigo;
- usar a página oficial do artigo, DOI, periódico/conferência e repositório dos autores para confirmação;
- usar GitHub ou outra fonte oficial para código;
- usar a fonte oficial do dataset sempre que possível.

A busca comum na web pode ser utilizada para complementar a pesquisa, mas a seleção do artigo deve ser baseada na busca/confirmacão no Google Scholar.

---

## 17. Estado esperado da tarefa

A tarefa só deve ser considerada concluída quando houver:

- [ ] artigo de 2023 ou posterior;
- [ ] artigo encontrado/verificado no Google Scholar;
- [ ] Autoencoder confirmado;
- [ ] dataset identificado;
- [ ] dataset acessível;
- [ ] código original/reprodução disponível;
- [ ] modelo original executando;
- [ ] inferência original funcionando;
- [ ] arquitetura modificada;
- [ ] justificativa da modificação;
- [ ] modelo modificado treinado;
- [ ] inferência modificada funcionando;
- [ ] comparação quantitativa;
- [ ] comparação qualitativa;
- [ ] relatório técnico;
- [ ] referências verificadas;
- [ ] nenhuma informação inventada.

---

## 18. Instrução principal para a LLM

Você é responsável por conduzir o projeto técnico de forma verificável.

**Primeiro pesquise e selecione o artigo. Depois reproduza o modelo AE. Somente após a reprodução funcionar, modifique a arquitetura e execute o experimento comparativo.**

Em todas as etapas:

- seja técnico;
- registre as decisões;
- preserve a rastreabilidade das fontes;
- não invente informações;
- diferencie resultados do artigo de resultados obtidos no novo experimento;
- mantenha o Autoencoder como arquitetura principal;
- priorize uma implementação que possa efetivamente ser executada e apresentada em sala.

### Resultado final esperado

Produzir uma implementação funcional de:

**AE original → AE modificado → treinamento → inferência → comparação → relatório técnico**

com todas as etapas sustentadas por código, dados, fontes e resultados reproduzíveis.
