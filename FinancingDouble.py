"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 1/7/2023
	Project name: PyStock
	File name: FinancingDouble.py
	File description: Utility functions for use in PyStock.py (via subprocess use in PystockGraphingForSubprocess.py) to graph multiple tickers over time.
"""

import json,os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


def graph1DayValue(StockList):
	""" Graph the value of the tickers for the most recent day's data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (1 day)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="1d")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph5DayValue(StockList):
	""" Graph the value of the tickers for the past five days' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (5 days)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="5d")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph1MonthValue(StockList):
	""" Graph the value of the tickers for the most recent month's data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (1 month)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="1mo")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph3MonthValue(StockList):
	""" Graph the value of the tickers for the past three months' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (3 months)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="3mo")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph6MonthValue(StockList):
	""" Graph the value of the tickers for the past six months' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (6 months)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="6mo")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph1YearValue(StockList):
	""" Graph the value of the tickers for the most recent year's data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (1 year)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="1y")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph2YearValue(StockList):
	""" Graph the value of the tickers for the past two years' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (2 years)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="2y")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph5YearValue(StockList):
	""" Graph the value of the tickers for the past five years' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (5 years)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="5y")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graph10YearValue(StockList):
	""" Graph the value of the tickers for the past ten years' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (10 years)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="10y")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graphYTDValue(StockList):
	""" Graph the value of the tickers for the year to date data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (YTD)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="ytd")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graphMaxValue(StockList):
	""" Graph the value of the tickers for the maximum range of data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (max)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="max")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()

def graphDailyValue(StockList):
	""" Graph the value of the tickers for the past five days' data '"""
	plt.figure("PyStock Chart",edgecolor="black",figsize=(12,5))
	nameOfChart = ", ".join(StockList)
	plt.title(f'Price of {nameOfChart} (5 day)')
	colors = ['r','g','k','y','b','c','m']
	legendList = []
	for i in range(len(StockList)):
		StockName = StockList[i]
		yf_ticker = yf.Ticker(StockName.upper())
		history = yf_ticker.history(period="5d")
		plt.plot(history.Open, color=colors[i%7])
		legendList.append(f"Price ($) {StockName}")
	plt.xlabel('Date')
	plt.legend(legendList)
	plt.show()
