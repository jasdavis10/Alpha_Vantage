#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:56:46 2020

@author: jason
"""


from alpha_vantage.timeseries import TimeSeries

# Your key here
key = '1BK09VNETQVBA25U'

ts = TimeSeries(key)

aapl, meta = ts.get_daily(symbol='AAPL')

#print(aapl['2019-09-12'])





from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Your key here
key = '1BK09VNETQVBA25U'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
# aapl_sma is a dict, aapl_meta_sma also a dict
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')


# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['1. open'].plot()
plt.tight_layout()
plt.grid()
plt.show()











from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt

alpha_vantage_api_key = "1BK09VNETQVBA25U"

def pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name, data_interval = '1min'):
    """
    Pull intraday time series data by stock ticker name.
    Args:
        alpha_vantage_api_key: Str. Alpha Vantage API key.
        ticker_name: Str. Ticker name that we want to pull.
        data_interval: String. Desired data interval for the data. Can be '1min', '5min', '15min', '30min', '60min'.
    Outputs:
        data: Dataframe. Time series data, including open, high, low, close, and datetime values.
        metadata: Dataframe. Metadata associated with the time series.   
    """
    #Generate Alpha Vantage time series object
    ts = TimeSeries(key = alpha_vantage_api_key, output_format = 'pandas')
    #Retrieve the data for the past sixty days (outputsize = full)
    data, meta_data = ts.get_intraday(ticker_name, outputsize = 'full', interval= data_interval)
    data['date_time'] = data.index
    return data, meta_data

def plot_data(df, x_variable, y_variable, title):
    """
    Plot the x- and y- variables against each other, where the variables are columns in
    a pandas dataframe
    Args:
        df: Pandas dataframe, containing x_variable and y_variable columns. 
        x_variable: String. Name of x-variable column
        y_variable: String. Name of y-variable column
        title: String. Desired title name in the plot.
    Outputs:
        Plot in the console. 
    """
    fig, ax = plt.subplots()
    ax.plot_date(df[x_variable], 
                 df[y_variable], marker='', linestyle='-', label=y_variable)
    fig.autofmt_xdate()
    plt.title(title)
    plt.show()

    
#####################################################################################################
#### EXECUTE IN MAIN FUNCTION #######################################################################
ts_data, ts_metadata = pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name = "GOOGL")
#Plot the high prices
plot_data(df = ts_data, 
          x_variable = "date_time", 
          y_variable = "2. high", 
          title ="High Values, Google Stock, 15 Minute Data")
