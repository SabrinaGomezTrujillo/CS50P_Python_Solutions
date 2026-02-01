import pytest
from um import count

def test_um():
    assert count ("Umbrella, um., hola, UM") == 2
    assert count ("um um um") == 3
    assert count ("hello world") == 0

 