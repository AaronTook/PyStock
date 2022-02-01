# PyStock
A Stock Market GUI made in Python

PyStock is a simple GUI made with the Pygame module. Pystock uses the YFinance module to request the stock data and uses matplotlib.pyplot to render the data. This project contains four .py files. Financing.py and FinancingDouble.py include functions for use in PystockGraphingForSubprocess.py. This file, as its name implies, runs via the subprocess.popen function so that it runs independent of the GUI and allows the GUI to continue after the pyplot is closed. To run the project, simply execute PyStock.py.

Project appearance:
The GUI measures 1000 pixels wide and 700 pixels high. 
In the center from top to bottom are:
1. PyStock Logo.
2. The time selector. This is a series of six clickable buttons that set the current time period for which your plot will be shown. The periods are 5 day, 1 month, 6 month, 10 years, year-to-date (YTD), and max.
3. The search bar. Typing allows you to enter tickers which can be used to add companies to the plot. As a note, if you type a ticker that does not exist, it will still be accepted by the program because I have not made a ticker validation method. Directly next to this is a magnifying glass icon, which when clicked (or when the user presses the enter/return key) launches the plot. All tickers selected (they will be shown either in the search bar or on the right side) will be entered into the plot. The farthest right button in the search bar is the "add and continue" button which looks like an addition symbol and two graphs. This adds the currently entered ticker to the plotlist, but does not launch the plot (this allows you to plot multiple stocks next to each other).

On the left, it displays six popular or well-known companies each of which, when clicked, sets the current search ticker to the company's ticker.
On the right are up to two things. In the top corner, there is data on the Dow Jones and the NASDAQ from the day prior. If the multiple tickers are being plotted simultaneously, a box will also appear showing the tickers that have already been entered into the plot.

I hope you enjoy and feel free to contact me with any ideas you have for improvements to the project! 
