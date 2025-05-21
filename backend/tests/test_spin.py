from backend.core.slot_machine import SlotMachine

def test_spin_has_three_symbols():
    sm = SlotMachine()
    result = sm.spin()
    assert len(result) == 3
    for symbol in result:
        assert isinstance(symbol, str)

def test_payout_return_type():
    sm = SlotMachine()
    result = sm.calculate_payout(["BAR", "BAR", "BAR"])
    assert isinstance(result, tuple)
    assert isinstance(result[0], int)
    assert isinstance(result[1], str)
