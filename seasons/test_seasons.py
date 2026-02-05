
import pytest
from datetime import date, datetime, time
from seasons import validate_date, __str__

def test_invalid_date():
    with pytest.raises(SystemExit):
        validate_date("Invalid date")

def test_valid_date():
    assert validate_date(dob=datetime.strptime("2000-01-01", "%Y-%m-%d").date()) == 13726080.0
