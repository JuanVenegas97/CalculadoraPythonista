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
El presente proyecto corresponde al desarrollo de una Calculadora científica en Python que puede realizar operaciones matemáticas básicas y avanzadas, como operatoria aritmética, funciones trigonométricas exponenciales y logarítmicas. En líneas generales, se programó la calculadora  en base a llamadas de funciones desde dos librerías externas que las contienen. Estas se ejecutan con un *script* que es llamado desde terminal. 


## 2 Instalación: 
La Calculadora Pythonista no requiere de mayor instalación, salvo que el programa principal y las librerías se encuentren en el mismo directorio donde Python ejecuta el programa o, en su defecto, que se encuentren en la ruta de acceso de programa. El llamado se hace desde la terminal, el cual dará inicio a la rutina:

```
python calculadora.py 
```

## 3 Uso: 
Esta versión de la  Calculadora Pythonista, permite hacer las operaciones aritméticas básicas de suma resta multiplicación división, además de dos opciones de división adicionales, parte entera y resto del cociente. También permite el cálculo de funciones trigonométricas y sus correspondientes funciones inversas y, en adición, admite ángulos en sistema de radianes y grados sexagesimales. Calcula logaritmos en distintas bases y una opción especial para logaritmo natural. Para utilizar la Calculadora Pythonista, simplemente se debe ejecutar el programa principal Calculadora y se desplegarán en la consola las distintas operaciones, funciones y una opción de salida. Una vez completada una operación, la calculadora preguntará si se desea realizar una nueva. 

## 4 Operaciones Básicas:
Esta calculadora permite el cálculo de operaciones binarias básicas como suma, resta, multiplicación, potencias, división y operaciones de resto y parte entera del cociente.

### 4 1 Suma:
Calcula la suma de dos números reales.
### 4 2 Resta
Calcula la resta de dos números reales. Al primer número ingresado se le resta el segundo número ingresado. 
### 4 3 Multiplicación
Calcula el producto entre dos números reales.
### 4 4 Potencia
Calcula la potencia de dos números. El primero es la base de la potencia y el segundo es el exponente.
### 4 5 Raíz cuadrada
Se calcula la raíz cuadrada del número ingresado, estableciendo la condición de que debe ser positivo. En caso de no serlo, devolverá un *warning*.
### 4 6 División:
Calcula la división entre dos números. El primer valor ingresado se divide por el segundo ingresado. Se establece la restricción de que el segundo número debe ser distinto de cero. 
### 4 7 Cociente (División parte entera):
Se calcula la parte entera del cociente entre dos números rales. Obtiene la parte entera del cociente entre el primer número dividido por el segundo número ingresado. La restricción para este caso es que el segundo valor debe ser distinto de cero. 
### 4 8 Resto del cociente:
Se calcula el resto del cociente entre dos números rales. Obtiene el residuo del cociente entre el primer número ingresado dividido por el segundo número ingresado. La restricción es que el segundo número debe ser distinto de cero.

## 5 Funciones Avanzadas:
También se pueden calcular funciones más avanzadas, como: trigonométricas, trigonométricas inversas y logarítmicas.

### 5 1 Seno:
Se calcula el seno del ángulo ingresado. Se le consulta previamente al usuario en qué sistema angular quiere ingresar este ángulo: grados sexagesimales (0) o radianes (1). 
### 5 2 Coseno:
Se calcula el coseno del ángulo ingresado. Se le consulta previamente al usuario en qué sistema angular quiere ingresar este ángulo: grados sexagesimales (0) o radianes (1).
### 5 3 Tangente:
Se calcula la tangente del ángulo ingresado. Se le consulta previamente al usuario en qué sistema angular quiere ingresar este ángulo: grados sexagesimales (0) o radianes (1).
### 5 4 Arcoseno
Se calcula el arcoseno del número ingresado. Se le consulta previamente al usuario en qué sistema angular quiere la salida: grados sexagesimales (0) o radianes (1). La restricción es que el número ingresado debe estar entre -1 y 1.
### 5 5 Arcocoseno
Se calcula el arcocoseno del número ingresado. Se le consulta previamente al usuario en qué sistema angular quiere la salida: grados sexagesimales (0) o radianes (1). Existe la restricción de que el número ingresado debe estar entre -1 y 1.
### 5 6 Arcotangente:
Se calcula la arcotangente del número ingresado. Se le consulta previamente al usuario en qué sistema angular quiere la salida: grados sexagesimales (0) o radianes (1).
### 5 7 Logaritmo:
Se calcula el logaritmo de un número como argumento en una base específica. Al primer valor se le calcula el logaritmo en la base que indique segundo número ingresado. Se establecen restricciones para la base, estas son: que debe ser positiva y distinta de 1 y, adicionalmente, que el argumento debe ser positivo también.

### 5 8 Logaritmo natural:
Se calcula el logaritmo natural de un número como argumento. Se establece que el argumento debe ser positivo.


## 6 Prerrequisitos: 
Para poder usar la Calculadora Pythonista, es necesario ejecutarla en la consola de un intérprete de Python versión 3.7 y, como se indicó anteriormente, que estén instaladas las librerías de las funciones externas en el mismo directorio o ruta de acceso del programa principal.

## 7 Contribución: 
La estructura del código de la Calculadora Pythonista es muy simple, se basa en llamadas a funciones que se definen en librerías externas , lo que facilita implementar nuevas características, mejorando o agregando nuevas funciones a las librerías y darles cabida en la estructura del código del programa principal.  

## 8 Licencia: 
Este código es de licencia libre. Se puede utilizar y distribuir sin limitaciones.

## 9 Implementación:
Este proyecto se realizo en una modalidad cooperativa remota y se utilizaron dos repositorios locales, cada uno perteneciente a cada miembro del equipo (colaborador A y colaborador B). Todo el desarrollo fue basado en seguir los lineamientos de un flujo de trabajo de tipo GitFlow (rama main, hotfixes, release, develop, features). En la primera etapa se programaron las librerias que contienen las funciones que son llamadas desde el código principal. Las librerías *basicas.py* y *avanzadas.py*, fueron ensambladas en repositorios locales por cada integrante del equipo a través de ramas temporales de desarrollo de características (features). A se encargó, en primera instancia de *basicas.py*, y B de *avanzadas.py*. Se empujan estas versiones de las librerías al repositorio remoto interactuando en equipo en mejoras, correcciones y resolución de conflictos (por ejemplo *merge conflicts*). Después, en forma colaborativa, se desarrolló el código del programa principal *calculadora.py*. El archivo *gitflow.jpg* contiene un diagrama de flujo que ayuda a comprender mejor a las ramas involucradas y la forma en que éstas fueron fusionadas entre sí durante el desarrollo del proyecto.

## 10 Merge conflicts

Dado que en un principio ambos colaboradores trabajamos principalmente en archivos separados, los *merge conflicts* iban generándose sobre nuestras mismas modificaciones, por lo que inicialmente no interferíamos en el archivo que trabajaba el otro colaborador del proyecto. Es por esto que se generó un *merge conflict* más acorde a lo solicitado.

Cuando ya teníamos en la rama develop una versión del proyecto que podía ser enviada a la rama de release, hicimos la fusión de dichas ramas. Luego, desde la rama de release, comenzamos a editar simultáneamente el archivo README. Al hacer los commits comenzó el conflicto buscado, pues Github informó que el archivo había sido editado paralelamente por otro colaborador. Para solucionar esto, se tomó la opción de crear una nueva rama tipo "*patch*", con el objetivo de generar *pull request* que fusione esta rama auxiliar con release. Al hacer la pull request fue necesario solucionar el conflicto manualmente, es decir, se editó el archivo en la nube confirmando una nueva versión del mismo que pudiera ser fusionada en release. Al hacer esto, el otro colaborador tuvo un problema similar al intentar un nuevo commit, por lo que debió proceder con la misma estrategia recién comentada.

A continuación, se encuentran los SHA de las *pull request* mencionadas:

*  *pull request #44* : 7fc978fc26e86bf80105895fd844ebcacca7ce1c
*  *pull request #45* : 11379bf7917a059466abbb1f20b4f9b85801cbf6

## 11 Rastreo de autorías

Usando *git blame* se generaron 3 archivos de extensión *.txt* que contienen las autorías de cada linea de código de los archivos *.py* contenidos en el repositorio. Estos archivos son: *blame_basicas.txt*, *blame_avanzadas.txt* y *blame_calculadora.txt*.

## 12 Autores: 
Los autores de este código son estudiantes de la asignatura de Programación Avanzada del programa de Magíster en simulación computacional que dicta la Pontificia Universidad Católica de Valparaíso: Juan Venegas y Claudio Guzmán.

## 13 Estado del Proyecto: 
El proyecto está terminado, pero siempre disponible para aportes y modificaciones.

## 14 Agradecimientos: 
Agradecimientos a nuestro profesor Bady Gana por sus clases, tips y videos muy aclaradores sin los cuales hubiese sido muy difícil hacer este trabajo 

## 15 Notas de Versión (v4.0) : 

* Se incluye a la calculadora Pythonista con funcionamiento estable y debidamente testeada.
* Son corregidos algunos detalles finales en la documentación (principalmente README).
* Se incluye un diagrama del flujo GitFlow implementado en la elaboración del proyecto.