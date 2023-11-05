# División
def division(a, b):
  """
  Esta función realiza la división de a en b.

  Args:
  a, b (num): a será dividendo y b el divisor.

  Return:
  (num): Resultado de la división de a en b.

  Ejemplo:
  >>> division(12,3)
  4
  """
  # Excepción del caso división por cero
  if b == 0:
    return "Error: No se puede dividir por cero"
  return a / b