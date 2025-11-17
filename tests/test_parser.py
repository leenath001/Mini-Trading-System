from systems.FIX_parser import FIX_parser
import pytest 

def test_FIX_parser():
    test_str = "8=FIX.4.2\x019=133\x0135=D\x0149=SENDER123\x0156=TARGET456\x0134=7\x0152=20251117-16:42:58.912\x0111=ORD498372\x0121=1\x0155=MSFT\x0154=1\x0138=250\x0140=2\x0144=374.82\x0159=0\x0110=057"
    tst = {
    8: "FIX.4.2",
    9: "133",
    35: "D",
    49: "SENDER123",
    56: "TARGET456",
    34: "7",
    52: "20251117-16:42:58.912",
    11: "ORD498372",
    21: "1",
    55: "MSFT",
    54: "1",
    38: "250",
    40: "2",
    44: "374.82",
    59: "0",
    10: "057"}
    assert tst == FIX_parser(test_str)
