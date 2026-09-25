# Projeto 2 - Autoencoder para Detecção de Fraude

## 1. Descrição
Esta pasta contém a entrega do Projeto 2 para a disciplina **Tópicos em IA — AI4Good**.
O objetivo é reproduzir a detecção de anomalias com um Autoencoder (AE) em uma base de dados pública e comparar o desempenho do modelo original modificado. O caso de uso selecionado é a **Detecção de Fraude em Cartões de Crédito** (Credit Card Fraud Detection).

## 2. Estrutura do Projeto
- `artigo/`: Referência do artigo científico base escolhido de 2023.
- `data/`: Contém a documentação da base de dados utilizada.
- `src/`: Códigos-fonte.
  - `dataset.py`: Função para carregar e formatar os dados.
  - `train_evaluate.py`: Script unificado de treinamento e avaliação.
  - `modelo_original/`: Arquitetura do Autoencoder Base.
  - `modelo_modificado/`: Arquitetura do Autoencoder Modificado (melhorado com Dropout, LeakyReLU e Batch Normalization).
- `results/`: Resultados dos testes e gráficos (original e modificado).
- `report/`: Relatório Técnico em formato Markdown.

## 3. Como executar
O projeto faz uso de pacotes comuns de Deep Learning e Data Science.
1. Instale as dependências: `pip install torch torchvision scikit-learn pandas matplotlib`
2. Navegue até a pasta `src`: `cd projeto_2/src`
3. Execute o treinamento do modelo original:
   ```bash
   python train_evaluate.py --model original
   ```
4. Execute o treinamento do modelo modificado:
   ```bash
   python train_evaluate.py --model modified
   ```

Os resultados (curvas de loss, distribuições de erro de reconstrução, métricas) estarão na pasta `results/`.
