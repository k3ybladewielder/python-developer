def soma(a, b):
    """
    Função que realiza a soma de dois números.

    >>> soma(2, 3)
    5
    >>> soma(-1, 1)
    0
    >>> soma(10, -5)
    5
    """
    return a + b
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
