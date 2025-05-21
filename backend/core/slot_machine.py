import random
from typing import List, Tuple

class SlotMachine:
    def __init__(self):
        self.reels = self._generate_reels()

    def _generate_reels(self) -> List[List[str]]:
        base_strip = [
            "BLANK", "BLANK", "CHERRY", "CHERRY", "BAR", "BAR", "BAR",
            "DOUBLE_DIAMOND", "SEVEN", "BLANK"
        ]
        return [base_strip * 7 for _ in range(3)]

    def spin(self) -> List[str]:
        return [random.choice(reel) for reel in self.reels]

    def calculate_payout(self, symbols: List[str]) -> Tuple[int, str]:
        wild = "DOUBLE_DIAMOND"
        if symbols.count(wild) == 3:
            return (1000, "Jackpot! Triple Double Diamond!")

        non_wilds = [s for s in symbols if s != wild]
        base_prize = 0

        if len(set(non_wilds)) == 1 and len(non_wilds) == 3:
            base_prize = {
                "SEVEN": 300,
                "BAR": 150,
                "CHERRY": 50
            }.get(non_wilds[0], 0)
        elif non_wilds.count(non_wilds[0]) == 2 and symbols.count(wild) == 1:
            base_prize = 30
        elif symbols.count("CHERRY") == 1:
            base_prize = 5
        elif symbols.count("CHERRY") == 2:
            base_prize = 10

        multiplier = 2 ** symbols.count(wild)
        return (base_prize * multiplier, f"{'No win' if base_prize == 0 else 'Win with multiplier'}")
