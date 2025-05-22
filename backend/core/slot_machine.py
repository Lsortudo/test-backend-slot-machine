import random
from typing import List, Tuple

class SlotMachine:
    def __init__(self):
        self.virtual_to_physical = self._build_virtual_to_physical_map()

    def _build_virtual_to_physical_map(self) -> List[Tuple[int, str]]:
        # virtual reel strip (ainda acho que da pra melhorar, mas esse foi o entendimento basico/rapido que entendi de como funciona isso, mesmo sendo limitacao da maquina presencial, queria colocar o mesmo pensamento aqui)
        mapping = [
            (range(1, 4), "BLANK"),
            ([4], "SEVEN"),
            (range(5, 10), "BLANK"),
            (range(10, 13), "ONE_BAR"),
            (range(13, 20), "BLANK"),
            (range(20, 22), "CHERRY"),
            (range(22, 27), "BLANK"),
            ([27], "DOUBLE_DIAMOND"),
            (range(28, 33), "BLANK"),
            (range(33, 36), "ONE_BAR"),
            (range(36, 40), "BLANK"),
            ([40], "THREE_BAR"),
            (range(41, 43), "BLANK"),
            ([43], "SEVEN"),
            (range(44, 52), "BLANK"),
            (range(52, 55), "ONE_BAR"),
            (range(55, 60), "BLANK"),
            ([60], "DOUBLE_DIAMOND"),
            (range(61, 66), "BLANK"),
            (range(66, 68), "TWO_BAR"),
            (range(68, 71), "BLANK"),
            (range(71, 73), "ONE_BAR"),
        ]

        virtual_to_physical = {}
        for rng_range, symbol in mapping:
            for i in rng_range:
                virtual_to_physical[i] = symbol
        return virtual_to_physical

    def spin(self) -> List[str]:
        # 1 a 72, nao entendi o erro mas dps consertar !!!!!!
        return [self.virtual_to_physical[random.randint(1, 72)] for _ in range(3)]

    def calculate_payout(self, symbols: List[str]) -> Tuple[int, str]:
        wild = "DOUBLE_DIAMOND"
        if symbols.count(wild) == 3:
            return (1000, "Jackpot! Triple Double Diamond!")

        non_wilds = [s for s in symbols if s != wild]
        base_prize = 0

        if len(non_wilds) == 3 and len(set(non_wilds)) == 1:
            base_prize = {
                "SEVEN": 300,
                "ONE_BAR": 150,
                "TWO_BAR": 100,
                "THREE_BAR": 80,
                "CHERRY": 50,
                "BLANK": 0,
            }.get(non_wilds[0], 0)
        elif non_wilds.count(non_wilds[0]) == 2 and symbols.count(wild) == 1:
            base_prize = 30
        elif symbols.count("CHERRY") == 1:
            base_prize = 5
        elif symbols.count("CHERRY") == 2:
            base_prize = 10

        multiplier = 2 ** symbols.count(wild)
        return (base_prize * multiplier, f"{'No win' if base_prize == 0 else 'Win with multiplier'}")
