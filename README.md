# CalculadoraPythonista

## Tabla de Contenidos : 

1 Descripción  
2 Instalación  
3 Uso  
4 Operaciones Básicas   
5 Funciones Avanzadas   
6 Prerrequisitos  
7 Contribución  
8 Licencia   
9 Implementación   
10 Merge conflicts  
11 Rastreo de autorías  
12 Autores  
13 Estado del proyecto  
14 Agradecimientos   
15 Notas de la versión 

## 1 Descripción: 
El presente proyecto corresponde al desarrollo de una Calculadora científica en Python que puede realizar operaciones matemáticas básicas y avanzadas, como operatoria aritmética, funciones trigonométricas exponenciales y logarítmicas. En líneas generales, se programó la calculadora  en base a llamadas de funciones hacia dos librerías externas que contienen las funciones, las que se ejecutan en un código principal 
Título del Proyecto: Un título descriptivo que identifica el proyecto.

## 2 Instalación: 
La Calculadora Pythonista   no requiere de mayor instalación, salvo que el programa principal y las librerías se encuentren en el mismo directorio donde Python ejecuta el programa o en su defecto, que se encuentren en la ruta de acceso de programa.

## 3 Uso: 
Esta versión de la  Calculadora Pythonista, permite hacer las operaciones aritméticas básicas de suma resta multiplicación división, además de dos opciones de división adicionales, parte entera y resto del cociente. También permite el cálculo de funciones trigonométricas y sus correspondientes funciones  inversas, además, admite ángulos en sistema de radianes y grados sexagesimales, adicionalmente, calcula logaritmos en distintas bases y una opción especial para logaritmo natural. Para utilizar la Calculadora Pythonista, simplemente se debe ejecutar el programa principal Calculadora y se desplegarán en la consola las distintas operaciones, funciones y una opción de salida, mientras el usuario no de la instrucción de salida (17), la calculadora seguirá activa esperando una opción elegida por el usuario.

## 4 Operaciones Básicas:
Esta calculadora permite el cálculo de operaciones binaria básicas como suma, resta, multiplicación, potencias, división y operaciones de resto y parte entera del cociente.

### 4 1 Suma:
Calcula la suma de dos números reales
### 4 2 Resta
Calcula la resta de dos números reales, al primer número ingresado se le resta el segundo número ingresado. 
### 4 3 Multiplicación
Calcula la multiplicación de dos números reales
### 4 4 Potencia
Calcula la potencia de dos números el primero es la base de la potencia y el segundo es el exponente 
### 4 5 Raíz cuadrada
Se calcula la raíz cuadrada del número ingresado estableciendo la condición que debe ser positivo
### 4 6 ivisión:
Calcula la división entre dos números, el primer número ingresado se divide por el segundo número ingresado, se establece la restricción que el segundo número debe ser distinto de cero. 
### 4 7 Parte entera del cociente:
Se calcula la parte entera del cociente entre dos números rales, se obtiene la parte entera del cociente entre el primer número ingresado dividido por el segundo número ingresado, se establece la restricción que el segundo número debe ser distinto de cero. 
### 4 8 Resto del cociente:
Se calcula el resto del cociente entre dos números rales, se obtiene el residuo del cociente entre el primer número ingresado dividido por el segundo número ingresado, se establece la restricción que el segundo número debe ser distinto de cero.

## 5 Funciones Avanzadas:
también se pueden calcular funciones más avanzadas, trigonométricas,  trigonométricas inversas y logarítmicas

### 5 1 Seno:
Se calcula el seno del ángulo ingresado, se le consulta previamente al usuario en qué sistema angular quiere ingresar este ángulo, grados sexagesimales (0) o radianes (1). 
### 5 2 Coseno:
Se calcula el coseno del ángulo ingresado, se le consulta previamente al usuario en qué sistema angular quiere ingresar este ángulo, grados sexagesimales (0) o radianes (1).
### 5 3 Tangente:
Se calcula la tangente del ángulo ingresado, se le consulta previamente al usuario en qué sistema angular quiere ingresar este ángulo, grados sexagesimales (0) o radianes (1).
### 5 4 Arcoseno
Se calcula el arcoseno del número ingresado, se le consulta previamente al usuario en qué sistema angular quiere la salida, grados sexagesimales (0) o radianes (1). Se establece la restricción que el número ingresado debe estar entre -1 y 1.
### 5 5 Arcocoseno
Se calcula el arcocoseno del número ingresado, se le consulta previamente al usuario en qué sistema angular quiere la salida, grados sexagesimales (0) o radianes (1). Se establece la restricción que el número ingresado debe estar entre -1 y 1.
### 5 6 Arcotangente:
Se calcula la arcotangente del número ingresado, se le consulta previamente al usuario en qué sistema angular quiere la salida, grados sexagesimales (0) o radianes (1).
### 5 7 Logaritmo:
Se calcula el logaritmo de un número como argumento en una base específica, se calcula el logaritmo del primer número ingresado, en la base correspondiente al segundo número ingresado. Se establecen restricciones para la base, que debe ser positiva y distinta de 1 y también para el argumento que debe ser positivo.

### 5 8 Logaritmo natural:
Se calcula el logaritmo natural de un número como argumento, se calcula el logaritmo natural del número ingresado. Se establece restriciones  para el argumento que debe ser positivo.


## 6 Prerrequisitos: 
Para poder usar la Calculadora Pythonista, es necesario ejecutarla en la consola de un intérprete de Python versión 3.7 y como se indicó anteriormente, que estén instaladas las librerías de las funciones externas en el mismo directorio o ruta de acceso del programa principal  Lista de software, bibliotecas y dependencias necesarias para ejecutar el proyecto.

## 7 Contribución: 
La estructura del código de la Calculadora Pythonista es muy simple, se basa en llamadas a funciones que se definen en librerías externas , lo que facilita implementar nuevas características, mejorando o agregando nuevas funciones a las librerías  y hacerles cabida en la estructura del código del programa principal.  

## 8 Licencia: 
Este código es libre se  puede utilizar y distribuir sin limitaciones, siempre y cuando no sea con fines de lucro ni beneficio económico alguno.

## 9 Implementación:
Este proyecto se realizo en una modalidad cooperotiva remota, se utilizaron dos repositorios locales cada uno perteneciente a cada miembrom del equipo A y B. En la primera etapa se programaron las librerias que contienen las funciones que son llamadas en el código principal. Las librerías basicas.py y avanzadas. py, fueron creadas en repositorios locales por cada integrante del equipo. A se encargo en primera instancia de las basicas.py y B de las avanzadas.py. Posteriormente se empujan estas versiones de las librerías al repositorio remoto  interactuando el equipo en mejoras y correcciones y resolviendo conflictos. Despoues, en forma colaborativa, se genera el código del programa principal calculadora.py.

## 10 Merge conflicts

Dado que en un principio ambos colaboradores trabajamos principalmente en archivos separados, los *merge conflicts* iban generándose sobre nuestras mismas modificaciones, por lo que inicialmente no interferíamos en el archivo que trabajaba el otro colaborador del proyecto. Es por esto que se generó un *merge conflict* más acorde a lo solicitado.

Cuando ya teníamos en la rama develop una versión del proyecto que podía ser enviada a la rama de release, hicimos la fusión de dichas ramas. Luego, desde la rama de release, comenzamos a editar simultáneamente el archivo README. Al hacer los commits comenzó el conflicto buscado, pues Github informó que el archivo había sido editado paralelamente por otro colaborador. Para solucionar esto, se tomó la opción de crear una nueva rama tipo "*patch*", con el objetivo de generar *pull request* que fusione esta rama auxiliar con release. Al hacer la pull request fue necesario solucionar el conflicto manualmente, es decir, se editó el archivo en la nube confirmando una nueva versión del mismo que pudiera ser fusionada en release. Al hacer esto, el otro colaborador tuvo un problema similar al intentar un nuevo commit, por lo que debió proceder con la misma estrategia recién comentada.

A continuación, se encuentran los SHA de las *pull request* mencionadas:


*  *pull request #44* : 7fc978fc26e86bf80105895fd844ebcacca7ce1c
*  *pull request #45* : 11379bf7917a059466abbb1f20b4f9b85801cbf6

## 11 Rastreo de autorías

Usando *git blame* se generaron 3 archivos de extensión *.txt* que contienen las autorías de cada linea de código de los archivos *.py* contenidos en el repositorio. Estos archivos son: *blame_basicas.txt*, *blame_avanzadas.txt* y *blame_calculadora.txt*.

## 12 Autores: 
Los autores de este código son estudiantes de la asignatura de Programación Avanzada del programa de Magister en simulación computacional que dicta la Pontificia Universidad Católica de Valparaíso. Juan Venegas y Claudio Guzmán

## 13 Estado del Proyecto: 
El proyecto está terminado, pero siempre disponible para aportes y modificaciones.

## 14 Agradecimientos: 
Agradecimientos a nuestro profesor Bady Gana por sus clases, tips y videos muy aclaradores sin los cuales hubiese sido muy difícil hacer este trabajo 

## 15 Notas de Versión: 
<<<<<<< HEAD
Información sobre las versiones anteriores y las actualizaciones recientes del proyecto.
=======
Información sobre las versiones anteriores y las actualizaciones recientes del proyecto.

>>>>>>> e6d8e925ac6a7a5deaf5c5d8db075b5181897dd2
