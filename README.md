![insurance-producer_16](https://user-images.githubusercontent.com/93053350/208117801-629cf869-7d39-461d-b6e9-e41d12e59504.jpg)


# Credit Risk



<h1> Índice </h1>

<h3>

• [Problemas de Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#mag_right-problemas-de-neg%C3%B3cio-)

• [Premissas do Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#gear-premissas-do-neg%C3%B3cio-)

• [Planejamento da Solução](https://github.com/JeffersonMedines/health_insurance_cross_sell#computer-planejamento-da-solu%C3%A7%C3%A3o-)

• [Top 3 Insights de Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#bar_chart-top-3-insights-de-neg%C3%B3cio)

• [Machine Learning e Métricas de Performance](https://github.com/JeffersonMedines/health_insurance_cross_sell#mechanical_arm-machine-learning-e-m%C3%A9tricas-de-performance-)

• [Resultados Financeiros para o Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#chart_with_upwards_trend-resultados-financeiros-para-o-neg%C3%B3cio-)

• [Deploy do Modelo em Produção](https://github.com/JeffersonMedines/health_insurance_cross_sell#hammer_and_wrench-deploy-do-modelo-em-produ%C3%A7%C3%A3o-)

• [Próximos Passos](https://github.com/JeffersonMedines/health_insurance_cross_sell#pushpin-pr%C3%B3ximos-passos-)
 
 </h3>

<h1>:mag_right: Problema de Negócio </h1>

<p>  </p>

<h1>:gear: Premissas do Negócio </h1>

<p>  </p>


<h1>:computer: Planejamento da Solução </h1>

<p>  </p>

![crisp dm](https://user-images.githubusercontent.com/93053350/208129563-6f933191-f522-4603-bf98-06b3f0db9937.jpg)


<h1>:bar_chart: Top 3 Insights de Negócio</h1>

<h3>  </p>

<h1>:mechanical_arm: Machine Learning e Métricas de Performance </h1>

<p>  </p>

<h3> Single Result </h3>

| Model Name  |  Precision@K  |  Recall@K  |
| ------------------- | ------------------- | ------------------- |
|  XGBoost |  0.3296 |  0.7003 |
|  Random Forest |  0.3070	 |  0.6524 |
|  KNN |  0.2937 |  0.6241 |
|  Logistic Regression |  0.2888 |  0.6136 |
|  Baseline |  0.1258 |  0.2674 |

<p>  </p>

<h3> Cross-Validation Result </h3>

| Model Name  |  Precision@K CV  |  Recall@K CV  |
| ------------------- | ------------------- | ------------------- |
| XGBoost | 0.3106 +/- 0.004 | 0.8327 +/- 0.0059 |
| Random Forest | 0.3082 +/- 0.0341 | 0.8261 +/- 0.087 |
| KNN | 0.2911 +/- 0.0347 | 0.7801 +/- 0.0889 |
| Logistic Regression | 0.2761 +/- 0.0021 | 0.7402 +/- 0.0076 |
| Baseline | 0.1258 | 0.2674 |

<p>  </p>

<h3> Cross-Validation Result After Fine Tuning </h3>

| Model Name  |  Precision@K CV  |  Recall@K CV  |
| ------------------- | ------------------- | ------------------- |
|  XGBoost Tunned |  0.3117 +/- 0.0058 |  0.8358 +/- 0.0111 |

<p>  </p>


<h1>:chart_with_upwards_trend: Resultados Financeiros para o Negócio </h1>

<h3> Total Performance </h3>

<p>  </p>


<h1>:hammer_and_wrench: Deploy do Modelo em Produção </h1>

<p>   </p>

<p>  </p>


<h1>:pushpin: Próximos Passos </h1>

<p>  </p>
