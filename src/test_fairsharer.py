import pytest
from fairsharer import fair_sharer

def test_fair_sharer():
    # Test case 1
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert result == [100, 800, 900, 0]

    # Test case 2
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert result == [100, 890, 720, 90]
