# Here go your api methods.

#structures for stocks from iex api
import numpy as np
import pandas as pd
import requests
import ast
#stocks are imported as json files with values

@auth.requires_login()
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
            company_name = r.company_name,
            company_symbol = r.company_symbol,
            company_description = r.company_description,
            user_email = r.user_email,
        )
        stocks.append(stock)
    
    logged_in = auth.user is not None
    return response.json(dict(
        stocks=stocks,
        logged_in=logged_in,
    ))
    
def search_stock():
    sym = request.vars.search_form
    search_list = []
    r = requests.get('https://api.iextrading.com/1.0/stock/'+sym+'/company')
    d = ast.literal_eval(r.text)
    search_stock = []
    t_id = dict(
        user_email = "",
        company_name = d['companyName'],
        company_symbol = d['symbol'],
        company_description = d['description'],
    )
    search_list.append(t_id)
    return response.json(dict(search_list=search_list,
    ))
    
#api call for stocks    
def init_stocks():
    init_stock = []
    sym = "AAPL"
    df_close = pd.DataFrame()
    df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+sym+'/chart/3m')
    #t_id = db.stock.insert(
    #    name = request.vars.name,
    #    price = request.vars.price,
    #    quantity = request.vars.quantity,
    #    
    #    company_name = d['companyName'],
    #    company_symbol = d['symbol'],
    #    company_description = d['description'],
    #)
    #t = db.stock(t_id)
    #db.init
    #return response.json(dict(stock=t))
    
@auth.requires_login()
@auth.requires_signature()
def add_stock():
    sym = request.vars.search_form
    r = requests.get('https://api.iextrading.com/1.0/stock/'+sym+'/company')
    d = ast.literal_eval(r.text)
    t_id = db.stock.insert(
        name = request.vars.name,
        price = request.vars.price,
        quantity = request.vars.quantity,
        
        company_name = d['companyName'],
        company_symbol = d['symbol'],
        company_description = d['description'],
    )
    t = db.stock(t_id)
    return response.json(dict(stock=t))
    
@auth.requires_signature()
def del_stock():
    t_id = db(db.stock.id == request.vars.id).delete()
    return dict()