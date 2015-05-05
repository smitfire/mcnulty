def fibonacci(n):
    """
    Return the fibonacci of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    """

    if n <= 2:
        fib = 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
    return fib


if __name__ == "__main__":
    import doctest
    doctest.testmod()
