# Resto (residuo)
def resto(a, b):
  """
  Esta función realiza la división de a en b. Luego, devuelve el residuo de dicha división.

  Args:
  a, b (num): a es dividendo y b el divisor.

  Return:
  (num): Residuo de la división de a en b.

  Ejemplo:
  >>> resto(10,3)
  1
  """
  # Excepción del caso de divsión por cero
  if b == 0:
      return "Error: No se puede dividir por cero"
  return a % b