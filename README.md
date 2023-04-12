![shutterstock_635516519](https://user-images.githubusercontent.com/93053350/231486996-184e050b-0f4e-4387-a95a-37474f106cff.jpg)



# Credit Risk



<h1> Índice </h1>

<h3>

• [Problema de Negócio](https://github.com/JeffersonMedines/credit_risk#mag_right-problema-de-neg%C3%B3cio-)

• [Premissas do Negócio](https://github.com/JeffersonMedines/credit_risk#gear-premissas-do-neg%C3%B3cio-)

• [Planejamento da Solução](https://github.com/JeffersonMedines/credit_risk#computer-planejamento-da-solu%C3%A7%C3%A3o-)

• [Top 3 Insights de Negócio](https://github.com/JeffersonMedines/credit_risk#bar_chart-top-3-insights-de-neg%C3%B3cio)

• [Machine Learning e Métricas de Performance](https://github.com/JeffersonMedines/credit_risk#mechanical_arm-machine-learning-e-m%C3%A9tricas-de-performance-)

• [Resultados Financeiros para o Negócio](https://github.com/JeffersonMedines/credit_risk#chart_with_upwards_trend-resultados-financeiros-para-o-neg%C3%B3cio-)

• [Deploy do Modelo em Produção](https://github.com/JeffersonMedines/credit_risk#hammer_and_wrench-deploy-do-modelo-em-produ%C3%A7%C3%A3o-)

• [Próximos Passos](https://github.com/JeffersonMedines/credit_risk#pushpin-pr%C3%B3ximos-passos-)
 
 </h3>

<h1>:mag_right: Problema de Negócio </h1>

<p> A EasyCredit é uma instituição financeira que busca democratizar o acesso ao crédito e soluções financeiras para pessoas físicas e pequenas e médias empresas. Um dos seus principais produtos é a concessão de empréstimos para seus clientes, assim, foi solicitado o desenvolvimento de um modelo de previsão para determinar quais clientes serão inadimplentes, e quais não serão, a fim de melhorar a tomada de decisão em relação a quais clientes terão o pedido de crédito concedido, para se ter uma maior assertividade. </p>

<h1>:gear: Premissas do Negócio </h1>

<p> Como não é informado qual o valor solicitado de empréstimo, e também não existem dados referentes a quanto a empresa obtém de receita ou lucro para cada empréstimo, para se calcular o impacto financeiro que o modelo irá gerar no negócio, será considerado que o valor médio de solicitação de empréstimo é de R$5000, e que para cada empréstimo honrado é gerado 15% de lucro, ou R$750, e que para cada cliente inadimplente é tido o prejuízo de R$5000. </p>


<h1>:computer: Planejamento da Solução </h1>

<h3> 1.0 Input </h3>
<p> 

1.1 Problema de Negócio: Classificar quais pedidos de crédito serão inadimplentes e quais serão honrados.
    
1.2 Conjunto de Dados: Clientes que solicitaram crédito e as suas features nas colunas. A granularidade dos dados é 1 cliente para cada linha do dataset. </p>
    
<h3> 2.0 Output </h3>

<p> 2.1 Uma nova coluna no dataset com a classificação de inadimplência do cliente.

2.2 Construção de uma API para fazer o deploy do modelo em produção e possibilitar que ele seja acessado de qualquer computador e horário. </p>

<h3> 3.0 Tasks </h3>

<p> 3.1 Entendimento do problema de negócio.

3.2 Descrição dos dados.

3.3 Construir o mindmap de hipóteses.

3.4 Criar as hipóteses e realizar o feature engineering.

3.5 Responder as hipóteses de negócio e realizar a EDA.

3.6 Prepração dos dados.

3.7 Seleção de features.

3.8 Aplicação dos modelos de ML.

3.9 Hyperparameter fine tuning.

3.10 Tradução e interpretação do erro para negócios.

3.11 Construir a classe credit.

3.12 Construir a API.

3.13 Subir o modelo e a API na cloud. </p>

<h3> 4.0 Metodologia </h3>

<p> 4.1 Este projeto será desenvolvido com base no Processo Padrão Inter-Indústrias para Mineração de Dados (CRISP-DM). O intuito desa metodologia é que o cientista passe inicialmente por todos os passos do projeto da forma mais rápida possível. Mas como isso pode ajudar no desenvolvimento do projeto e na agregação de valor para a empresa? Ao passar por todas as etapas do projeto de maneira rápida já é possível identificar qualquer problema que impeça o projeto de ser desenvolvido, reduzindo custos no caso de construir um projeto excelente já na primeira entrega o que demandaria mais tempo e investimento para no final descobrir o problema que impede o desenvolvimento do projeto. Ao desenvolver uma solução inicial rápida, a empresa já está sendo beneficiada financeiramente ainda que pouco nessa primeira versão do projeto em quanto uma solução mais robusta é construída em uma próxima iteração do CRISP-DM. </p>

![crisp dm](https://user-images.githubusercontent.com/93053350/208129563-6f933191-f522-4603-bf98-06b3f0db9937.jpg)


<h1>:bar_chart: Top 3 Insights de Negócio</h1>

<h3> 1. Clientes com número de dependentes maiores, são mais inadimplentes do que clientes com números menores. </h3>

<p> FALSA: Clientes com maiores números de dependentes são menos inadimplentes do que clientes com números menores de dependentes. </p>

![1mais dependentes, mais inacimplente](https://user-images.githubusercontent.com/93053350/231508579-4a2e80d4-0e94-481a-bffb-178add6358e3.png)

<h3> 2. Clientes mais velhos são menos inadimplentes do que clientes mais novos. </h3>

<p> VERDADEIRA: A inadimplência crescre até a idade de 46 anos, e após isso os clientes mais velhos são menos inadimplentes. </p>

![2mais velho, menos inadimplente](https://user-images.githubusercontent.com/93053350/231508937-52e5a285-a795-440f-8ad5-5630968b58d2.png)

<h3> 3. Clientes com maiores números de empréstimos abertos, são mais inadimplentes do que clientes com menos empréstimos abertos. </h3>

<p> FALSO: A inadimplência cresce apenas até 5 empréstimos abertos, após isso diminui conforme os empréstimos aumentam. </p>

![3mais empréstimos, mais inadimplente](https://user-images.githubusercontent.com/93053350/231509253-f0fd2a28-67d2-4262-8dbc-d6497a5e5f2a.png)



<h1>:mechanical_arm: Machine Learning e Métricas de Performance </h1>

<p> Para avaliar o desempenho dos algoritmos de machine learning, foram selecionadas três métricas, precision (das previsões que o modelo fez para clientes não inadimplentes, quantas estão corretas?), recall (de todos os casos de clientes inadimplentes, quantos o modelo conseguiu acertar?) e F1 score (média harmônica das duas métricas anteriores). Durante o projeto a métrica F1 score foi a mais abservada por refletir o desempenho da precision e da recall e o melhor é que se maximize as duas, porém, no momento de tomar as decisões sobre quais algoritmos iriam para a etapa de fine tuning, também eram analisadas a precision e recall individualmente para garantir que elas estejam próximas uma da outra, pois da mesma forma que é importante prever os inadimplentes para reduzir o prejuízo, também é importante prever os não inadimplentes para que a empresa consiga lucrar emprestando para quem irá pagar. Assim, foram selecionados três modelos baseados em árvores para treinar, Random Forest, Decision Tree e XGBoost. (o modelo baseline é feito aleatoriamente para se comparar inicialmente o desempenho dos modelos criados.) </p>

<h3> Single Result </h3>

| Model Name  |  Precision  |  Recall  | F1 Score |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  Random Forest |  0.8704	 |  0.9178 |  0.8935  |
|  XGBoost |  0.8362 |  0.8712 |  0.8533  |
|  Decision Tree |  0.8077 |  0.8427 |  0.8249  |
|  Baseline |  0.5071 |  0.0702 |  0.1234  |

<p> Dos três algoritmos escolhidos, a decision tree ficou bem abaixo do desempenho dos outros dois modelos. A random forest obteve o maior desempenho em quanto o XGBoost ficou um pouco a baixo dela. </p>

<h3> Cross-Validation Result </h3>

| Model Name  |  Precision CV  |  Recall CV  | F1 Score CV |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  Random Forest |  0.8572 +/- 0.0013	 |  0.904 +/- 0.0018 |  0.8799 +/- 0.0005  |
|  XGBoost |  0.8304 +/- 0.0021 |  0.8659 +/- 0.0022 |  0.8478 +/- 0.0016  |
|  Decision Tree |  0.799 +/- 0.0026 |  0.8304 +/- 0.0029 |  0.8144 +/- 0.0018  |
|  Baseline |  0.5071 |  0.0702 |  0.1234  |

<p> Calculando a performance real com o cross validation, a random forest e o xgboost ficaram com um desempenho ainda mais próximo um do outro, assim, os dois modelos foram selecionados para ir a etapa de fine tuning. </p>

<h3> Cross-Validation Result After Fine Tuning </h3>

| Model Name  |  Precision CV  |  Recall CV  |  F1 Score CV  |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  XGBoost Tunned |  0.9117 +/- 0.0058 |  0.9658 +/- 0.0111 |  0.9379 +/- 0.0021 |
|  Random Forest Tunned |  0.8974 +/- 0.0099 |  0.9397 +/- 0.0143 |  0.9180 +/- 0.0221 |
<p> Após o fine tunning o xgboost apresentou um desempenho melhor que a random forest em todas as métricas, e por isso foi o modelo selecionado para colocar em produção. </p>


<h1>:chart_with_upwards_trend: Resultados Financeiros para o Negócio </h1>

<h3> Total Performance </h3>

<p> Levando em conta as premissas de negócio para se calcular o impacto financeiro do modelo, para os quase 40 mil clientes do conjunto de dados de validação, será gerado um retorno financeiro de R$8.960.750 para a empresa. </p>

![resultado financeiro](https://user-images.githubusercontent.com/93053350/231520724-d0b3e94b-f7c0-4aeb-aa77-032db683d9f0.png)

<h1>:hammer_and_wrench: Deploy do Modelo em Produção </h1>

<p> Foi construída a classe do modelo com todos os métodos e transformações utilizados no decorrer do projeto em conjunto com uma API. As duas aplicações foram colocadas em produção na cloud Render e estão acessíveis para requisições de qualquer computador e em qualquer horário. Na imagem a baixo, demonstro uma requisição bem sucedida com o retorno das previsões: </p>

![requisição](https://user-images.githubusercontent.com/93053350/231522117-00001f8e-bbaa-4789-8e91-2e4fa2e59696.png)

<h1>:pushpin: Próximos Passos </h1>

<p> Para próximos ciclos do CRISP-DM, coloco dois pontos para se implementar no projeto:

1. Melhorar a performance da métrica precission para que se iguale a métrica de recall. Isso consequentemente irá aumentar o retorno finaceiro já que a precission nos indica o quanto a empresa está emprestando dinheiro para bons pagadores.

2. A fim de implementar a solução desenvolvida o mais próxima possível do tomador de decisão que irá consumir a solução, proponho desenvolver um script em VBA no Excel, que será integrado a um botão na planilha, que ao clicar no botão, o script irá automaticamente coletar os dados da planilha, fazer a requisição na API, e retornar as previsões como uma nova coluna na própria planilha, facilitando e tornando muito prático o acesso as previsões. </p>
