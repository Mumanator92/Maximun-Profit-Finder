def maxPro(n):
    """This function return the maximum earn of list a prices.

    Args:
        n(list(int)): int

    >>> maxPro([100, 180, 260, 310, 40, 535, 695])
    865
    """
    
    profit = 0
    for i in range(1,len(n)):
        if n[i] > n[i-1]:
            profit += n[i] - n[i-1]
    print(profit)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
