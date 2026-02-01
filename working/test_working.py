import pytest

from working import convert
def test_working():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("7:30 AM to 1:55 PM") == "07:30 to 13:55"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("6:15 PM to 7:15 AM") == "18:15 to 07:15"

def test_working_invalid():
    with pytest.raises(ValueError):
        convert("9 to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 1:35 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 12 AM")
    with pytest.raises(ValueError):
        convert("1:15 PM - 3:30 AM")

