from series import fibonacci

def test_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_15n():
    expected = 610
    actual = fibonacci(15)
    assert actual == expected

# expected failure

def test_negative():
    expected = 0
    actual = fibonacci(-4)
    assert actual == expected

