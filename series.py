def fibonacci(n):
    previous = 0
    current = 1

    for i in range(n):
        previous, current = current, previous + current

    return previous
    

