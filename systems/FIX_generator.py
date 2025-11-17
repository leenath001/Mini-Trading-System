## Generates FIX protocol strings for ingestion by FIX_parser.py
#  See https://ref.onixs.biz/fix-message.html for str documentation

from datetime import datetime
import time
from threading import Thread

def FIX_Protocol_Generator():
    """
    Generates FIX Protocol message with preset parameters.
    """ 
    BEGIN_STR = 'FIX.4.2'
    BODY_LENGTH = 100
    MSG_TYPE = 'D'
    SENDER_COMP_ID = 'ONIXS'
    TARGET_COMP_ID = 'CME'
    MSG_SEQ_NUM = 2
    SENDING_TIME = datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3]
    CIORDERID = 1023
    HANDINST = 1
    ORDER_QTY = 100
    SYMBOL = "NVDA"
    ORDER_TYPE = 1
    SIDE = 1
    TRANSACT_TIME = datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3]
    CHECKSUM = 12

    return f"8={BEGIN_STR}\x019={BODY_LENGTH}\x0135={MSG_TYPE}\x0149={SENDER_COMP_ID}\x0156={TARGET_COMP_ID}\x0134={MSG_SEQ_NUM}\x0152={SENDING_TIME}\x0111={CIORDERID}\x0121={HANDINST}\x0138={ORDER_QTY}\x0155={SYMBOL}\x0140={ORDER_TYPE}\x0154={SIDE}\x0160={TRANSACT_TIME}\x0110={CHECKSUM}"


def FIX_Stream(time_btwn_msg: int, handler):
    try:
        while True:
            msg = FIX_Protocol_Generator()
            handler(msg)                     
            time.sleep(time_btwn_msg)
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Stream Stopped.")
    
def start_FIX_Stream(interval, handler):
    t = Thread(target=FIX_Stream, args=(interval, handler), daemon=True)
    t.start()
    return t
