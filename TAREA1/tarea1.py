#ASIGNATURA: ESTRUCTURA DE DATOS 
#DOCENTE: ING. DANIEL VERA 
#ESTUDIANTE: DERICK VINCES RONQUILLO

#Clases y Colecciones (sin herencia)

#EJERCICIO 1: Validador de notas con promedio
#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista; (3) tenga método promedio() que retorne el promedio de notas almacenadas.

#1. Entender el problema
#Entrada: El usuario ingresa varias notas.
#Proceso: Se crea un objeto de la clase Calificador. Cada nota es validada; si está entre 0 y 100 se guarda en una lista interna. Luego se calcula el promedio de todas las notas válidas.
#Salida: Se muestra la lista de notas válidas y su promedio.

#2. Bosquejo a mano
# Crear la clase Calificador
# Crear una lista vacía para almacenar las notas
# Crear un método validar_nota(nota)
# Si la nota está entre 0 y 100:
#     Retornar True
# Si no:
#     Retornar False
# Crear un método cargar_notas(*args)
# Recorrer todas las notas recibidas
# Si la nota es válida:
#     Guardarla en la lista
# Retornar la lista
# Crear un método promedio()
# Si no hay notas:
#     Retornar 0
# Caso contrario:
#     Sumar todas las notas
#     Dividir entre la cantidad de notas
# Crear un objeto
# Cargar las notas
# Mostrar las notas válidas
# Mostrar el promedio

#3. Descubrir el patrón
# Se utiliza una lista porque permite almacenar múltiples notas.
# La validación se realiza en un método independiente para reutilizar el código.
# El promedio se obtiene sumando las notas y dividiendo entre la cantidad de elementos almacenados.

#4. Escribir código

class Calificador:

    def __init__(self):

        self.notas = []

    def validar_nota(self, nota):

        return 0 <= nota <= 100

    def cargar_notas(self, *args):

        for nota in args:

            if self.validar_nota(nota):

                self.notas.append(nota)

        return self.notas

    def promedio(self):

        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


estudiante = Calificador()

estudiante.cargar_notas(90, 80, 70, 105, -5)

print(estudiante.notas)
print(estudiante.promedio())

#5. Prueba de escritorio

# Datos ingresados:
# 90, 80, 70, 105, -5

# Inicio:
# self.notas = []

# Nota = 90
# validar_nota(90) → True
# self.notas = [90]

# Nota = 80
# validar_nota(80) → True
# self.notas = [90, 80]

# Nota = 70
# validar_nota(70) → True
# self.notas = [90, 80, 70]

# Nota = 105
# validar_nota(105) → False
# No se agrega

# Nota = -5
# validar_nota(-5) → False
# No se agrega

# Promedio:
# (90 + 80 + 70) / 3
# 240 / 3 = 80.0

# Salida:
# [90, 80, 70]
# 80.0

#EJERCICIO 2: Contador de palabras únicas

#1. Entender el problema
#Entrada: El usuario ingresa varias palabras.
#Proceso: Se crea una clase AnalizadorTexto que almacena las palabras en una lista para conservar el orden en que fueron agregadas y en un conjunto para evitar palabras repetidas. 
#Se crea un método para agregar una palabra, otro para contar cuántas palabras únicas existen y otro para agregar varias palabras reutilizando el método anterior.
#Salida: Se muestra la lista completa de palabras, el conjunto con palabras únicas y la cantidad de palabras sin repetir.

#2. Bosquejo a mano
# Crear una clase AnalizarTexto
# Crear una lista vacía para guardar palabras en orden
# Crear un conjunto vacío para guardar palabras únicas
# Crear método agregar_palabra(palabra)
#     Agregar palabra al conjunto
#     Agregar palabra a la lista
# Crear método contar_palabras_unicas()
#     Retornar la cantidad de elementos del conjunto
# Crear método agregar_multiples(*args)
#     Recorrer todas las palabras recibidas
#     Llamar al método agregar_palabra para cada una
# Crear un objeto de la clase
# Agregar varias palabras
# Mostrar resultados

#3. Descubrir el patrón
# Se utilizan dos estructuras de datos con diferentes funciones:
# La lista permite mantener el orden original de las palabras ingresadas.
# El conjunto permite almacenar únicamente valores sin repetir.
# Se reutiliza el método agregar_palabra dentro de agregar_multiples para evitar repetir código.

#4. Escribir código

class AnalizarTexto:
    def __init__(self):
        self.palabra_conjunto = set()
        self.palabra_lista = []

    def agregar_palabra(self, palabra):
        self.palabra_conjunto.add(palabra)
        self.palabra_lista.append(palabra)

    def contar_palabras_unicas(self):
        return len(self.palabra_conjunto)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

        return self.palabra_lista


texto = AnalizarTexto()

texto.agregar_multiples("hola", "python", "hola", "clase")

print(texto.palabra_lista)
print(texto.palabra_conjunto)
print(texto.contar_palabras_unicas())


#5. Prueba de escritorio

#Entrada:
# Palabras ingresadas:
# "hola", "python", "hola", "clase"

#Proceso:

# Primera palabra: "hola"
# Lista: ["hola"]
# Conjunto: {"hola"}

# Segunda palabra: "python"
# Lista: ["hola", "python"]
# Conjunto: {"hola", "python"}

# Tercera palabra: "hola"
# Lista: ["hola", "python", "hola"]
# Conjunto: {"hola", "python"}
# (No se agrega porque ya existe en el conjunto)

# Cuarta palabra: "clase"
# Lista: ["hola", "python", "hola", "clase"]
# Conjunto: {"hola", "python", "clase"}

#Salida:
# Lista de palabras:
# ["hola", "python", "hola", "clase"]

# Palabras únicas:
# {"hola", "python", "clase"}

# Cantidad de palabras únicas:
# 3

#EJERCICIO 3: Gestor de compras con totales

#1. Entender el problema
#Entrada: El usuario ingresa artículos con su nombre y precio.
#Proceso: Se crea una clase CarroCompras que utiliza un diccionario para guardar cada artículo como clave y su precio como valor. Luego se crean métodos para agregar artículos, sumar todos los precios y buscar artículos que estén dentro de un rango de precios.
#CAMBIO: Se utiliza un método separado para filtrar los artículos según un precio mínimo y máximo.
#Salida: Se muestra el total de todos los productos y los artículos que cumplen con el rango indicado.


#2. Bosquejo a mano
# Crear la clase CarroCompras
# Crear un constructor con un diccionario vacío
# Crear método agregar_articulo(nombre, precio)
# Guardar nombre como clave y precio como valor
# Crear método total_carrito()
# Obtener todos los valores del diccionario
# Sumar los precios
# Crear método articulos_por_rango(minimo, maximo)
# Crear una lista vacía
# Recorrer el diccionario con items()
# Comparar si el precio está dentro del rango
# Agregar el nombre del artículo a la lista
# Retornar la lista


#3. Descubrir el patrón
# Se utiliza un diccionario porque permite relacionar un artículo con su precio.
# La clave representa el nombre del producto y el valor representa su precio.
# Se utiliza values() para obtener únicamente los precios y poder sumarlos.
# Se utiliza items() para recorrer cada artículo junto con su precio y poder aplicar una condición de búsqueda.


#4. Escribir código

class CarroCompras: 
    def __init__(self): 
        self.productos = dict() 

    def agregar_articulo(self, nombre, precio): 
        self.productos[nombre] = precio 

    def total_carrito(self): 
        return sum(self.productos.values()) 

    def articulos_por_rango(self, minimo, maximo): 
        rango_precio = [] 

        for nombre, precio in self.productos.items(): 
            if minimo <= precio <= maximo: 
                rango_precio.append(nombre) 

        return rango_precio 


producto1 = CarroCompras()

producto1.agregar_articulo("Arroz", 45)
producto1.agregar_articulo("Laptop", 800)
producto1.agregar_articulo("Mouse", 20)

print(producto1.total_carrito())


#5. Prueba de escritorio

#Objeto creado:
#producto1 = CarroCompras()

#Diccionario inicial:
#{}

#Después de agregar artículos:

#agregar_articulo("Arroz", 45)
#{"Arroz": 45}

#agregar_articulo("Laptop", 800)
#{"Arroz": 45, "Laptop": 800}

#agregar_articulo("Mouse", 20)
#{"Arroz": 45, "Laptop": 800, "Mouse": 20}

#Ejecución del método total_carrito():

#Valores del diccionario:
#[45, 800, 20]

#Suma:
#45 + 800 + 20 = 865

#Salida:
#865

#EJERCICIO 4: Inversor de secuencias
#Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles)
#(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas y retorne un diccionario {lista_original: lista_invertida}.

#1. Entender el problema
#Entrada: El usuario ingresa una o varias listas que contienen elementos.
#Proceso: Se crea una clase InversorSecuencia con un método que invierte una lista manualmente usando ciclos, recorriendo sus posiciones desde el último elemento hasta el primero. Luego se crea otro método que recibe varias listas, reutiliza el método de inversión y guarda cada lista original junto con su versión invertida en un diccionario.
#CAMBIO: Se agrega un método para procesar múltiples listas utilizando el método invertir_lista() para evitar repetir código.
#Salida: Se muestra una lista invertida o un diccionario con varias listas y sus respectivas inversiones.


#2. Bosquejo a mano
# Crear clase InversorSecuencia
# Crear método invertir_lista(lista)
# Crear lista vacía para guardar resultado
# Recorrer la lista desde la última posición hasta la primera
# Agregar cada elemento a la nueva lista
# Retornar lista invertida
#
# Crear método invertir_multiples(*listas)
# Crear diccionario vacío
# Recorrer todas las listas recibidas
# Llamar al método invertir_lista()
# Guardar lista original como clave y lista invertida como valor
# Retornar diccionario


#3. Descubrir el patrón
# Se utiliza un recorrido con range() en orden inverso para acceder a las posiciones de la lista desde el último elemento hasta el primero.
# Se reutiliza el método invertir_lista() dentro de invertir_multiples() para evitar repetir la lógica de inversión.
# Se convierte la lista original en una tupla porque las listas no pueden ser claves de un diccionario, mientras que las tuplas sí.


#4. Escribir código

class InversorSecuencia:

    def invertir_lista(self, lista):

        lista_invertida = []

        for i in range(len(lista)-1, -1, -1):

            lista_invertida.append(lista[i])

        return lista_invertida


    def invertir_multiples(self, *listas):

        resultado = {}

        for lista in listas:

            invertida = self.invertir_lista(lista)

            resultado[tuple(lista)] = invertida

        return resultado

inversor = InversorSecuencia()


lista1 = [1, 2, 3, 4]

print(inversor.invertir_lista(lista1))

resultado = inversor.invertir_multiples(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(resultado)


#5. Prueba de escritorio

#Objeto creado:
#inversor = InversorSecuencia()

#Prueba del método invertir_lista():

#Lista inicial:
#[1, 2, 3, 4]

#Recorrido:
#i = 3 → lista[3] = 4
#i = 2 → lista[2] = 3
#i = 1 → lista[1] = 2
#i = 0 → lista[0] = 1

#Lista invertida:
#[4, 3, 2, 1]


#Prueba del método invertir_multiples():

#Listas recibidas:
#([1,2,3], [4,5,6], [7,8,9])

#Primera iteración:
#Lista original: [1,2,3]
#Invertida: [3,2,1]
#Diccionario:
#{(1,2,3): [3,2,1]}


#Segunda iteración:
#Lista original: [4,5,6]
#Invertida: [6,5,4]
#Diccionario:
#{(1,2,3): [3,2,1], (4,5,6): [6,5,4]}


#Tercera iteración:
#Lista original: [7,8,9]
#Invertida: [9,8,7]


#Salida final:

#{(1,2,3): [3,2,1], (4,5,6): [6,5,4], (7,8,9): [9,8,7]}
    
#EJERCICIO 5: Detector de números pares e impares
# Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False
#(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par
#(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).   

#1. Entender el problema
#Entrada: El usuario ingresa varios números.
#Proceso: Se crea una clase AnalizarNumeros que permite verificar si un número es par o impar mediante el método es_par(). Luego, el método separar() recibe varios números, reutiliza es_par() y los clasifica dentro de un diccionario con dos listas: pares e impares. Finalmente, el método cantidad_pares_impares() cuenta cuántos números pares e impares existen.
#CAMBIO: Se agregan atributos internos self.pares y self.impares para almacenar los números clasificados y poder utilizarlos en otros métodos de la clase.
#Salida: Se muestra el diccionario con los números separados y una tupla con la cantidad de pares e impares.


#2. Bosquejo a mano
# Crear clase AnalizarNumeros
# Crear constructor con listas vacías para pares e impares
# Crear método es_par(numero)
# Verificar si el número es divisible entre 2
# Retornar True si es par y False si es impar
#
# Crear método separar(*numeros)
# Crear diccionario con listas pares e impares
# Recorrer todos los números recibidos
# Llamar al método es_par()
# Si es par:
#     Agregar a lista de pares
# Si es impar:
#     Agregar a lista de impares
# Retornar diccionario
#
# Crear método cantidad_pares_impares()
# Contar elementos de cada lista
# Retornar una tupla con ambas cantidades


#3. Descubrir el patrón
# Se utiliza un método separado es_par() para reutilizar la lógica de comprobación y evitar repetir código.
# Se utilizan listas para almacenar los números pares e impares.
# Se utiliza un diccionario porque permite organizar la información mediante claves: "pares" e "impares".
# Se utilizan atributos con self para conservar los datos y poder acceder a ellos desde otros métodos.


#4. Escribir código

class AnalizarNumeros:

    def __init__(self):
        self.pares = []
        self.impares = []


    def es_par(self, numero):

        return numero % 2 == 0


    def separar(self, *numeros):

        diccionario = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:

            if self.es_par(numero):

                diccionario["pares"].append(numero)
                self.pares.append(numero)

            else:

                diccionario["impares"].append(numero)
                self.impares.append(numero)

        return diccionario


    def cantidad_pares_impares(self):

        return len(self.pares), len(self.impares)



# Parámetros de prueba

analizador = AnalizarNumeros()

resultado = analizador.separar(10, 15, 22, 7, 30, 41, 8)

print(resultado)

print(analizador.cantidad_pares_impares())


#5. Prueba de escritorio

#Objeto creado:
#analizador = AnalizarNumeros()

#Listas iniciales:
#self.pares = []
#self.impares = []


#Prueba del método separar():

#Datos ingresados:
#10, 15, 22, 7, 30, 41, 8


#Primera iteración:
#Número: 10
#10 % 2 == 0 → True
#Se agrega a pares

#pares = [10]


#Segunda iteración:
#Número: 15
#15 % 2 == 0 → False
#Se agrega a impares

#impares = [15]


#Tercera iteración:
#Número: 22
#22 % 2 == 0 → True
#pares = [10, 22]


#Cuarta iteración:
#Número: 7
#7 % 2 == 0 → False
#impares = [15, 7]


#Quinta iteración:
#Número: 30
#30 % 2 == 0 → True
#pares = [10, 22, 30]


#Sexta iteración:
#Número: 41
#41 % 2 == 0 → False
#impares = [15, 7, 41]


#Séptima iteración:
#Número: 8
#8 % 2 == 0 → True
#pares = [10, 22, 30, 8]


#Resultado del diccionario:

#{
#"pares": [10, 22, 30, 8],
#"impares": [15, 7, 41]
#}


#Prueba del método cantidad_pares_impares():

#Cantidad de pares:
#4

#Cantidad de impares:
#3


#Salida final:

#{
#"pares": [10, 22, 30, 8],
#"impares": [15, 7, 41]
#}

#(4, 3)

#EJERCICIO 6: Estadísticas de temperatura
#Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista
#(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas
#(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.

#1. Entender el problema
#Entrada: El usuario ingresa una o varias temperaturas.
#Proceso: Se crea una clase GestorTemperatura que almacena temperaturas en una lista. 
#El método registrar_temperatura() agrega una temperatura individual. 
#El método registrar_multiples() recibe varias temperaturas y reutiliza registrar_temperatura().
#Los métodos minima(), maxima() y promedio() trabajan con la lista almacenada para obtener diferentes resultados.
#Salida: Se muestran las temperaturas registradas, la temperatura mínima, máxima y el promedio.


#2. Bosquejo a mano
# Crear clase GestorTemperatura
# Crear constructor con una lista vacía para temperaturas
#
# Crear método registrar_temperatura(temp)
# Agregar temperatura a la lista
#
# Crear método minima()
# Obtener el valor más pequeño de la lista
#
# Crear método maxima()
# Obtener el valor más grande de la lista
#
# Crear método promedio()
# Sumar temperaturas y dividir entre cantidad de temperaturas
#
# Crear método registrar_multiples(*temps)
# Recorrer todas las temperaturas recibidas
# Llamar al método registrar_temperatura()
# Guardar todas las temperaturas


#3. Descubrir el patrón
# Se utiliza una lista porque se necesita almacenar varios valores.
# Se utiliza self para mantener las temperaturas guardadas dentro del objeto.
# Se reutiliza registrar_temperatura() dentro de registrar_multiples() para evitar repetir código.
# Los métodos minima(), maxima() y promedio() trabajan sobre la misma lista creada en el constructor.


#4. Escribir código

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []


    def registrar_temperatura(self, temp):

        self.temperaturas.append(temp)


    def minima(self):

        return min(self.temperaturas)


    def maxima(self):

        return max(self.temperaturas)


    def promedio(self):

        return sum(self.temperaturas) / len(self.temperaturas)


    def registrar_multiples(self, *temps):

        for temp in temps:

            self.registrar_temperatura(temp)



# Parámetros de prueba

clima = GestorTemperatura()

clima.registrar_temperatura(25)

clima.registrar_multiples(30, 18, 22, 27, 35)


print(clima.temperaturas)

print("Temperatura mínima:", clima.minima())

print("Temperatura máxima:", clima.maxima())

print("Promedio:", clima.promedio())


#5. Prueba de escritorio

#Objeto creado:
#clima = GestorTemperatura()


#Lista inicial:
#self.temperaturas = []


#Registro individual:

#Se ingresa:
#25

#Lista:
#[25]


#Registro múltiple:

#Datos recibidos:
#(30, 18, 22, 27, 35)


#Primera iteración:
#temp = 30
#Lista:
#[25, 30]


#Segunda iteración:
#temp = 18
#Lista:
#[25, 30, 18]


#Tercera iteración:
#temp = 22
#Lista:
#[25, 30, 18, 22]


#Cuarta iteración:
#temp = 27
#Lista:
#[25, 30, 18, 22, 27]


#Quinta iteración:
#temp = 35
#Lista:
#[25, 30, 18, 22, 27, 35]


#Prueba de métodos:

#Mínima:
#min([25,30,18,22,27,35])
#Resultado:
#18


#Máxima:
#max([25,30,18,22,27,35])
#Resultado:
#35


#Promedio:

#sum([25,30,18,22,27,35]) = 157

#cantidad = 6

#157 / 6 = 26.16


#Salida final:

#[25, 30, 18, 22, 27, 35]

#Temperatura mínima: 18

#Temperatura máxima: 35

#Promedio: 26.16

#EJERCICIO 7: Mapeador de edades 
#Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario 
#(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥ 
#(3) tenga método edad_promedio() que retorne el promedio de edades. 


#1. Entender el problema
#Entrada: El usuario ingresa el nombre y la edad de una o varias personas.
#Proceso: Se crea una clase que almacena personas en una lista de diccionarios.
#Cada diccionario guarda el nombre y la edad de una persona.
#Se puede obtener una lista de personas mayores a una edad indicada y calcular el promedio de edades.
#Salida: Se muestran las personas registradas, los nombres de las personas mayores a una edad mínima y el promedio de edades.


#2. Bosquejo a mano
#Crear la clase GestorPersonas
#Crear un constructor con una lista vacía
#
#Crear método agregar_personas(nombre, edad)
#Crear un diccionario con nombre y edad
#Guardar el diccionario en la lista
#
#Crear método personas_mayores(edad_minima)
#Recorrer todas las personas
#Comparar la edad con la edad mínima
#Guardar los nombres que cumplen la condición
#
#Crear método edad_promedio()
#Recorrer todas las personas
#Sumar las edades
#Dividir la suma para la cantidad de personas


#3. Descubrir el patrón
#Se utiliza una lista para almacenar varias personas.
#Cada persona se representa mediante un diccionario con nombre y edad.
#Se utiliza un recorrido con for para acceder a cada persona.
#Se utilizan listas para guardar los nombres filtrados.
#El promedio se obtiene sumando todas las edades y dividiendo para la cantidad de personas.


#4. Escribir código

class GestorPersonas:

    def __init__(self):
        self.edades = []

    def agregar_personas(self, nombre, edad):

        personas = {
            "nombre": "",
            "edad": 0
        }

        personas["nombre"] = nombre
        personas["edad"] = edad

        self.edades.append(personas)

    def personas_mayores(self, edad_minima):

        mayores = []

        for persona in self.edades:

            if persona["edad"] >= edad_minima:

                mayores.append(persona["nombre"])

        return mayores

    def edad_promedio(self):

        if len(self.edades) == 0:
            return 0

        suma = 0

        for persona in self.edades:

            suma += persona["edad"]

        return suma / len(self.edades)


#Parámetros de prueba

gestor = GestorPersonas()

gestor.agregar_personas("Derick", 19)
gestor.agregar_personas("Ana", 22)
gestor.agregar_personas("Luis", 17)
gestor.agregar_personas("Carlos", 25)

print(gestor.edades)

print(gestor.personas_mayores(18))

print(gestor.edad_promedio())


#5. Prueba de escritorio

#Objeto creado:
#gestor = GestorPersonas()

#Lista inicial:
#self.edades = []

#Se agrega:
#("Derick",19)

#Lista:
#[{"nombre":"Derick","edad":19}]

#Se agrega:
#("Ana",22)

#Lista:
#[{"nombre":"Derick","edad":19},
# {"nombre":"Ana","edad":22}]

#Se agrega:
#("Luis",17)

#Lista:
#[{"nombre":"Derick","edad":19},
# {"nombre":"Ana","edad":22},
# {"nombre":"Luis","edad":17}]

#Se agrega:
#("Carlos",25)

#Lista final:
#[{"nombre":"Derick","edad":19},
# {"nombre":"Ana","edad":22},
# {"nombre":"Luis","edad":17},
# {"nombre":"Carlos","edad":25}]

#Método personas_mayores(18)

#Primera persona:
#19 >= 18
#Se agrega "Derick"

#Segunda persona:
#22 >= 18
#Se agrega "Ana"

#Tercera persona:
#17 >= 18
#No se agrega

#Cuarta persona:
#25 >= 18
#Se agrega "Carlos"

#Resultado:
#["Derick","Ana","Carlos"]

#Método edad_promedio()

#suma = 0

#19 + 22 + 17 + 25 = 83

#Cantidad de personas = 4

#83 / 4 = 20.75

#Salida final:

#[{'nombre': 'Derick', 'edad': 19},
# {'nombre': 'Ana', 'edad': 22},
# {'nombre': 'Luis', 'edad': 17},
# {'nombre': 'Carlos', 'edad': 25}]

#['Derick', 'Ana', 'Carlos']

#20.75


            