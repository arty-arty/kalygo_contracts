from pyteal import *
from contracts.escrow.constants import *


@Subroutine(TealType.uint64)
def guard_buyer_close_out():
    return Seq(
        And(
            App.globalGet(GLOBAL_BUYER) == Txn.sender(),
            Txn.application_args[0] == CLOSE_OUT_CONTRACT_BALANCE,
        )
    )
