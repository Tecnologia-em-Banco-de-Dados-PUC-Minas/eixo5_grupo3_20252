## Conclusão do Projeto

Este projeto desenvolveu e comparou modelos de machine learning para previsão de risco de crédito, com resultados que demonstram a superioridade do **Random Forest (RF)** sobre a **Regressão Logística (RL)**.

### Principais Resultados

O modelo Random Forest demonstrou ser significativamente superior à Regressão Logística para a previsão de risco de crédito, tornando-se a escolha mais adequada para implementação prática:

- **Superioridade em Precisão**: O RF alcançou uma Precisão de **97,3%** na identificação de inadimplentes, enquanto a RL atingiu apenas **51,5%**.

- **Mitigação de Risco de Negócio**: A alta precisão resultou em uma drástica redução nos Falsos Positivos:
  - Random Forest: apenas **43 falsos positivos**
  - Regressão Logística: **1.601 falsos positivos**
  
  Isso significa que o RF é muito mais confiável ao negar crédito, minimizando a perda de clientes que seriam bons pagadores.

- **Fatores Chave**: Ambos os modelos concordaram que os fatores mais críticos para a inadimplência são:
  - Proporção do empréstimo em relação à renda (`loan_percent_income`)
  - Classificação de risco (`loan_grade`)

> O Random Forest oferece um equilíbrio de desempenho robusto e confiável, crucial para a mitigação de riscos financeiros.

## Otimizações Futuras e Próximos Passos

Para elevar a robustez e o valor de negócio do modelo, os próximos passos recomendados são:

### 1. Otimização de Hiperparâmetros

Utilizar Grid Search ou Random Search para refinar os parâmetros do Random Forest, visando otimizar o trade-off entre Precisão e Recall:
- Número de árvores
- Profundidade máxima
- Critérios de divisão

### 2. Ajuste do Limiar de Classificação

Analisar a curva Precisão-Recall para encontrar um ponto de corte ideal que maximize o ganho financeiro, priorizando ainda mais a minimização de Falsos Positivos em vez de usar o limiar padrão (0.5).

### 3. Interpretabilidade Aprofundada (SHAP)

Implementar técnicas como SHAP Values para explicar as decisões de classificação do Random Forest para cada cliente individual, aumentando a transparência e a confiança no modelo.

### 4. Exploração de Ensembles Avançados

Testar modelos de Gradient Boosting que podem potencialmente superar o Random Forest em performance:
- XGBoost
- LightGBM
- CatBoost
