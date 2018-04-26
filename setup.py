import simplestock
from datetime import datetime
from datetime import timedelta

common = simplestock.StockType.COMMON
preferred = simplestock.StockType.PREFERRED
tea_stock = simplestock.Stock('TEA', common , 0, None, 100)
pop_stock = simplestock.Stock('POP', common, 8, None, 100)
ale_stock = simplestock.Stock('ALE', common, 23, None, 60)
gin_stock = simplestock.Stock('GIN', preferred, 8, 2, 100)
joe_stock = simplestock.Stock('JOE', common, 13, None, 250)

trade_tea_1 = simplestock.Trade(20.5, datetime.now(), tea_stock, 5, simplestock.TransactionType.BUY)
trade_tea_2 = simplestock.Trade(10.2, datetime.now() + timedelta(minutes=-1), tea_stock, 20, simplestock.TransactionType.BUY)
trade_tea_3 = simplestock.Trade(15.6, datetime.now() + timedelta(minutes=-6), tea_stock, 10, simplestock.TransactionType.BUY)
trade_pop_1 = simplestock.Trade(7.29, datetime.now(), pop_stock, 14, simplestock.TransactionType.SELL)
trade_pop_2 = simplestock.Trade(15.29, datetime.now() + timedelta(minutes=-2), pop_stock, 18, simplestock.TransactionType.SELL)
trade_ale = simplestock.Trade(20.24, datetime.now(), ale_stock, 15, simplestock.TransactionType.BUY)
trade_gin = simplestock.Trade(50.67, datetime.now(), gin_stock, 12, simplestock.TransactionType.SELL)
trade_joe = simplestock.Trade(32.57, datetime.now(), joe_stock, 22, simplestock.TransactionType.BUY)

exchange = simplestock.GlobalBeverageCorporationExchange()
exchange.add_stock(tea_stock)
exchange.add_stock(pop_stock)
exchange.add_stock(ale_stock)
exchange.add_stock(gin_stock)
exchange.add_stock(joe_stock)


exchange.record_trade(trade_tea_1)
exchange.record_trade(trade_tea_2)
exchange.record_trade(trade_tea_3)
exchange.record_trade(trade_pop_1)
exchange.record_trade(trade_pop_2)
exchange.record_trade(trade_ale)
exchange.record_trade(trade_gin)
exchange.record_trade(trade_joe)

print("Dividend Yield for TEA stock for price 16.0")
print(exchange.find_stock("TEA").calculate_dividend_yield(16.0))

print("Dividend Yield for POP stock for price 2.5")
print(exchange.find_stock("POP").calculate_dividend_yield(2.5))

print("P/E ratio for POP stock for price 2.5")
print(exchange.find_stock("POP").pe_ratio(2.5))

print("Dividend Yield for GIN stock for price 6.5")
print(exchange.find_stock("GIN").calculate_dividend_yield(6.5))

print("P/E ratio for GIN stock for price 6.5")
print(exchange.find_stock("GIN").pe_ratio(6.5))

print("Volume Weighted Stock price for TEA")
print(exchange.volume_weighted_stock_price("TEA"))

print("Volume Weighted Stock price for POP")
print(exchange.volume_weighted_stock_price("POP"))

print("All Share Price Index")
print(exchange.all_share_index())


