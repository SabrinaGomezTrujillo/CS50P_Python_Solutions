from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_h():
    assert value("h") == 20

def test_value_no_h():
    assert value("aloha") == 100

def test_case_insensitive():
    assert value("hello") == value("HELLO") == value("Hello") == 0

def test_phrase():
    assert value("hello susan") == 0
    assert value("como va?") == 100
