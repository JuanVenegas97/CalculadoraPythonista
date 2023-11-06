# Raíz cuadrada
def raiz_cuadrada(numero):
  """
  Esta función calcula la raíz cuadrada de un número.

  Args:
  numero (num): número positivo al que se le calculará la raíz cuadrada.

  Return:
  (num): Valor de la raíz cuadrada de numero.

  Ejemplo:
  >>> raiz_cuadrada(16)
  4
  """
  # Excepción caso complejo
  if numero < 0:
      return "Error: No se puede calcular la raíz cuadrada de un número negativo"
  return numero ** 0.5