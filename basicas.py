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

# Multiplicación
def multiplicacion(a, b):
  """
  Esta función devuelve el producto entre los valores a y b.

  Args:
  a, b (num): Valores a ser multiplicados.

  Return:
  (num): Resultado de la multiplicación entre a y b.

  Ejemplo:
  >>> multiplicacion(4, 5)
  20
  """
  return a * b

# Resta
def resta(a, b):
  """
  Esta función devuelve la resta entre los valores a y b.

  Args:
  a, b (num): Valores a ser restados.

  Return:
  (num): Resultado de la resta de a y b.

  Ejemplo:
  >>> resta(9, 3)
  6
  """
  return a - b

# Suma
def suma(a, b):
  """
  Esta función devuelve la suma de los valores a y b.

  Args:
  a, b (num): Valores a ser sumados.

  Return:
  (num): Resultado de la suma de a y b.

  Ejemplo:
  >>> suma(3,2)
  5
  """
  return a + b