##  Class tracks and logs state of system and specific ticker position sizes
#   

from systems.Order_Sim import Order

class SystemLog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "logs"):
            self.logs = []

    def update(self,ord: Order):
        self.logs.append(ord)

class PositionLog:
    _instances = {}

    def __new__(cls, ticker):
        if ticker not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[ticker] = instance
        return cls._instances[ticker]  

    def __init__(self, ticker):
        if getattr(self, "_initialized", False):
            return
        self.ticker = ticker
        self.position_size = 0
        self.orders = []
        self._initialized = True

    def update(self,ord: Order):
        self.orders.append(ord)
        if ord.side == 1:
            self.position_size += ord.qty
        else: 
            self.position_size -= ord.qty