
import pytest
from datetime import date, datetime, time
from seasons import conv_text, validate_date

def test_invalid_date():
    with pytest.raises(SystemExit):
        validate_date("Invalid date")

def test_conv_text ():
    assert conv_text("10") == "Ten minutes"
