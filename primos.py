"""
 Sebastian Pérez Capitano

Funciones:
- esPrimo(numero): Determina si un número es primo.
- primos(numero): Devuelve todos los números primos menores que el argumento.
- descompon(numero): Descompone un número en factores primos.
- mcm(numero1, numero2): Calcula el mínimo común múltiplo de dos números.
- mcd(numero1, numero2): Calcula el máximo común divisor de dos números.
- mcmN(*numeros): Calcula el mínimo común múltiplo de varios números.
- mcdN(*numeros): Calcula el máximo común divisor de varios números.

Tests unitarios:
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcmN(42, 60, 70, 63)
1260
>>> mcdN(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Determina si un número es primo.
    
    Args:
        numero (int): Número a evaluar.
        
    Returns:
        bool: True si es primo, False si no lo es.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que el argumento.
    
    Args:
        numero (int): Límite superior (no incluido) para la búsqueda de primos.
        
    Returns:
        tuple: Tupla con los números primos encontrados.
    """
    return tuple([num for num in range(2, numero) if esPrimo(num)])

def descompon(numero):
    """
    Descompone un número en factores primos.
    
    Args:
        numero (int): Número a descomponer.
        
    Returns:
        tuple: Tupla con los factores primos ordenados de menor a mayor.
    """
    factores = []
    if numero < 2:
        return tuple()
    
    # Manejo especial para números negativos
    if numero < 0:
        factores.append(-1)
        numero = -numero
    
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero = numero // divisor
        divisor += 1
        if divisor * divisor > numero and numero > 1:
            factores.append(numero)
            break
    return tuple(factores)

def mcm(numero1, numero2):
    """
    Calcula el mínimo común múltiplo de dos números a partir de su descomposición en factores primos.
    
    Args:
        numero1 (int): Primer número.
        numero2 (int): Segundo número.
        
    Returns:
        int: Mínimo común múltiplo de los dos números.
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    
    # Creamos un diccionario con los factores máximos
    factores_mcm = {}
    
    for factor in factores1:
        factores_mcm[factor] = factores_mcm.get(factor, 0) + 1
    
    for factor in factores2:
        if factores_mcm.get(factor, 0) < factores2.count(factor):
            factores_mcm[factor] = factores2.count(factor)
    
    resultado = 1
    for factor, exponente in factores_mcm.items():
        resultado *= factor ** exponente
    
    return resultado

def mcd(numero1, numero2):
    """
    Calcula el máximo común divisor de dos números a partir de su descomposición en factores primos.
    
    Args:
        numero1 (int): Primer número.
        numero2 (int): Segundo número.
        
    Returns:
        int: Máximo común divisor de los dos números.
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    
    # Creamos un diccionario con los factores mínimos comunes
    factores_mcd = {}
    
    for factor in set(factores1):
        if factor in factores2:
            min_count = min(factores1.count(factor), factores2.count(factor))
            factores_mcd[factor] = min_count
    
    resultado = 1
    for factor, exponente in factores_mcd.items():
        resultado *= factor ** exponente
    
    return resultado

def mcmN(*numeros):
    """
    Calcula el mínimo común múltiplo de varios números.
    
    Args:
        *numeros (int): Números para calcular el mcm.
        
    Returns:
        int: Mínimo común múltiplo de los números proporcionados.
    """
    if not numeros:
        return 0
    
    # Inicializamos con el primer número
    current_mcm = numeros[0]
    
    for num in numeros[1:]:
        current_mcm = mcm(current_mcm, num)
    
    return current_mcm

def mcdN(*numeros):
    """
    Calcula el máximo común divisor de varios números.
    
    Args:
        *numeros (int): Números para calcular el mcd.
        
    Returns:
        int: Máximo común divisor de los números proporcionados.
    """
    if not numeros:
        return 0
    
    # Inicializamos con el primer número
    current_mcd = numeros[0]
    
    for num in numeros[1:]:
        current_mcd = mcd(current_mcd, num)
    
    return current_mcd

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)