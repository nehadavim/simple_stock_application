from enum import Enum
from datetime import datetime
from datetime import timedelta
import operator
from functools import reduce


class TransactionType(Enum):
    BUY = 1
    SELL = 2


class StockType(Enum):
    PREFERRED = 1
    COMMON = 2


class Stock:
    def __init__(self, symbol: str, stock_type: StockType, last_dividend: float, fixed_dividend: float, par_value: int):
        self.symbol = symbol
        self.stock_type = stock_type
        if last_dividend == None or last_dividend < 0.0:
            raise ValueError("Last Dividend cannot be negative")
        if stock_type == StockType.PREFERRED and (fixed_dividend == None or fixed_dividend < 0.0):
            raise ValueError("Fixed Dividend cannot be negative")
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value

    def calculate_dividend_yield(self, price: float) -> float:
        if price <= 0.0:
            raise ValueError("Price should be greater than 0")
        if self.stock_type == StockType.COMMON:
            return self.last_dividend / price
        else:
            return self.fixed_dividend * self.par_value / price

    def pe_ratio(self, price) -> float:
        if price <= 0.0:
            raise ValueError("Price should be greater than 0")
        if self.last_dividend <= 0:
            raise ValueError("P/E ration cannot be calculated as dividend is not declared")
        return price / self.last_dividend


class Trade:

    def __init__(self, price: float, time: datetime, stock: Stock, quantity: int, transaction_type: TransactionType):
        self.price = price
        self.execution_time = time
        self.stock = stock
        self.quantity = quantity
        self.transaction_type = transaction_type

    def tostring(self) -> str:
        return "with price " + self.price.__str__() + ", execution time " + self.execution_time.__str__() \
               + ", stock " + self.stock.symbol.__str__() + ", quantity " + self.quantity.__str__() \
               + ", transaction type " + self.transaction_type.__str__()


class GlobalBeverageCorporationExchange():
    stocks = {}
    trades = []

    def add_stock(self, stock: Stock):
        self.stocks[stock.symbol] = stock

    def find_stock(self, stock_symbol) -> Stock:
        return self.stocks.get(stock_symbol)

    def record_trade(self, trade: Trade):
        print("Recording trade " + trade.tostring())
        self.trades.append(trade)

    def volume_weighted_stock_price(self, stock_symbol: str):
        required_trades = [trade for trade in self.trades if
                           trade.execution_time >= datetime.now() - timedelta(minutes=5)
                           and trade.stock.symbol == stock_symbol]
        if len(required_trades) > 0:
            return self.calculate_volume_weighted_stock_price(required_trades)
        else:
            return ValueError("Stock is not traded on exchange for last 5 minutes")

    def calculate_volume_weighted_stock_price(self, trades) -> float:
        sum_price_quantity = 0
        sum_quantity = 0
        for trade in trades:
            sum_price_quantity = sum_price_quantity + (trade.quantity * trade.price)
            sum_quantity = sum_quantity + trade.quantity
        return sum_price_quantity / sum_quantity

    def all_share_index(self):
        volume_weighted_stock_prices: float = []
        for stock in self.stocks.values():
            stock_trades = [trade for trade in self.trades if trade.stock.symbol == stock.symbol]
            volume_weighted_stock_prices.append(self.calculate_volume_weighted_stock_price(stock_trades))
        power = 1.0 / len(volume_weighted_stock_prices)
        return reduce(operator.mul, volume_weighted_stock_prices) ** power
