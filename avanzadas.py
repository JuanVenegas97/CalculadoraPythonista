# Arcocoseno 
def arcocoseno(a,t):
  """
  Esta función calcula el arcocoseno de un número a, cuyo formato de salida puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Arcoseno del ángulo (num)

  Ejemplo:
  >>>arcocoseno(0.5,D)
  60
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    return acos(float(a))
  else:
    return acos(float(a))*180/math.pi
