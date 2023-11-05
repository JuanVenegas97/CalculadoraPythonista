# Cociente (División entera)
def cociente(a, b):
  """
  Esta función realiza la división de a en b. Devuelve la parte entera del resultado.

  Args:
  a,b (num): a es dividendo y b el divisor.

  Return:
  (num): Parte entera de la división de a en b.

  Ejemplo:
  >>> cociente(10, 3)
  3
  """
  # Excepción del caso de división por cero
  if b == 0:
      return "Error: No se puede dividir por cero"
  return a // b