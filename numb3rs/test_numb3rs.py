import pytest
from numb3rs import validate

def test_numb3rs():
    assert validate("127.0.0.1") == True

    assert validate("256.100.50.25") == False
    assert validate("192.168.1.300") == False

def test_numb3rs_additional():
    assert validate("001.001.001.001") == False
    assert validate("192.168.01") == False

def test_numb3rs_edge_cases():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True 
