import math
#AVANZADAS 
# Seno 
def seno(a,t):

  """
  Esta función calcula el seno de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (1) o en Grados (0) 

  Args:
  a (num), t (num)

  Return: 
  CSeno del ángulo (num)

  Ejemplo:
  >>>seno(30,D)
  0.5
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 1:
    a = float(a)
  elif t == 0:
    a = math.radians(float(a))
  else:
    print("Debe ingresar R para radianes o D para grados sexagesimales")
  return math.sin(a)

# Coseno 
def coseno(a,t):

  """
  Esta función calcula el coseno de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (1) o en Grados (0) 

  Args:
  a (num), t (num)

  Return: 
  Coseno del ángulo (num)

  Ejemplo:
  >>>coseno(60,D)
  0.5
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 1:
    a = float(a)
  elif t == 0:
    a = math.radians(float(a))
  else:
    print("Debe ingresar R para radianes o D para grados sexagesimales")
	
  return math.cos(a)

# Tangente 
def tangente(a,t):

  """
  Esta función calcula la tangente de un ángulo a, cuyo formato de entrada puede ser:
  en Radianes (1) o en Grados (0) 

  Args:
  a (num), t (num)

  Return: 
  Tangente del ángulo (num)

  Ejemplo:
  >>>tangente(45,D)
  1.0
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 1:
    a = float(a)
  elif t == 0:
    a = math.radians(float(a))
  else:
    print("Debe ingresar 1 para radianes o 0 para grados sexagesimales")
	
  return math.tan(a)




# Arcoseno 
def arcoseno(a,t):
  """
  Esta función calcula el arcoseno de un número a, cuyo formato de salida puede ser:
  en Radianes (1) o en Grados (0) 

  Args:
  a (num), t (num)

  Return: 
  Arcoseno del ángulo (num)

  Ejemplo:
  >>>arcoseno(0.5,0)
  30
  """
  # Condicion que establece el formato del argumento y de la salida

  if a <-1 or a > 1:
    return print("No es un argumento válido")
  else:
    if t == 1:
      return math.asin(float(a))
    elif t == 0:
      return math.asin(float(a))*180/math.pi
    else:
      print("Debe ingresar 1 para radianes o 0 para grados sexagesimales")

  
  # Arcocoseno 
def arcocoseno(a,t):
  """
  Esta función calcula el arcocoseno de un número a, cuyo formato de salida puede ser:
  en Radianes (1) o en Grados (0) 

  Args:
  a (num), t (char)

  Return: 
  Arcoseno del ángulo (num)

  Ejemplo:
  >>>arcocoseno(0.5,D)
  60
  """
  # Condicion que establece el formato del argumento y de la salida

  if a <-1 or a > 1:
    return print("No es un argumento válido")
  else:
    if t == 1:
      return math.acos(float(a))
    elif t == 0:
      return math.acos(float(a))*180/math.pi
    else:
      print("Debe ingresar 1 para radianes o 0 para grados sexagesimales")
  
# Arcotangente 
def arcotangente(a,t):
  """
  Esta función calcula el arcotangente de un número a, cuyo formato de salida puede ser:
  en Radianes (1) o en Grados (0) 

  Args:
  a (num), t (num)

  Return: 
  Arcoseno del ángulo (num)

  Ejemplo:
  >>>arcotangente(1,0)
  45
  """
  # Condicion que establece el formato de entrada del ángulo

  if t == 'R':
    return math.atan(float(a))
  else:
    return math.atan(float(a))*180/math.pi


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
      return "El número y la base deben ser mayores que 0 y la base no puede ser igual a 1."


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

  if a > 0 :
    return math.log(a)
  else: 
    return "El número  deben ser mayor que 0."


