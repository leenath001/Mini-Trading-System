import pytest
from systems.Risk_Eng import RiskEngine
from systems.Order_Sim import Order, OrderState
from systems.Logger import PositionLog

def test_risk_engine():
    ord = Order('NVDA', 100, 1)
    log = PositionLog('NVDA')
    x = RiskEngine(ord, 1000, 2000)
    assert x.check() == f"State change: {OrderState.ACKED}"

