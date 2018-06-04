# Here go your api methods.

#structures for stocks from iex api
import numpy as np
import pandas as pd
#stocks are imported as json files with values

@auth.requires_signature()
@auth.requires_login()
def get_stocks():
    user_email = request.vars.user_email
    
#api call for stocks    
def init_stocks():
    sym = "AAPL"
    df_close = pd.DataFrame()
    df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+sym+'/chart/3m')
    #df_temp.head(4)
    
    #df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+sym+'/company')
    #dfc_temp.head(4)