import pickle

class Credit( object ):
    def __init__( self ):
        self.home_path = '/home/jeffsmedines/repos/datarisk_credit/'
        self.idade_standard = pickle.load( open( self.home_path + 'parameter/idade_standard.pkl', 'rb' ) )
        self.salario_por_dependentes_min_max = pickle.load( open( self.home_path + 
        'parameter/salario_por_dependentes_min_max.pkl', 'rb' ) )
        self.soma_passou_min_max = pickle.load( open( self.home_path + 'parameter/soma_passou_min_max.pkl', 'rb' ) )
        self.util_linhas_inseguras_robust = pickle.load( open( self.home_path + 'parameter/util_linhas_inseguras_robust.pkl', 'rb' ) )
        self.debito_x_salario_robust = pickle.load( open( self.home_path + 'parameter/debito_x_salario_robust.pkl', 'rb' ) )
        self.idade_x_salario_robust = pickle.load( open( self.home_path + 'parameter/idade_x_salario_robust.pkl', 'rb' ) )
        
    def data_cleaning( self, df1 ):
        ### 1.5.1 Salário Mensal
        df1['salario_mensal'].fillna( df1.loc[df1['salario_mensal'] < 300000, 'salario_mensal'].mean(), inplace=True )

        ### 1.5.2 Número de Dependentes
        df1['numero_de_dependentes'].fillna( df1['numero_de_dependentes'].median(), inplace=True )

        ## 1.6 Change Types
        df1['numero_de_dependentes'] = df1['numero_de_dependentes'].astype( int )
        
        return df1
    
    def feature_engineering( self, df2 ):
        # Salário por denpendentes
        df2['salario_por_dependentes'] = df2[['salario_mensal', 'numero_de_dependentes']].apply( lambda x: x['salario_mensal'] 
        if x['numero_de_dependentes'] == 0 else x['salario_mensal'] / x['numero_de_dependentes'], axis=1 )

        # Salário por número de empréstimos abertos
        df2['salario_por_emprestimos'] = df2[['salario_mensal', 'numero_linhas_crdto_aberto']].apply( lambda x: 
        x['salario_mensal'] if x['numero_linhas_crdto_aberto'] == 0 else x['salario_mensal'] /
        x['numero_linhas_crdto_aberto'], axis=1 )

        # Soma do número de vezesque passou de 30, 60 e 90 dias
        df2['soma_passou'] = df2['vezes_passou_de_30_59_dias'] + df2['numero_vezes_passou_90_dias'] + df2['numero_de_vezes_que_passou_60_89_dias']

        # Razão débito vezes o salário
        df2['debito_x_salario'] = df2['razao_debito'] * df2['salario_mensal']

        # util linhas inseguras vezes numero de linhas de crédito aberto
        df2['linhas_credito_inseguras'] = df2['util_linhas_inseguras'] * df2['numero_linhas_crdto_aberto']

        # Idade vezes o salário
        df2['idade_x_salario'] = df2['idade'] * df2['salario_mensal']
        
        return df2
    
    def data_filtering( self, df3 ):
        ## 3.1 Filtering Rows
        # Removing outliers
        df3 = df3.loc[ df3['salario_mensal'] < 300000, : ]
        df3 = df3.loc[ df3['vezes_passou_de_30_59_dias'] < 50, : ]

        # Removing Age = 0
        df3 = df3.loc[df3['idade'] >= 18, :]

        ## 3.2 Filtering Cols

        # High Correlation Variables
        df3 = df3.drop( columns=['vezes_passou_de_30_59_dias', 'numero_vezes_passou_90_dias',
                                 'numero_de_vezes_que_passou_60_89_dias', 'linhas_credito_inseguras'] )
        
        return df3
    
    def data_preparation( self, df5 ):
        
        # ======================== StandardScaler ========================

        # Idade
        df5['idade'] = self.idade_standard.fit_transform( df5[['idade']].values )

        # ======================== MinMaxScaler ========================

        # Salario por Dependentes
        df5['salario_por_dependentes'] = self.salario_por_dependentes_min_max.fit_transform(
        df5[['salario_por_dependentes']].values )

        # Soma Passou
        df5['soma_passou'] = self.soma_passou_min_max.fit_transform( df5[['soma_passou']].values )
        
        # ======================== RobustScaler ========================
        
        # Util Linhas Inseguras
        df5['util_linhas_inseguras'] = self.util_linhas_inseguras_robust.fit_transform( df5[['util_linhas_inseguras']].values)

        # Debito x Salario
        df5['debito_x_salario'] = self.debito_x_salario_robust.fit_transform( df5[['debito_x_salario']].values )

        # Idade x Salario
        df5['idade_x_salario'] = self.idade_x_salario_robust.fit_transform( df5[['idade_x_salario']].values )
        
        cols_selected = [ 'util_linhas_inseguras','idade','salario_por_dependentes',
                          'salario_por_emprestimos','soma_passou','debito_x_salario','idade_x_salario' ]
        
        return df5[ cols_selected ]
    
    def get_prediction( self, model, original_data, test_data ):
        # Prediction
        pred = model.predict( test_data )
        
        # Join Pred into Original Data
        original_data['inadimplente'] = pred
        
        return original_data.to_json( orient='records' )