## Checks internal risk limits and blocks order if position exceeds limits
#  

from systems.Logger import PositionLog
from systems.Order_Sim import Order, OrderState

class RiskEngine():

    def __init__(self,ord: Order, max_order_size=1000, max_position=2000):
        self.ord = ord
        self.max_order_size = max_order_size
        self.max_position = max_position
        self.pos = PositionLog(ord.symbol)

    def check(self):
        projected_pos = self.pos.position_size + (
            self.ord.qty if self.ord.side == 1 else -self.ord.qty
        )

        if self.ord.qty > self.max_order_size:
            return self.ord.transition(OrderState.REJECTED)
        if abs(projected_pos) > self.max_position:
            return self.ord.transition(OrderState.REJECTED)
        return self.ord.transition(OrderState.ACKED)

