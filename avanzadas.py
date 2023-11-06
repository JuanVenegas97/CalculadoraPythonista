
# Arcoseno 
def arcoseno(a,t):
  """
  Esta función calcula el arcoseno de un número a, cuyo formato de salida puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Arcotangente del ángulo (num)

  Ejemplo:
  >>>arcoseno(0.5,D)
  30
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    return asin(float(a))
  else:
    return asin(float(a))*180/math.pi