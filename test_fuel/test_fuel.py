from fuel import convert
from fuel import gauge


def test_convert_integer():
    assert convert("5/5") == 100


def test_convert_decimal():
    assert convert("6/8") == 75

def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("9/4")


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("5/8.5")


def test_convert_negative_numbers():
    with pytest.raises(ValueError):
        convert("-1/2")


def test_convert_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("8/0")


def test_gauge_default():
    assert gauge(50) == "50%"


def test_gauge_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
