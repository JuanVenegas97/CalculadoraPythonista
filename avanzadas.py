import math

# Tangente 
def tangente(a,t):

  """
  Esta función calcula la tangente de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Tangente del ángulo (num)

  Ejemplo:
  >>>tangente(45,D)
  1

  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    a = float(a)
  else:
    a = math.radians(float(a))
	
  return math.tan(a)

