Super Simple Stocks

This is a simple application to represent a stock exchange. The exchange has following stocks:

1. TEA
2. POP
3. ALE
4. GIN
5. JOE

Each stock is either a Common stock or Preferred stock. Based on the type of stock its Dividend yield is calculated

The requirement is to calculate the following:

1. For a given stock
    i. Given price as input calculate the dividend yield
    ii. Given price as input calculate the P/E ratio
    iii. Record a trade with timestamp, quantity, buy or sell indicator and a price
    iv. Calculate volume weighted stock price based on trades in past 5 minutes

2. Calcuate All Share index for this exchange

Solution:

The code is structured into three main classes along with some utility classes
1. Trade
2. Stock
3. GlobalBeverageCorporationExchange

Main module is simplestock.py and setup.py is used to setup test data. It also prints out the results for few stocks.