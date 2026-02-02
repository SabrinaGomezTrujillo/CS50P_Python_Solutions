import pytest
from response import validation
def test_validation():
    assert validation("prueba@gmail.com") == "Valid"
    assert validation("aveces123@yahoo.com") == "Valid"
    assert validation("@harvard.edu") == "Invalid"
    assert validation(" error123.gob") == "Invalid"
