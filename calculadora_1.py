def suma(num1, num2):
    """
    la funcion suma dos números y retorna el resultado.

    Parámetros:
    num1 (int o float): El primer número a sumar.
    num2 (int o float): El segundo número a sumar.

    Retorna:
    int o float: La suma de los dos números.
    """
    return num1 + num2

def resta(num1, num2):
    """
    La función resta el segundo número del primero y retorna el resultado.

    Parámetros:
    num1 (int o float): El número al que se le resta.
    num2 (int o float): El número que se resta.

    Retorna:
    int o float: La resta de los dos números.
    """
    return num1 - num2

def multiplicacion(num1, num2):
    """
    Esta función multiplica dos números y retorna el resultado.

    Parámetros:
    num1 (int o float): El primer número que va a multiplicar.
    num2 (int o float): El segundo número que va a multiplicar.

    Retorna:
    int o float: El producto de los dos números.
    """
    return num1 * num2

def division(num1, num2):
    """
    La función divide el primer número por el segundo y retorna el resultado.

    Parámetros:
    num1 (int o float): El número dividendo.
    num2 (int o float): El número divisor distinto de cero.

    Retorna:
    float: El resultado de la división.
    """
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir por cero"

# Ejemplos de uso de las funciones de la calculadora
print(suma(7, 3))
print(resta(9, 5))
print(multiplicacion(10, 4))
print(division(6, 2))
