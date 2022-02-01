"""
Name: AaronTook
Use:  Uses functions in FinancingDouble.py to render a passed list of stock data over a passed period of time. This module is imported and run by PyStock.py.
"""

from FinancingDouble import *
import sys


StockString = sys.argv[1]
Selected = sys.argv[2]
StockList = StockString.split(">>")

if Selected == "5d":
	graph5DayValue(StockList)
if Selected == "1mo":
	graph1MonthValue(StockList)
if Selected == "6mo":
	graph6MonthValue(StockList)
if Selected == "10y":
	graph10YearValue(StockList)
if Selected == "ytd":
	graphYTDValue(StockList)
if Selected == "max":
	graphMaxValue(StockList)

