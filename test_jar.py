import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        Jar(capacity=-1)
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        Jar().deposit(-1)
    with pytest.raises(ValueError):
        Jar().deposit(13)
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5



def test_withdraw():
    with pytest.raises(ValueError):
        Jar().withdraw(-1)
    with pytest.raises(ValueError):
        Jar().withdraw(1)
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
