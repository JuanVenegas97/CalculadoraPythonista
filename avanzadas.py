import math

def seno(angulo, en_radianes=True):
    if en_radianes:
        return math.sin(angulo)
    else:
        angulo_radianes = math.radians(angulo)  # Convierte grados a radianes
        return math.sin(angulo_radianes)

# Ejemplo de uso
angulo_grados = 45  # Ángulo en grados
angulo_radianes = math.pi / 4  # Ángulo en radianes (equivalente a 45 grados)

resultado1 = seno(angulo_grados, en_radianes=False)
resultado2 = seno(angulo_radianes, en_radianes=True)