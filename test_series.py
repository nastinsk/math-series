from series import fibonacci, lucas

# Fibonacci tests"
# Expected Outcome

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

# Expected Failure

def test_negative():
    expected = 0
    actual = fibonacci(-4)
    assert actual == expected

def test_letter():
    expected = "Input should be a one integer"
    actual = fibonacci("a")
    assert actual == expected

# Edge Case

def test_float():
    expected = "Input should be a one integer"
    actual = fibonacci(1.354)
    assert actual == expected


# Lucas tests:
# Expected Outcome
def test_zero_lucas():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_one_lucas():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_three_lucas():
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_four_lucas():
    expected = 7
    actual = lucas(4)
    assert actual == expected

def test_15n_lucas():
    expected = 1364
    actual = lucas(15)
    assert actual == expected

# expected failure

def test_negative_lucas():
    expected = 2
    actual = lucas(-4)
    assert actual == expected


