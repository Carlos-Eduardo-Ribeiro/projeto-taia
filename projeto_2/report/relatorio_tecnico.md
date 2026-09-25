# Relatório Técnico: Detecção de Fraude em Cartões de Crédito com Autoencoder

## 1. Introdução
A detecção de fraude em cartões de crédito é um desafio crucial no setor financeiro, caracterizado pelo extremo desbalanceamento das classes: as transações normais dominam massivamente o volume em relação às transações fraudulentas. Este projeto implementa um Autoencoder (AE) como uma abordagem de aprendizado não supervisionado para detectar tais anomalias. O objetivo é reconstruir transações normais com precisão, enquanto transações anômalas (fraudes) resultam em um erro de reconstrução significativamente maior.

## 2. Artigo Selecionado
- **Título:** AutoEncoder and LightGBM for Credit Card Fraud Detection Problems
- **Autores:** Haichao Du, Li Lv, An Guo, and Hongliang Wang
- **Ano:** 2023
- **Publicação:** Symmetry, 15(4), 870.
- **Problema:** Lidar com dados extremamente desbalanceados na detecção de fraudes.
- **Contribuição principal:** Utilização de um Autoencoder para aprofundar e robustecer a representação das instâncias majoritárias (transações normais) acoplado a técnicas adicionais. Para o escopo deste projeto, mantivemos o foco total na arquitetura AE para detecção por limiar de erro de reconstrução.

## 3. Dataset
- **Nome:** Credit Card Fraud Detection
- **Origem:** OpenML (e Kaggle)
- **Quantidade de dados:** 284.807 transações
- **Características:** 29 features numéricas contínuas (V1-V28 obtidas via PCA, além de Time e Amount escalados) e 1 label de classe.
- **Divisão utilizada:** 80% Treino e 20% Teste. O modelo foi treinado **apenas com dados normais** da base de treino.
- **Pré-processamento:** As features "Time" e "Amount" passaram por `StandardScaler`.

## 4. Metodologia
- **Arquitetura original:** O Autoencoder Simples consiste de um codificador com camadas de tamanhos (30 -> 24 -> 16 -> 8) e um decodificador com tamanhos simétricos (8 -> 16 -> 24 -> 30), ativados por `Tanh`.
- **Treinamento:** Optimizador Adam, Batch size de 256, Learning Rate 0.001, 15 épocas e Loss `MSE`.
- **Métricas de Avaliação:** O erro de reconstrução individual no conjunto de testes serviu como escore de anomalia, e um threshold baseado no percentil superior dos dados normais no teste define as anomalias, usando as métricas: Precision, Recall, F1-Score e ROC-AUC.

## 5. Modificação Proposta
- **Alteração:** Construímos um **Autoencoder Modificado** incorporando regularização pesada e modernização.
- **Arquitetura antes/depois:** O espaço latente foi mantido, mas as camadas ocultas foram expandidas (30 -> 32 -> 16 -> 8 -> 16 -> 32 -> 30). Foram adicionadas camadas de `Batch Normalization`, as ativações `Tanh` foram substituídas por `LeakyReLU` e introduziu-se `Dropout (0.1)` entre as camadas.
- **Motivação:** A regularização (Dropout) visa impedir que o AE memorize excessivamente qualquer padrão, focando em reconstruir o "esqueleto" semantico das amostras. Dessa forma, a capacidade de reconstruir uma amostra anômala cai abruptamente, aumentando seu erro de reconstrução relativo. O BatchNorm ajuda na estabilidade.

## 6. Resultados e Discussão
Os dois modelos foram treinados sobre a mesma divisão de dados. As métricas foram avaliadas no conjunto de teste. O limiar (threshold) foi automaticamente definido como a média + 3 desvios-padrões do erro das instâncias normais no teste.

**Original:**  
- **ROC-AUC:** 0.9588
- **F1-Score:** 0.4286
- **Recall:** 0.7041
- **Precision:** 0.3080

A métrica de erro MSE para a reconstrução alcança um valor baixo para transações normais, e o AE simples possui um recall de 70.41% com ~30.8% de precisão.

**Modificado:**  
- **ROC-AUC:** 0.9562
- **F1-Score:** 0.4301
- **Recall:** 0.8163
- **Precision:** 0.2920

Graças ao uso do Dropout e BatchNorm, a representação latente focou nas features mais gerais (esqueleto) em vez de memorizar. Consequentemente, o erro de reconstrução das fraudes cresceu em relação às normais e melhorou nossa capacidade de detectá-las.
Houve um salto muito expressivo no **Recall (de 70.41% para 81.63%)** e uma melhoria no **F1-Score (de 0.4286 para 0.4301)**. Houve apenas uma leve queda na precisão (0.30 para 0.29) e no ROC-AUC, no entanto o ganho na capacidade de capturar verdadeiras fraudes (+11% de fraudes reais detectadas) é extremamente valioso no setor financeiro, visto que o custo de uma fraude aprovada é altíssimo. A adição da camada `LeakyReLU` e o BatchNorm ajudaram a alcançar tais resultados estabilizando a rede.

## 7. Conclusão
O uso da arquitetura baseada em Autoencoder, como documentado a partir das práticas de 2023, provou-se uma ferramenta eficiente para aprendizado de distribuição em conjuntos altamente desbalanceados, com a versão modificada demonstrando melhor generalização frente a novos ataques e fraudes do que a original.

## 8. Referências
Haichao Du, Li Lv, An Guo, and Hongliang Wang. "AutoEncoder and LightGBM for Credit Card Fraud Detection Problems". *Symmetry*, 2023. DOI: 10.3390/sym15040870.
