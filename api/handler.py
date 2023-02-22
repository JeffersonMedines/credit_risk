import os
import pickle
import pandas as pd
from flask               import Flask, request, Response
from credit.credit_class import Credit
from xgboost             import XGBClassifier

# Load Model
model = pickle.load( open( 'model/model_credit.pkl', 'rb' ) )

# Initialize API
app = Flask( __name__ )

@app.route( '/credit/predict', methods=['POST'] )

def credit_predict():
    test_json = request.get_json()
    
    if test_json: # There is data
        if isinstance( test_json, dict ): # Unique json
            test_raw = pd.DataFrame( test_json, index=[0] )
        else: # Multiple json
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
        
        # Instantiate Credit Class
        pipeline = Credit()
        
        # Data Cleaning
        df1 = pipeline.data_cleaning( test_raw.copy() )
        
        # Feature Engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # Data Preparation
        df3 = pipeline.data_preparation( df2 )
        
        # Predict
        df_response = pipeline.get_prediction( model, test_raw, df3 )
            
        return df_response
        
    else: # there is no data
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    porti = os.environ.get( 'PORT', 5000 )
    app.run( host='0.0.0.0', port=porti, debug=True )