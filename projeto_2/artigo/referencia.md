# Referência do Artigo

- **Título:** AutoEncoder and LightGBM for Credit Card Fraud Detection Problems
- **Autores:** Haichao Du, Li Lv, An Guo, and Hongliang Wang
- **Ano:** 2023
- **Periódico/Conferência:** Symmetry
- **DOI:** 10.3390/sym15040870
- **Problema abordado:** Detecção de fraude em cartões de crédito utilizando dados desbalanceados.
- **Tipo de Autoencoder:** Autoencoder Simples (Denso) para extração/reconstrução de features.
- **Dataset:** Credit Card Fraud Detection Dataset.
- **Métricas:** Precision, Recall, F1-score, Accuracy.
- **Disponibilidade do código:** O artigo não possui um repositório oficial no GitHub com o código fonte, contudo, a arquitetura de Autoencoder descrita no artigo para detecção de anomalias é reproduzível e pode ser facilmente implementada em PyTorch.
- **Disponibilidade do dataset:** Público (disponível no Kaggle e OpenML).
- **Dificuldade estimada de reprodução:** Baixa, pois arquiteturas de AE aplicadas a dados tabulares como este dataset são diretas de se implementar.
- **Possibilidade de modificação arquitetural:** Alta, é possível variar o número de camadas ocultas, introduzir Dropout, alterar a função de ativação, ou transformar o AE num Variational Autoencoder (VAE) para comparar os resultados.
