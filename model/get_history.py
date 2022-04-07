import yfinance as yf
import pandas as pd
import json
from dateutil import parser


def get_history(request_in):
    print("Received {}".format(request_in))
    request_dict = request_in

    request_dict['start'] = parser.parse(request_dict['start'])
    request_dict['end'] = parser.parse(request_dict['end'])

    ticker = yf.Ticker(request_dict['ticker'])
    ticker_price = ticker.history(start=request_dict['start'], end=request_dict['end'],
                                  interval=request_dict['interval'])

    try:
        ticker_price = ticker_price.drop(columns=['Dividends', 'Stock Splits'])
        data = ticker_price.to_json(orient="table", date_format="iso")
        return {"data": data, "code": 200}
    except:
        return {"data": None, "code": 404}
