# Análise dos Resultados 

**Análise da base de dados:**[Base de dados](https://github.com/Tecnologia-em-Banco-de-Dados-PUC-Minas/eixo5_grupo3_20252/blob/be1c1afc1417d63435bbd88baf67802be9cf26ed/projeto/base_dados/credit_risk_dataset.csv.zip)

## 1. Resultados e Discussão
Após o treinamento e teste dos modelos em um conjunto de dados separado, os resultados foram compilados e analisados tanto quantitativamente, por meio de métricas, quanto qualitativamente, por meio de visualizações gráficas.

1.1. Desempenho Geral dos Modelos
O desempenho quantitativo dos modelos é resumido na Tabela 1.

<img width="625" height="250" alt="tabela_metricas" src="https://github.com/user-attachments/assets/184dc3fc-8db6-4844-b0f1-2560b5a35e1f" />


A Figura 1 mostra a Curva ROC plotada para visualizar a capacidade de discriminação geral de cada modelo.
A área sob a curva (AUC) confirma a superioridade do Random Forest.

<img width="697" height="514" alt="image" src="https://github.com/user-attachments/assets/9cea82b7-441b-4fb6-897a-55f43a81f4e7" />


A Figura 2 ilustra a comparação direta das métricas de Acurácia, Precisão, Recall e F1-Score, evidenciando o trade-off entre Precisão e Recall.

<img width="844" height="459" alt="image" src="https://github.com/user-attachments/assets/7c02d008-9ff4-4dec-9ab3-1888b8b3aaf4" />

A análise dos erros é aprofundada na Figura 3, que apresenta as matrizes de confusão de forma visual. É notável a drástica redução de Falsos Positivos (de 1601 para 43) no modelo Random Forest, ao custo de um pequeno aumento nos Falsos Negativos (de 435 para 575).

<img width="878" height="322" alt="image" src="https://github.com/user-attachments/assets/093a936c-8310-495d-9c25-f9f55e651515" />


1.2. Análise de Importância das Variáveis
Para entender os critérios de decisão de cada modelo, foi realizada uma análise da importância das variáveis (Figura 4).
Ambos os modelos concordam que loan_percent_income e loan_grade são os fatores mais críticos.
O gráfico da Regressão Logística detalha quais fatores aumentam (coeficiente positivo) ou diminuem (coeficiente negativo) o risco, enquanto o Random Forest ranqueia as variáveis por seu poder preditivo geral.

<img width="872" height="379" alt="image" src="https://github.com/user-attachments/assets/8693fbbe-89b8-4a11-9fe2-f15a60d9cae0" />
