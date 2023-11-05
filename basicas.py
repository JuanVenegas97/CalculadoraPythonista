# Resto (residuo)
def resto(a, b):
    """
    Esta función realiza la división de a en b y devuelve el residuo de dicha división.

    Args:
    a, b  (num): a es el dividendo y b el divisor.

    Return:
    (num): Residuo de la división de a en b.

    Ejemplo:
    >>> resto(10,3)
    1
    """
    # Excepción del caso de división por cero
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a % b