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