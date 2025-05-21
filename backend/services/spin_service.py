from backend.core.slot_machine import SlotMachine
from backend.model.spin_result import SpinResult


class SpinService:
    def __init__(self):
        self.slot_machine = SlotMachine()

    def spin(self) -> SpinResult:
        symbols = self.slot_machine.spin()
        payout, message = self.slot_machine.calculate_payout(symbols)
        return SpinResult(
            reels=symbols,
            win=payout > 0,
            payout=payout,
            message=message
        )