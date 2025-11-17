import pytest
from systems.Order_Sim import Order, OrderState

def test_Order_transition():
    order = Order('AAPL', 100, 1)
    order.transition(OrderState.ACKED)
    assert order.state == OrderState.ACKED
