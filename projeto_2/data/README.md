# Dataset

O dataset utilizado neste projeto é o **Credit Card Fraud Detection**.
Ele contém transações feitas por cartões de crédito em setembro de 2013 por portadores de cartões europeus.
Este conjunto de dados apresenta transações que ocorreram em dois dias, onde temos 492 fraudes em 284.807 transações. O dataset é altamente desbalanceado, sendo as fraudes 0,172% de todas as transações.

Ele contém apenas variáveis de entrada numéricas que são o resultado de uma transformação PCA (V1, V2, ... V28). As únicas features que não foram transformadas com PCA são 'Time' e 'Amount'. 

**Como obter:**
O dataset foi extraído diretamente via OpenML e salvo no formato CSV dentro da pasta `raw/`.
Ao rodar os scripts, o arquivo `data/raw/creditcard.csv` será carregado nativamente.
Nenhum download adicional é necessário.
