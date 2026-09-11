# Contexto do Projeto: Rede Neural MLP do Zero com Interface Streamlit

## 1. Objetivo Principal
O objetivo deste projeto é construir uma Rede Neural do tipo **MLP (Multi-Layer Perceptron) puramente em Python (do zero / *from scratch*)**, sem o uso de bibliotecas prontas de Deep Learning (como TensorFlow ou PyTorch) para a estrutura do modelo [cite: 1]. 

O projeto exige o desenvolvimento de uma interface interativa em **Streamlit** onde seja possível configurar, visualizar e controlar todo o processo de treinamento e inferência da rede em tempo real [cite: 1].                       

Crie um estrura de pastas bem organizadas e me de os comendos e locais para a exceulção;

## 2. Especificações Técnicas e Entregáveis

### A. Jupyter Notebook (`.ipynb`)
Você deve documentar todo o processo de pipeline de dados em um notebook, contendo:
* **Extração de Dados**: Carregamento das bases de dados.
* **Pré-processamento e Tratamento**: Aplicação de técnicas de normalização ou padronização (*standardization*), tratamento de *outliers* e adequação das variáveis [cite: 1].
* **Treinamento e Validação Base**: Demonstração da lógica base antes de ir para a interface.

### B. Interface em Streamlit
A interface gráfica deve fornecer o controle total do modelo ao usuário, permitindo:
* **Controle de Arquitetura**: Escolha livre da quantidade de camadas ocultas e número de neurônios por camada [cite: 1].
* **Configuração de Hiperparâmetros**: Ajuste da taxa de aprendizado (*learning rate*), número de épocas (*epochs*), funções de ativação (ex: ReLU, Sigmoid, tanh) [cite: 1].
* **Controle de Execução**: Botões para acionar o treinamento, avançar por épocas (passo a passo) e realizar testes [cite: 1].
* **Visualização Gráfica do Treinamento**: A interface deve mostrar o grafo da rede neural sendo atualizado, permitindo visualizar os neurônios, as conexões (*feed-forward* e *back-propagation*) e o ajuste dos pesos (*weights*) durante as épocas [cite: 1].

## 3. Bases de Dados

Os dados devem ser divididos obrigatoriamente na proporção de **80% para treinamento** e **20% para testes** [cite: 1].

1. **Primeira Etapa (Base Principal)**: Dataset `heart.csv` (Heart Disease) [cite: 1].
2. **Segunda Etapa (Desafio)**: Datasets `diabetic_data.csv` e `IDS_mapping.csv` (Diabetes 130-US Hospitals for Years 1999-2008) [cite: 1].

## 4. Padrão de Resultados (Relatório / Apresentação)
Conforme a imagem de referência fornecida, ao final do treinamento, o sistema/projeto deve reportar de forma clara as **informações gerais do melhor modelo**, contendo a seguinte estrutura:

* **Nome do Autor/Equipe** e **Acurácia (Accuracy)** (Ex: *0.833 : Carlos Eduardo*)
* **accuracy**: Valor final da acurácia alcançada no teste (ex: 0.833).
* **learning rate**: Taxa de aprendizado utilizada (ex: 0.005).
* **activation**: Função de ativação utilizada (ex: relu).
* **architecture**: Arquitetura das camadas definida (ex: 13 | 8 | 5 | 1).
* **pre-processing**: O método utilizado para tratamento dos dados (ex: standardize).
* **comentários**: Um breve relato técnico sobre o treinamento. (Ex: "MLP codificada do zero como grafo, com feed-forward e back-propagation manuais. Redes maiores chegaram a 100% no treino mas caíam no teste por overfitting; a arquitetura enxuta generalizou melhor").
* **Grafo dos Pesos Finais**: Uma visualização clara do estado final dos pesos da rede neural após o fim do treinamento.
