def fibonacci(n):
    previous = 0
    current = 1
    try:
        for i in range(n):
            previous, current = current, previous + current
        return previous
    except TypeError:
        return ("Input should be a one integer")

def lucas(n):
    previous = 2
    current = 1
    try:
        for i in range(n):
            previous, current = current, previous + current
        return previous
    except TypeError:
        return ("Input should be a one integer")


