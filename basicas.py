# Raíz cuadrada
def raizCuadrada(numero):
    """
    Esta función calcula la raíz cuadrada de un número.

    Args:
    numero (num): Número al que se le calculará la raíz cuadrada.

    Return:
    (num): valor de la raíz cuadrada de numero.

    Ejemplo:
    >>> raizCuadrada(16)
    4
    """
    # Excepción para evitar caso complejo
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return numero ** 0.5