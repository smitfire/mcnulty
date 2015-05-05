def ways(cents, coins=[25, 10, 5, 1]):
    """Return the number of ways to make change.
    >>> ways(1)
    1
    >>> ways(5)
    2
    >>> ways(10)
    4
    >>> ways(100)
    242
    """
    if cents < 0 or not coins:
        return 0
    if cents == 0:
        return 1
    return ways(cents - coins[0], coins) + ways(cents, coins[1:])



    raise NotImplementedError

