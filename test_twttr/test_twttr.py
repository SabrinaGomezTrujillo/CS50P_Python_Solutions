import pytest

from twttr import shorten

def test_default():
    assert shorten("123") == "123"

def test_argument():
    assert shorten("ines") == "ns"
    assert shorten("SA.BRI") == "S.BR"
    assert shorten("SabrI") == "Sbr"


