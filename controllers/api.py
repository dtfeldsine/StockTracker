# Here go your api methods.

#structures for stocks from iex api
import numpy as np
import pandas as pd
import requests
import ast
from pandas_datareader import data as web
from datetime import datetime as dt
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
            day_open = r.day_open,
            day_high = r.day_high,
            day_low = r.day_low,
            day_close = r.day_close,
            day_volume = r.day_volume,
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
    
    start = dt(2018, 1, 1)
    end = dt.now()
    df = web.DataReader(
        sym,
        'iex',
        start,
        end
    )
    
    day_open_read = df.iloc[-1, 0]
    day_high_read = df.iloc[-1, 1]
    day_low_read = df.iloc[-1, 2]
    day_close_read = df.iloc[-1, 3]
    day_volume_read = int(df.iloc[-1, 4])
    
    r = requests.get('https://api.iextrading.com/1.0/stock/'+sym+'/company')
    d = ast.literal_eval(r.text)
    search_stock = []
    t_id = dict(
        user_email = "",
        company_name = d['companyName'],
        company_symbol = d['symbol'],
        company_description = d['description'],
        day_open = day_open_read,
        day_high = day_high_read,
        day_low = day_low_read,
        day_close = day_close_read,
        day_volume = day_volume_read,
    )
    search_list.append(t_id)
    return response.json(dict(search_list=search_list,
    ))
    
#api call for stocks    
def init_stocks():
    init_stock = []
    df_close = pd.DataFrame()
    
    start = dt(2018, 1, 1)
    end = dt.now()
    dfappl = web.DataReader(
        'AAPL',
        'iex',
        start,
        end
    )
    dfgoogl = web.DataReader(
        'GOOGL',
        'iex',
        start,
        end
    )
    dfamzn = web.DataReader(
        'AMZN',
        'iex',
        start,
        end
    )
    dftsla = web.DataReader(
        'TSLA',
        'iex',
        start,
        end
    )
    dfamd = web.DataReader(
        'AMD',
        'iex',
        start,
        end
    )
    
    day_open_read_appl = dfappl.iloc[-1, 0]
    day_high_read_appl = dfappl.iloc[-1, 1]
    day_low_read_appl = dfappl.iloc[-1, 2]
    day_close_read_appl = dfappl.iloc[-1, 3]
    day_volume_read_appl = int(dfappl.iloc[-1, 4])
    
    day_open_read_googl = dfgoogl.iloc[-1, 0]
    day_high_read_googl = dfgoogl.iloc[-1, 1]
    day_low_read_googl = dfgoogl.iloc[-1, 2]
    day_close_read_googl = dfgoogl.iloc[-1, 3]
    day_volume_read_googl = int(dfgoogl.iloc[-1, 4])
    
    day_open_read_amzn = dfamzn.iloc[-1, 0]
    day_high_read_amzn = dfamzn.iloc[-1, 1]
    day_low_read_amzn = dfamzn.iloc[-1, 2]
    day_close_read_amzn = dfamzn.iloc[-1, 3]
    day_volume_read_amzn = int(dfamzn.iloc[-1, 4])
    
    day_open_read_tsla = dftsla.iloc[-1, 0]
    day_high_read_tsla = dftsla.iloc[-1, 1]
    day_low_read_tsla = dftsla.iloc[-1, 2]
    day_close_read_tsla = dftsla.iloc[-1, 3]
    day_volume_read_tsla = int(dftsla.iloc[-1, 4])
    
    day_open_read_amd = dfamd.iloc[-1, 0]
    day_high_read_amd = dfamd.iloc[-1, 1]
    day_low_read_amd = dfamd.iloc[-1, 2]
    day_close_read_amd = dfamd.iloc[-1, 3]
    day_volume_read_amd = int(dfamd.iloc[-1, 4])
    
    r_aapl = requests.get('https://api.iextrading.com/1.0/stock/aapl/company')
    d_aapl = ast.literal_eval(r_aapl.text)
    r_googl = requests.get('https://api.iextrading.com/1.0/stock/googl/company')
    d_googl = ast.literal_eval(r_googl.text)
    r_amzn = requests.get('https://api.iextrading.com/1.0/stock/amzn/company')
    d_amzn = ast.literal_eval(r_amzn.text)
    r_tsla = requests.get('https://api.iextrading.com/1.0/stock/tsla/company')
    d_tsla = ast.literal_eval(r_tsla.text)
    r_amd = requests.get('https://api.iextrading.com/1.0/stock/amd/company')
    d_amd = ast.literal_eval(r_amd.text)
    
    t_id = dict(
        user_email = "",
        company_name = d_aapl['companyName'],
        company_symbol = d_aapl['symbol'],
        company_description = d_aapl['description'],
        day_open = day_open_read_appl,
        day_high = day_high_read_appl,
        day_low = day_low_read_appl,
        day_close = day_close_read_appl,
        day_volume = day_volume_read_appl,
    )
    init_stock.append(t_id)
    t_id = dict(
        user_email = "",
        company_name = d_googl['companyName'],
        company_symbol = d_googl['symbol'],
        company_description = d_googl['description'],
        day_open = day_open_read_googl,
        day_high = day_high_read_googl,
        day_low = day_low_read_googl,
        day_close = day_close_read_googl,
        day_volume = day_volume_read_googl,
    )
    init_stock.append(t_id)
    t_id = dict(
        user_email = "",
        company_name = d_amzn['companyName'],
        company_symbol = d_amzn['symbol'],
        company_description = d_amzn['description'],
        day_open = day_open_read_amzn,
        day_high = day_high_read_amzn,
        day_low = day_low_read_amzn,
        day_close = day_close_read_amzn,
        day_volume = day_volume_read_amzn,
    )
    init_stock.append(t_id)
    t_id = dict(
        user_email = "",
        company_name = d_tsla['companyName'],
        company_symbol = d_tsla['symbol'],
        company_description = d_tsla['description'],
        day_open = day_open_read_tsla,
        day_high = day_high_read_tsla,
        day_low = day_low_read_tsla,
        day_close = day_close_read_tsla,
        day_volume = day_volume_read_tsla,
    )
    init_stock.append(t_id)
    t_id = dict(
        user_email = "",
        company_name = d_amd['companyName'],
        company_symbol = d_amd['symbol'],
        company_description = d_amd['description'],
        day_open = day_open_read_amd,
        day_high = day_high_read_amd,
        day_low = day_low_read_amd,
        day_close = day_close_read_amd,
        day_volume = day_volume_read_amd,
    )
    init_stock.append(t_id)
    #t = db.stock(t_id)
    #db.init
    return response.json(dict(init_stock=init_stock))
    
@auth.requires_login()
@auth.requires_signature()
def add_stock():

    sym = request.vars.search_form
    start = dt(2017, 1, 1)
    end = dt.now()
    df = web.DataReader(
        sym,
        'iex',
        start,
        end
    )
    
    day_open_read = df.iloc[-1, 0]
    day_high_read = df.iloc[-1, 1]
    day_low_read = df.iloc[-1, 2]
    day_close_read = df.iloc[-1, 3]
    day_volume_read = df.iloc[-1, 4]
    
    #personal_open_read = str(day_open_read * quantity)
    #personal_high_read = str(day_open_read * quantity)
    #personal_low_read = str(day_open_read * quantity)
    #personal_close_read = str(day_open_read * quantity)

    
    #quantity = request.vars.quantity_form
    r = requests.get('https://api.iextrading.com/1.0/stock/'+sym+'/company')
    d = ast.literal_eval(r.text)
    t_id = db.stock.insert(
        name = request.vars.name,
        price = request.vars.price,
        quantity = request.vars.quantity,
        
        day_open = day_open_read,
        day_high = day_high_read,
        day_low = day_low_read,
        day_close = day_close_read,
        day_volume = day_volume_read,
        
        #personal_open = personal_open_read
        #personal_high = personal_high_read
        #personal_low = personal_low_read
        #personal_close = personal_close_read
        
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