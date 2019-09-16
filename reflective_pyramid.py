def reflective_pyramid(count=7):
    """
    Draws a reflective pyramid

    >>> reflective_pyramid(3)
     *
    ***
     *

    >>> reflective_pyramid(5)
      *
     ***
    *****
     ***
      *

    """

    pyramid_list = []

    base_matrix_list = [index*" " + "*"*(num) for index, num in enumerate(range(count, 0, -2))]
    pyramid_list.extend(base_matrix_list[::-1])
    pyramid_list.extend(base_matrix_list[1:])

    pyramid_str = "\n".join(pyramid_list)

    print (pyramid_str)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
