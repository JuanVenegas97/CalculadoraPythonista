# Arcotangente 
def arcotangente(a,t):
  """
  Esta función calcula el arcotangente de un número a, cuyo formato de salida puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Arcoseno del ángulo (num)

  Ejemplo:
  >>>arcotangente(1,D)
  45
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    return atan(float(a))
  else:
    return atan(float(a))*180/math.pi