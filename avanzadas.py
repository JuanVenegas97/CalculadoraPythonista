# Seno 
def seno(a,t):

  """
  Esta función calcula el seno de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  CSeno del ángulo (num)

  Ejemplo:
  >>>seno(30,D)
  0.5
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    a = float(a)
  else:
    a = math.radians(float(a))
	
  return math.sin(a)

# Coseno 
def coseno(a,t):

  """
  Esta función calcula el coseno de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Coseno del ángulo (num)

  Ejemplo:
  >>>coseno(60,D)
  0.5
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    a = float(a)
  else:
    a = math.radians(float(a))
	
  return math.cos(a)

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
  1.0
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    a = float(a)
  else:
    a = math.radians(float(a))
	
  return math.tan(a)




# Arcoseno 
def arcoseno(a,t):
  """
  Esta función calcula el arcoseno de un número a, cuyo formato de salida puede ser:
  en Radianes (R) o en Grados (D) 

  Args:
  a (num), t (char)

  Return: 
  Arcoseno del ángulo (num)

  Ejemplo:
  >>>arcoseno(0.5,D)
  30
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    return asin(float(a))
  else:
    return asin(float(a))*180/math.pi
  
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


# Logaritmo 
def logaritmo(a,b):
  """
  Esta función calcula el logaritmo de un número a, en base b 

  Args:
  a (num), b (num)

  Return: 
  Logaritmo en base b de a  (num)

  Ejemplo:
  >>>logaritmo(8,4)
  1.5
  """
  # Condicion que establece el formato de entrada del ángulo

  if a > 0 and b > 0 and b != 1:
        return math.log(a, b)
    else:
        Return "El número y la base deben ser mayores que 0 y la base no puede ser igual a 1."


# Logaritmo Natural 
def logaritmonatural(a):
  """
  Esta función calcula el logaritmo natural de un número a

  Args:
  a (num)

  Return: 
  Logaritmo natural de a  (num)

  Ejemplo:
  >>>logaritmonatural(5)
  1.609437912
  """
  # Condicion que establece el formato de entrada del número

  if a > 0 
        return math.log(a)
    else:
        Return "El número  deben ser mayores que 0."


