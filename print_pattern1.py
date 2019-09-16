def reflective_pattern(count=7):
    """Based on input param "count", prints the pattern
    >>> reflective_pattern(5)
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    """

    # SOLUTION: Using List comprehension, find upper increment and lower decrement decrement sections and join them together
    print("\n".join(['*'*i for i in range(1,count+1)]) + "\n" + "\n".join(['*'*i for i in range(count-1,0,-1)]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
