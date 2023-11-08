#CALCULADORA PYTHONISTA

import math
import basicas
import avanzadas

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("\nOpciones:")
    print(" 1. Suma")
    print(" 2. Resta")
    print(" 3. Multiplicación")
    print(" 4. División")
    print(" 5. Raíz Cuadrada")
    print(" 6. Potencia")
    print(" 7. División parte entera")
    print(" 8. División resto")
    print(" 9. Seno")
    print("10. coseno")
    print("11. Tangente")
    print("12. Arcoseno")
    print("13. Arcocoseno")
    print("14. Arcotangente")
    print("15. Logaritmo Natural")
    print("16. Logaritmo")
    print("17. Salir")
    return input("Seleccione una opción de 1 a 17: ")

while True:
    opcion = mostrar_menu()

    if opcion == '17':
        print("¡Hasta luego!")
        break



    if opcion in ('1', '2', '3', '4', '5', '6', '7', '8'):
        a = float(input("Ingrese el primer número: "))

        if opcion != '5':
            b = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            resultado = basicas.suma(a, b)
        elif opcion == '2':
            resultado = basicas.resta(a, b)
        elif opcion == '3':
            resultado = basicas.multiplicacion(a, b)
        elif opcion == '4':
            resultado = basicas.division(a, b)
        elif opcion == '5':
            resultado = basicas.raiz_cuadrada(a)
        elif opcion == '6':
            resultado = basicas.potencia(a, b)
        elif opcion == '7':
            resultado = basicas.cociente(a, b)
        elif opcion == '8':
            resultado = basicas.resto(a, b)

        print("Resultado:", resultado)

    if opcion in ('9', '10', '11'):
        t = float(input("Ingrese  1 para radian 0 para grado: "))
        a = float(input("Ingrese el ángulo: "))

        if opcion == '9':
            resultado = avanzadas.seno(a, t)
        elif opcion == '10':
            resultado = avanzadas.coseno(a, t)
        elif opcion == '11':
            resultado = avanzadas.tangente(a, t)

        print("Resultado:", resultado)

    if opcion in ('12', '13', '14'):
        t = float(input("Ingrese  1 para radian 0 para grado: "))
        a = float(input("Ingrese el número: "))

        if opcion == '12':
            resultado = avanzadas.arcoseno(a, t)
        elif opcion == '13':
            resultado = avanzadas.arcocoseno(a, t)
        elif opcion == '14':
            resultado = avanzadas.arcotangente(a, t)

        print("Resultado:", resultado)

    if opcion in ('15', '16'):
         a = float(input("Ingrese el número: "))

         if opcion == '16':
            b = float(input("Ingrese la base: "))

         if opcion == '15':
            resultado = avanzadas.logaritmonatural(a)
         elif opcion == '16':
            resultado = avanzadas.logaritmo(a, b)


         print("Resultado:", resultado)

