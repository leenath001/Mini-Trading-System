## Class structure represents creation -> completion lifecycle of order
#  Order read in from FIX_parser.py

from enum import Enum, auto

class OrderState(Enum):
    NEW = auto()
    ACKED = auto()
    FILLED = auto()
    CANCELLED = auto()
    REJECTED = auto()

class Order():
    def __init__(self, symbol, qty, side):
        self.state = OrderState.NEW
        self.symbol = symbol
        self.qty = qty
        self.side = side

    def transition(self, new_state):
        allowed = {
            OrderState.NEW: {OrderState.ACKED, OrderState.REJECTED},
            OrderState.ACKED: {OrderState.FILLED, OrderState.CANCELLED},
        }
        if new_state in allowed[self.state]:
            self.state = new_state
            st = f"State change: {new_state}"
        else:
            st = f"Invalid State."
        return st
    
    def __repr__(self):
        return f"Order(symbol={self.symbol!r}, side={self.side!r}, qty={self.qty})"