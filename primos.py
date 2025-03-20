"""
Sebastian Pérez Capitano

>>> esPrimo(5)
True

>>> esPrimo(2)
True

>>> esPrimo(74211)
False

"""


def esPrimo(numero):
    """
    Devuelve True si el numero es primo, False si no lo es.

    >>> for numero in range(2, 10): 
    ...     print(esPrimo(numero))
    True
    True
    False
    True
    False
    True
    False
    False
    """
    for prueba in range(2, numero):
        if numero % prueba == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
