"""
Name: AaronTook
Use:  Defines functions and variables for use in Pystock.py.
"""

import json,os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

Dow_Jones = 'DJI'
NASDAQ = 'NDX'
SP_500 = 'SPX'
GO = 'GOOG'
AM = 'AMZN'
PF = 'PFE'

def graph1DayValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="1d")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (1 day)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()

def graph5DayValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="5d")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (5 days)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()

def graph1MonthValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="1mo")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (1 month)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()

def graph3MonthValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="3mo")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (3 months)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graph6MonthValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="6mo")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (6 months)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graph1YearValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="1y")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (1 year)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graph2YearValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="2y")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (2 year)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graph5YearValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="5y")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (5 year)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graph10YearValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="10y")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (10 year)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graphYTDValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="ytd")
	plt.figure(figsize=(12,5))
	plt.title(f'Price of {StockName} (ytd)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()
	
def graphMaxValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="max")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (max)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()

def graphDailyValue(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="5d")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	plt.title(f'Price of {StockName} (max)')
	plt.plot(history.Open)
	plt.xlabel('Date')
	plt.legend(['Price ($)'])
	plt.show()

def getDowJonesPic():
	yf_ticker = yf.Ticker(Dow_Jones.upper())
	history = yf_ticker.history(period="max")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(2,1))
	plt.plot(history.Open)
	plt.savefig("PYPLOTED.png")
	
def getNASDAQPic():
	yf_ticker = yf.Ticker(NASDAQ.upper())
	history = yf_ticker.history(period="max")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(2,1))
	plt.plot(history.Open)
	plt.savefig("PYPLOTED2.png")

def getSP500Pic():
	yf_ticker = yf.Ticker(SP_500.upper())
	history = yf_ticker.history(period="max")
	plt.figure("PyStock Chart",edgecolor="black",figsize=(2,1))
	plt.plot(history.Open)
	plt.savefig("PYPLOTED3.png")
def DELETEALL_pics():
	os.remove("PYPLOTED1.png")
	os.remove("PYPLOTED2.png")
	os.remove("PYPLOTED3.png")

def getDowJonesDay():
	yf_ticker = yf.Ticker(Dow_Jones.upper())
	history = yf_ticker.history(period="5d")
	Change,Close = float(history.Close[-1]-history.Close[-2]),history.Close[-1]
	Percent = round((Change/Close)*100,3)
	return Change,Close,Percent

def getNASDAQDay():
	yf_ticker = yf.Ticker(NASDAQ.upper())
	history = yf_ticker.history(period="5d")
	Change,Close = float(history.Close[-1]-history.Close[-2]),history.Close[-1]
	Percent = round((Change/Close)*100,3)
	return Change,Close,Percent

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w

def graphDailyChange(StockName):
	yf_ticker = yf.Ticker(StockName.upper())
	history = yf_ticker.history(period="max")
	datevals = pd.to_datetime(history.index[1:].values)
	oldvals = history.Close[:-1].values
	newvals = history.Close[1:].values
	percent_change = (newvals-oldvals)*100/oldvals
	plt.figure(figsize=(12,5))
	plt.title(f'Daily change of {StockName}')
	plt.plot(datevals, percent_change)
	plt.xlabel('Date')
	plt.ylabel('Daily Change (%)')
	plt.show()

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return round(todays_data['Close'][0],2)

def get_business_summary(symbol):
	ticker = yf.Ticker(symbol)
	info = ticker.info
	return info["longBusinessSummary"]
