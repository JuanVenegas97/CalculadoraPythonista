# División
def division(a, b):
  """
  Esta función realiza la división de a en b, con b distinto de cero.

  Args:
  a, b (num): a es el dividendo y b el divisor.

  Return:
  (num): Resultado de la división.

  Ejemplo:
  >>> division(6,2)
  3
  """
  # Excepción para división por cero
  if b == 0:
    return "Error: No se puede dividir por cero"
  return a / b

# Multiplicación
def multiplicacion(a, b):
  """
  Esta función devuelve el producto entre a y b.

  Args:
  a, b (num): Valores que se multiplicarán entre sí.

  Return:
  (num): Resultado de la multiplicación entre a y b.

  Ejemplo:
  >>> multiplicacion(3, 4)
  12
  """
  return a * b

# Suma
def suma(a, b):
    """
    Esta función devuelve la suma de dos valores.

    Args:
    a, b (num): Valores numéricos que serán sumados.

    Return:
    (num): Valor de la suma entre a y b.

    Ejemplo:
    >>> suma(2,3)
    5
    """
    return a + b
