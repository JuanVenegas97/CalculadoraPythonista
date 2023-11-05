# Cociente (División entera)
def cociente(a, b):
  """
  Esta función realiza la división entera de a en b.

  Args:
  a, b (num): a es el dividendo y b el divisor.

  Return:
  (num): parte entera del resultado de la división de a en b.

  Ejemplo:
  >>> cociente(10,3)
  3
  """
  # Excepción del caso de división por cero
  if b == 0:
      return "Error: No se puede dividir por cero"
  return a // b