"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 1/7/2023
	Project name: PyStock
	File name: PystockGraphingForSubprocess.py
	File description: When passed arguments via subprocess from PyStock.py, graph the passed stocks in a seperate instance so that PyStock.py is still interactive.
"""

from FinancingDouble import *
import sys

""" Parse the passed arguments into a useable format """
StockString = sys.argv[1]
Selected = sys.argv[2]
StockList = StockString.split(">>")

""" Graph based on length of time for the graph, using functions from FinancingDouble.py """
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
