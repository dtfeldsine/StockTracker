# Here go your api methods.

#structures for stocks from iex api
import numpy as np
import pandas as pd
#stocks are imported as json files with values


def get_stocks():
    rows = db().select(db.stock.ALL)
    
    stocks = []
    for i, r in enumerate(rows):
        stock = dict(
            id = r.id,
            name = r.name,
            price = r.price,
            quantity = r.quantity,
            favorite = r.favorite,
            user_email = r.user_email,
        )
        stocks.append(stock)
    
    logged_in = auth.user is not None
    return response.json(dict(
        stocks=stocks,
        logged_in=logged_in,
    ))
    
#api call for stocks    
def init_stocks():
    sym = "AAPL"
    df_close = pd.DataFrame()
    df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+sym+'/chart/3m')
    #df_temp.head(4)
    
    #df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+sym+'/company')
    #dfc_temp.head(4)
    
@auth.requires_login()
@auth.requires_signature()
def add_stock():
    t_id = db.stock.insert(
        name = request.vars.name,
        price = request.vars.price,
        quantity = request.vars.quantity,
    )
    t = db.stock(t_id)
    return response.json(dict(stock=t))
    
@auth.requires_signature()
def del_stock():
    t_id = db(db.stock.id == request.vars.id).delete()
    return dict()