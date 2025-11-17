import pytest
from systems.Logger import SystemLog,PositionLog
from systems.Order_Sim import Order,OrderState

def test_singleton():
    log1 = SystemLog()
    log2 = SystemLog()
    NVDA = PositionLog('NVDA')
    AAPL = PositionLog('AAPL')
    assert log1 == log2
    assert NVDA != AAPL

def test_order_update():
    x = Order('NVDA', 100, 1)
    pos_log = PositionLog("NVDA")
    pos_log.update(x)
    assert pos_log.position_size == 100
