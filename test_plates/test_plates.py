from plates import is_valid


def test_lenght_min_2():
    assert is_valid("A") == False


def test_lenght_max_6():
    assert is_valid("AAAA17878") == False


def test_first_2_alpha():
    assert is_valid("54") == False


def test_alphanum():
    assert is_valid(s="aa23") == True
    assert is_valid(s="++") == False


def test_no_0_first():
    assert is_valid("AA0214") == False


def test_numbers_after_1st_number():
    assert is_valid("AA52X4") == False


def test_default():
    assert is_valid("CDE35") == True
