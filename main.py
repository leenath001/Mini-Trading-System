from systems.FIX_parser import FIX_parser
from systems.Order_Sim import Order, OrderState
from systems.Risk_Eng import RiskEngine
from systems.Logger import PositionLog, SystemLog
from systems.FIX_generator import start_FIX_Stream
import time

def on_FIX(msg):
    parsed = FIX_parser(msg)

    order = Order(
        parsed[55],
        int(parsed[38]),
        int(parsed[54])
    )
    print(order)

    risk = RiskEngine(order, max_order_size=1000, max_position=2000)
    result = risk.check() 

    if result == OrderState.ACKED:
        pos = PositionLog(order.symbol)
        pos.update(order.symbol)
        print(f"Position for {order.symbol}: {pos.position_size}")

    SystemLog().update(order)

def main():
    start_FIX_Stream(2, on_FIX)
    print("FIX Stream started. Processing messages.")

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()