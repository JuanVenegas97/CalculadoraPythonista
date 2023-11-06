# Seno 
def seno(a,t):
  """
  Esta función calcula el seno de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Seno del ángulo (num)

  Ejemplo:
  >>> seno(30,D)
  0.5
  """
  # Condicion que establece el formato de entrada del ángulo

    if t == 'R':
	a = float(a)
    else:
        a = math.radians(float(a))
	
  return math.sin(a)
