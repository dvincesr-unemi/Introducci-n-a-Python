#ASIGNATURA: ESTRUCTURA DE DATOS 
#DOCENTE: ING. DANIEL VERA 
#ESTUDIANTE: DERICK VINCES RONQUILLO

#Clases y Colecciones (sin herencia)

#EJERCICIO 1: Validador de notas con promedio
#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario
#(2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista
#(3) tenga método promedio() que retorne el promedio de notas almacenadas.

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

# EJERCICIO:
# Crear una clase Ventas que almacene únicamente ventas mayores que 0.
# La clase debe tener los siguientes métodos:
# - validar(monto)
# - agregar_ventas(*ventas)
# - total()
# - promedio()
# - venta_mayor()
# - venta_menor()
#
# Crear un objeto de la clase, agregar las ventas:
# 120, 250, -40, 90, 600 y 0.
# Finalmente mostrar:
# - Las ventas válidas.
# - El total vendido.
# - El promedio.
# - La venta mayor.
# - La venta menor.

# Bosquejo a mano
# Crear la clase Ventas
# Crear una lista vacía para almacenar las ventas
# Crear un método validar(monto)
# Si el monto es mayor que 0:
#     Retornar True
# Si no:
#     Retornar False
# Crear un método agregar_ventas(*ventas)
# Recorrer todas las ventas recibidas
# Si la venta es válida:
#     Guardarla en la lista
# Retornar la lista
# Crear un método total()
# Si no existen ventas:
#     Retornar 0
# Caso contrario:
#     Retornar la suma de todas las ventas
# Crear un método promedio()
# Si no existen ventas:
#     Retornar 0
# Caso contrario:
#     Retornar el total dividido para la cantidad de ventas
# Crear un método venta_mayor()
# Si no existen ventas:
#     Retornar None
# Caso contrario:
#     Retornar la venta más alta
# Crear un método venta_menor()
# Si no existen ventas:
#     Retornar None
# Caso contrario:
#     Retornar la venta más baja
# Crear un objeto
# Agregar varias ventas
# Mostrar las ventas válidas
# Mostrar el total
# Mostrar el promedio
# Mostrar la venta mayor
# Mostrar la venta menor

class Ventas:

    def __init__(self):
        self.ventas = []

    def validar(self, monto):
        return monto > 0

    def agregar_ventas(self, *ventas):

        for venta in ventas:

            if self.validar(venta):
                self.ventas.append(venta)

        return self.ventas

    def total(self):

        if len(self.ventas) == 0:
            return 0

        return sum(self.ventas)

    def promedio(self):

        if len(self.ventas) == 0:
            return 0

        return self.total() / len(self.ventas)

    def venta_mayor(self):

        if len(self.ventas) == 0:
            return None

        return max(self.ventas)

    def venta_menor(self):

        if len(self.ventas) == 0:
            return None

        return min(self.ventas)


ventas = Ventas()

ventas.agregar_ventas(120, 250, -40, 90, 600, 0)

print("Ventas válidas:", ventas.ventas)
print("Total vendido:", ventas.total())
print("Promedio:", ventas.promedio())
print("Venta mayor:", ventas.venta_mayor())
print("Venta menor:", ventas.venta_menor())

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

# EJERCICIO:
# Crear una clase Encuesta que almacene las respuestas de varias personas.
#
# Métodos:
# - agregar_respuesta(respuesta)
# - agregar_varias(*respuestas)
# - respuesta_mas_comun()
# - cantidad_respuestas()
#
# Crear un objeto y agregar las respuestas:
# "Sí", "No", "Sí", "Sí", "No", "Tal vez"
#
# Finalmente mostrar:
# - Todas las respuestas.
# - La cantidad de respuestas.
# - La respuesta que más se repitió.

# Bosquejo a mano
# Crear la clase Encuesta
# Crear una lista vacía para almacenar las respuestas
# Crear un método agregar_respuesta(respuesta)
# Agregar la respuesta a la lista
# Crear un método agregar_varias(*respuestas)
# Recorrer todas las respuestas recibidas
# Llamar al método agregar_respuesta()
# Retornar la lista
# Crear un método cantidad_respuestas()
# Retornar la cantidad de respuestas
# Crear un método respuesta_mas_comun()
# Crear un diccionario vacío
# Recorrer la lista de respuestas
# Contar cuántas veces aparece cada respuesta
# Retornar la respuesta con mayor frecuencia
# Crear un objeto
# Agregar varias respuestas
# Mostrar la lista
# Mostrar la cantidad de respuestas
# Mostrar la respuesta más común

class Encuesta:

    def __init__(self):
        self.respuestas = []

    def agregar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def agregar_varias(self, *respuestas):

        for respuesta in respuestas:
            self.agregar_respuesta(respuesta)

        return self.respuestas

    def cantidad_respuestas(self):
        return len(self.respuestas)

    def respuesta_mas_comun(self):

        contador = {}

        for respuesta in self.respuestas:
            contador[respuesta] = contador.get(respuesta, 0) + 1

        return max(contador, key=contador.get)


encuesta = Encuesta()

encuesta.agregar_varias("Sí", "No", "Sí", "Sí", "No", "Tal vez")

print(encuesta.respuestas)
print(encuesta.cantidad_respuestas())
print(encuesta.respuesta_mas_comun())


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

#EJERCICIO 8: Asignador de equipos

#Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario

#(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo

#(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.


#1. Entender el problema
#Entrada: El usuario ingresa el nombre de uno o varios equipos y luego agrega jugadores a cada equipo.
#Proceso: Se crea una clase que almacena equipos en un diccionario.
#Cada clave del diccionario es el nombre de un equipo y su valor es una lista de jugadores.
#Se puede agregar jugadores y determinar cuál equipo tiene más integrantes.
#Salida: Se muestran los equipos registrados y el nombre del equipo con mayor cantidad de jugadores.


#2. Bosquejo a mano
#Crear la clase Equipos
#Crear un constructor con un diccionario vacío
#
#Crear método crear_equipo(nombre_equipo)
#Crear una clave en el diccionario
#Asignarle una lista vacía
#
#Crear método agregar_jugador(equipo, jugador)
#Buscar el equipo en el diccionario
#Agregar el jugador a la lista correspondiente
#
#Crear método equipo_mayor_integrantes()
#Recorrer todos los equipos
#Comparar la cantidad de jugadores
#Guardar el equipo con mayor cantidad
#Retornar su nombre


#3. Descubrir el patrón
#Se utiliza un diccionario donde la clave es el nombre del equipo.
#Cada valor del diccionario es una lista de jugadores.
#Se utiliza append() para agregar jugadores a la lista.
#Se utiliza len() para conocer la cantidad de integrantes de cada equipo.
#Se recorre el diccionario con items() para obtener la clave y el valor.


#4. Escribir código

class Equipos:

    def __init__(self):

        self.equipos = {}

    def crear_equipo(self, equipo):

        self.equipos[equipo] = []

    def agregar_jugador(self, equipo, jugador):

        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):

        mayor = ""
        cantidad = 0

        for equipo, jugadores in self.equipos.items():

            if len(jugadores) > cantidad:

                cantidad = len(jugadores)

                mayor = equipo

        return mayor


#Parámetros de prueba

liga = Equipos()

liga.crear_equipo("Barcelona")
liga.crear_equipo("Emelec")
liga.crear_equipo("Liga")

liga.agregar_jugador("Barcelona", "Derick")
liga.agregar_jugador("Barcelona", "Luis")

liga.agregar_jugador("Emelec", "Ana")

liga.agregar_jugador("Liga", "Carlos")
liga.agregar_jugador("Liga", "Pedro")
liga.agregar_jugador("Liga", "Juan")

print(liga.equipos)

print(liga.equipo_mayor_integrantes())


#5. Prueba de escritorio

#Objeto creado:
#liga = Equipos()

#Diccionario inicial:
#{}

#Se crea:
#"Barcelona"

#Diccionario:
#{
#    "Barcelona": []
#}

#Se crea:
#"Emelec"

#Diccionario:
#{
#    "Barcelona": [],
#    "Emelec": []
#}

#Se crea:
#"Liga"

#Diccionario:
#{
#    "Barcelona": [],
#    "Emelec": [],
#    "Liga": []
#}

#Se agregan jugadores

#Barcelona:
#["Derick", "Luis"]

#Emelec:
#["Ana"]

#Liga:
#["Carlos", "Pedro", "Juan"]

#Diccionario final:

#{
#    "Barcelona": ["Derick", "Luis"],
#    "Emelec": ["Ana"],
#    "Liga": ["Carlos", "Pedro", "Juan"]
#}

#Método equipo_mayor_integrantes()

#Barcelona -> 2 jugadores

#Emelec -> 1 jugador

#Liga -> 3 jugadores

#El equipo con mayor cantidad de integrantes es:

#"Liga"

#Salida final:

#{
#    'Barcelona': ['Derick', 'Luis'],
#    'Emelec': ['Ana'],
#    'Liga': ['Carlos', 'Pedro', 'Juan']
#}

#Liga

#Ejercicio 9: Validador de caracteres 
#Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal 
#(2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
#(3) tenga atributo que guarde el texto más largo analizado. 


#1. Entender el problema

#Entrada:
#El usuario ingresa un texto que contiene letras, vocales, consonantes y números.

#Proceso:
#Crear una clase que analice caracteres.
#Se utiliza un método para comprobar si un carácter es vocal.
#Se recorre el texto completo para contar vocales, consonantes y dígitos.
#Se guarda el texto con mayor longitud analizado.

#Salida:
#Retornar un diccionario con la cantidad de vocales, consonantes y dígitos.
#Mostrar cuál fue el texto más largo analizado.


#2. Bosquejo a mano

#Crear clase AnalizadorString

#Crear constructor:
#Crear atributo texto_mas_largo vacío.

#Crear método solo_vocales(letra):
#Crear una cadena con vocales.
#Comprobar si la letra pertenece a esa cadena.
#Retornar True o False.

#Crear método contar_por_tipo(texto):
#Crear diccionario con contadores en cero.
#Recorrer cada letra del texto.
#Si es vocal aumentar contador de vocales.
#Si es número aumentar contador de dígitos.
#Si es letra aumentar contador de consonantes.
#Comparar la longitud del texto actual con el texto más largo guardado.
#Retornar diccionario.


#3. Descubrir el patrón

#Se utiliza un ciclo for para recorrer cadenas.
#Cada carácter es analizado individualmente.
#Se reutiliza un método creado anteriormente mediante self.
#Se utilizan métodos propios de Python:
#.isdigit() para comprobar números.
#.isalpha() para comprobar letras.
#Se usa len() para comparar tamaños de textos.


#4. Escribir código

class AnalizadorString:

    def __init__(self):

        self.texto_mas_largo = ""


    def solo_vocales(self, letra):

        vocales = "aeiouAEIOU"

        return letra in vocales


    def contar_por_tipo(self, texto):

        contador = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for letra in texto:

            if self.solo_vocales(letra):

                contador["vocales"] += 1

            elif letra.isdigit():

                contador["digitos"] += 1

            elif letra.isalpha():

                contador["consonantes"] += 1


        if len(texto) > len(self.texto_mas_largo):

            self.texto_mas_largo = texto


        return contador



#Parámetros de prueba

analizador = AnalizadorString()


texto1 = "Hola123"

texto2 = "Programacion2026"

texto3 = "Python"


print(analizador.contar_por_tipo(texto1))

print(analizador.contar_por_tipo(texto2))

print(analizador.contar_por_tipo(texto3))


print(analizador.texto_mas_largo)



#5. Prueba de escritorio


#Objeto creado:

#analizador = AnalizadorString()


#Atributo inicial:

#texto_mas_largo = ""


#Primer texto:

#texto1 = "Hola123"


#Recorrido:

#H -> consonante
#o -> vocal
#l -> consonante
#a -> vocal
#1 -> dígito
#2 -> dígito
#3 -> dígito


#Resultado:

#{
# "vocales": 2,
# "consonantes": 2,
# "digitos": 3
#}


#Como "Hola123" tiene más longitud que "":
#texto_mas_largo = "Hola123"



#Segundo texto:

#texto2 = "Programacion2026"


#Se cuentan:

#vocales = 6
#consonantes = 6
#digitos = 4


#Como es más largo que "Hola123":

#texto_mas_largo = "Programacion2026"



#Tercer texto:

#texto3 = "Python"


#Se cuentan:

#vocales = 1
#consonantes = 5
#digitos = 0


#No reemplaza el texto más largo porque es menor.


#Salida final:

#{
# 'vocales': 2,
# 'consonantes': 2,
# 'digitos': 3
#}

#{
# 'vocales': 6,
# 'consonantes': 6,
# 'digitos': 4
#}

#{
# 'vocales': 1,
# 'consonantes': 5,
# 'digitos': 0
#}

#Programacion2026

#EJERCICIO 10: Gestor de tareas con prioridad
#Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad)
#(2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta
#(3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.


#1. Entender el problema

#Entrada:
#El usuario ingresa una descripción y una prioridad (Alta, Media o Baja).

#Proceso:
#Crear una clase que almacene tareas en una lista de tuplas.
#Agregar tareas.
#Buscar las tareas con prioridad alta.
#Eliminar una tarea mediante su descripción.

#Salida:
#Mostrar las tareas prioritarias.
#Eliminar una tarea si existe.


#2. Bosquejo a mano

#Crear clase Tareas.

#Crear constructor:
#Crear una lista vacía para almacenar las tuplas.

#Crear método agregar_tarea():
#Crear una tupla (descripcion, prioridad).
#Agregar la tupla a la lista.

#Crear método tareas_prioritarias():
#Crear una lista vacía.
#Recorrer todas las tareas.
#Si la prioridad es "Alta", guardar la descripción.
#Si no existen tareas altas, retornar un mensaje.
#Retornar la lista.

#Crear método eliminar_completada():
#Recorrer todas las tuplas.
#Comparar la descripción.
#Si coincide, eliminar la tupla.
#Retornar True.
#Si no existe, retornar False.


#3. Descubrir el patrón

#Se utiliza una lista para almacenar tuplas.
#Cada tupla contiene:
#(descripcion, prioridad)

#Se recorre la lista con:

#for descripcion, prioridad in self.lista_tuplas

#Se utiliza append() para agregar tareas.
#Se utiliza remove() para eliminar tareas.
#Se utiliza lower() para comparar textos sin importar mayúsculas.


#4. Escribir código

class Tareas:

    def __init__(self):

        self.lista_tuplas = []


    def agregar_tarea(self, descripcion, prioridad):

        tarea = (descripcion, prioridad)

        self.lista_tuplas.append(tarea)


    def tareas_prioritarias(self):

        prioritarias = []

        for descripcion, prioridad in self.lista_tuplas:

            if prioridad.lower() == "alta":

                prioritarias.append(descripcion)

        if len(prioritarias) == 0:

            return "No hay actividades con prioridad alta registradas"

        return prioritarias


    def eliminar_completada(self, descripcion):

        for desc, prioridad in self.lista_tuplas:

            if desc == descripcion:

                self.lista_tuplas.remove((desc, prioridad))

                return True

        return False


#Parámetros de prueba

tareas = Tareas()

tareas.agregar_tarea("Estudiar Python", "Alta")
tareas.agregar_tarea("Comprar pan", "Baja")
tareas.agregar_tarea("Hacer deberes", "Media")
tareas.agregar_tarea("Preparar examen", "Alta")

print(tareas.lista_tuplas)

print(tareas.tareas_prioritarias())

print(tareas.eliminar_completada("Comprar pan"))

print(tareas.lista_tuplas)

print(tareas.eliminar_completada("Ir al cine"))


#5. Prueba de escritorio

#Objeto creado:

#tareas = Tareas()

#Lista inicial:

#[]


#Agregar tareas:

#("Estudiar Python", "Alta")
#("Comprar pan", "Baja")
#("Hacer deberes", "Media")
#("Preparar examen", "Alta")

#La lista queda:

#[
# ("Estudiar Python", "Alta"),
# ("Comprar pan", "Baja"),
# ("Hacer deberes", "Media"),
# ("Preparar examen", "Alta")
#]


#Método tareas_prioritarias()

#Recorrido:

#("Estudiar Python","Alta") -> Se agrega.
#("Comprar pan","Baja") -> No se agrega.
#("Hacer deberes","Media") -> No se agrega.
#("Preparar examen","Alta") -> Se agrega.

#Resultado:

#["Estudiar Python", "Preparar examen"]


#Método eliminar_completada("Comprar pan")

#Recorrido:

#("Estudiar Python","Alta") -> No coincide.
#("Comprar pan","Baja") -> Coincide.

#Se elimina la tupla.

#Retorna:

#True


#La lista queda:

#[
# ("Estudiar Python", "Alta"),
# ("Hacer deberes", "Media"),
# ("Preparar examen", "Alta")
#]


#Método eliminar_completada("Ir al cine")

#No encuentra la tarea.

#Retorna:

#False

#EJERCICIO 11: Contador de frecuencia
#Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones
#(2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia
#(3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.


#1. Entender el problema

#Entrada:
#El usuario ingresa varios elementos.

#Proceso:
#Guardar los elementos en un diccionario contando cuántas veces aparece cada uno.
#Encontrar el elemento con mayor frecuencia.
#Consultar cuántas veces aparece un elemento específico.

#Salida:
#Mostrar el diccionario de frecuencias.
#Mostrar el elemento más frecuente.
#Mostrar la frecuencia de un elemento.


#2. Bosquejo a mano

#Crear clase ContadorFrecuencia.

#Crear constructor:
#Crear un diccionario vacío.

#Crear método agregar_elemento():
#Verificar si el elemento ya existe.
#Si existe, aumentar su contador.
#Si no existe, agregarlo con valor 1.

#Crear método elemento_mas_frecuente():
#Buscar la clave con el mayor valor del diccionario.

#Crear método frecuencia_elemento():
#Si el elemento existe, retornar su frecuencia.
#Si no existe, retornar 0.


#3. Descubrir el patrón

#Se utiliza un diccionario.

#Clave -> Elemento.
#Valor -> Cantidad de veces que aparece.

#Si la clave existe:
#Se incrementa su contador.

#Si no existe:
#Se crea con valor 1.

#Para encontrar el elemento más frecuente se utiliza:

#max(diccionario, key=diccionario.get)


#4. Escribir código

class ContadorFrecuencia:

    def __init__(self):

        self.frecuencias = {}

    def agregar_elemento(self, elemento):

        if elemento in self.frecuencias:

            self.frecuencias[elemento] += 1

        else:

            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):

        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):

        if elemento in self.frecuencias:

            return self.frecuencias[elemento]

        return 0


#Parámetros de prueba

contador = ContadorFrecuencia()

contador.agregar_elemento("manzana")
contador.agregar_elemento("pera")
contador.agregar_elemento("manzana")
contador.agregar_elemento("uva")
contador.agregar_elemento("manzana")
contador.agregar_elemento("pera")

print(contador.frecuencias)

print(contador.elemento_mas_frecuente())

print(contador.frecuencia_elemento("manzana"))

print(contador.frecuencia_elemento("pera"))

print(contador.frecuencia_elemento("naranja"))


#5. Prueba de escritorio

#Objeto creado:

#contador = ContadorFrecuencia()

#Diccionario inicial:

#{}


#Agregar "manzana"

#{
#   "manzana": 1
#}


#Agregar "pera"

#{
#   "manzana": 1,
#   "pera": 1
#}


#Agregar "manzana"

#{
#   "manzana": 2,
#   "pera": 1
#}


#Agregar "uva"

#{
#   "manzana": 2,
#   "pera": 1,
#   "uva": 1
#}


#Agregar "manzana"

#{
#   "manzana": 3,
#   "pera": 1,
#   "uva": 1
#}


#Agregar "pera"

#{
#   "manzana": 3,
#   "pera": 2,
#   "uva": 1
#}


#Método elemento_mas_frecuente()

#Compara los valores del diccionario.

#manzana -> 3
#pera -> 2
#uva -> 1

#Retorna:

#"manzana"


#Método frecuencia_elemento("manzana")

#Retorna:

#3


#Método frecuencia_elemento("pera")

#Retorna:

#2


#Método frecuencia_elemento("naranja")

#Como no existe en el diccionario:

#Retorna:

#0

#EJERCICIO 12: Selector de rango con tuplas
#Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango
#(2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.


#1. Entender el problema

#Entrada:
#Dos números para crear un rango.
#Varias tuplas que contienen inicio y fin de diferentes rangos.

#Proceso:
#Crear una tupla con números dentro del rango indicado.
#Recorrer varios rangos.
#Unir todos los números en un conjunto para eliminar repetidos.

#Salida:
#Retornar una tupla con un rango.
#Retornar una lista con todos los elementos sin duplicados.


#2. Bosquejo a mano

#Crear clase SelectorRango.

#Método crear_rango():
#Recibir inicio y fin.
#Usar range().
#Convertir el resultado en una tupla.

#Método elementos_en_multiples_rangos():
#Crear un conjunto vacío.
#Recorrer cada tupla recibida.
#Separar inicio y fin.
#Crear números del rango.
#Agregar números al conjunto.
#Convertir conjunto en lista y retornar.


#3. Descubrir el patrón

#Se utiliza una tupla porque los rangos recibidos tienen una estructura fija:

#(inicio, fin)

#Se utiliza *rangos porque se reciben varias tuplas.

#Ejemplo:

#(1,5), (4,8), (10,12)

#Se usa set porque no permite elementos repetidos.

#Ejemplo:

#{1,2,3,4,5,6,7,8}


#4. Escribir código

class SelectorRango:

    def crear_rango(self, inicio, fin):

        return tuple(range(inicio, fin + 1))


    def elementos_en_multiples_rangos(self, *rangos):

        conjunto = set()

        for inicio, fin in rangos:

            for numero in range(inicio, fin + 1):

                conjunto.add(numero)

        return list(conjunto)



#Parámetros de prueba

selector = SelectorRango()


print(selector.crear_rango(1, 5))


resultado = selector.elementos_en_multiples_rangos(
    (1, 5),
    (4, 8),
    (10, 12)
)


print(resultado)



#5. Prueba de escritorio

#Objeto creado:

#selector = SelectorRango()


#Método crear_rango(1,5)

#Inicio:
#1

#Fin:
#5


#range(1,6) genera:

#1,2,3,4,5


#Resultado:

#(1,2,3,4,5)



#Método elementos_en_multiples_rangos()

#Datos recibidos:

#(1,5)
#(4,8)
#(10,12)


#Primer recorrido:

#inicio = 1
#fin = 5

#Agrega:

#1,2,3,4,5


#Segundo recorrido:

#inicio = 4
#fin = 8

#Agrega:

#4,5,6,7,8


#El set elimina repetidos:

#1,2,3,4,5,6,7,8


#Tercer recorrido:

#inicio = 10
#fin = 12

#Agrega:

#10,11,12


#Conjunto final:

#{1,2,3,4,5,6,7,8,10,11,12}


#Retorna lista:

#[1,2,3,4,5,6,7,8,10,11,12]

#EJERCICIO 14: Combinador de listas
#Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas
#(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.


#1. Entender el problema

#Entrada:
#Dos listas para combinar.
#Varias listas para intercalar.

#Proceso:
#Tomar un elemento de la primera lista.
#Tomar un elemento de la segunda lista.
#Repetir hasta terminar una lista.
#Agregar los elementos restantes si una lista es más larga.

#Salida:
#Retornar una lista con elementos alternados.


#2. Bosquejo a mano

#Crear clase CombinadorListas.

#Método intercalar():
#Crear lista vacía resultado.
#Obtener la menor longitud de las listas.
#Recorrer los índices.
#Agregar un elemento de cada lista.
#Agregar sobrantes.

#Método intercalar_multiples():
#Crear resultado vacío.
#Recorrer las listas recibidas.
#Llamar al método intercalar usando self.
#Retornar resultado.


#3. Descubrir el patrón

#Se utiliza len() para conocer tamaños.

#Se utiliza min() porque solo se puede intercalar hasta donde existan
#elementos en ambas listas.

#Se utiliza extend() para agregar elementos sobrantes.

#Se utiliza *listas porque se reciben cantidades variables de listas.


#4. Escribir código


class CombinadorListas:

    def intercalar(self, lista1, lista2):

        resultado = []

        longitud = min(len(lista1), len(lista2))

        for i in range(longitud):

            resultado.append(lista1[i])

            resultado.append(lista2[i])


        if len(lista1) > longitud:

            resultado.extend(lista1[longitud:])


        if len(lista2) > longitud:

            resultado.extend(lista2[longitud:])


        return resultado


    def intercalar_multiples(self, *listas):

        resultado = []

        for lista in listas:

            resultado = self.intercalar(resultado, lista)

        return resultado



#Parámetros de prueba


combinador = CombinadorListas()


lista1 = [1, 2, 3]

lista2 = ["A", "B", "C"]


print(combinador.intercalar(lista1, lista2))


resultado = combinador.intercalar_multiples(
    [1, 2],
    [3, 4],
    [5, 6]
)


print(resultado)



#5. Prueba de escritorio


#Objeto creado:

#combinador = CombinadorListas()


#Prueba 1:

#lista1 = [1,2,3]
#lista2 = ["A","B","C"]


#longitud:

#min(3,3) = 3


#Iteraciones:

#i=0:
#Agrega 1 y "A"

#resultado:
#[1,"A"]


#i=1:
#Agrega 2 y "B"

#resultado:
#[1,"A",2,"B"]


#i=2:
#Agrega 3 y "C"

#resultado:
#[1,"A",2,"B",3,"C"]


#Retorna:

#[1,"A",2,"B",3,"C"]



#Prueba 2:

#intercalar_multiples(
#[1,2],
#[3,4],
#[5,6]
#)


#Primera llamada:

#intercalar([], [1,2])

#resultado:

#[1,2]


#Segunda llamada:

#intercalar([1,2],[3,4])

#resultado:

#[1,3,2,4]


#Tercera llamada:

#intercalar([1,3,2,4],[5,6])

#resultado final:

#[1,5,3,6,2,4]

#EJERCICIO 14: Mapeo de estudiantes a notas

#Clase RegistroNotas que:
#(1) tenga método registrar(estudiante, nota) que guarde en un diccionario
#(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes
#(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.



#1. Entender el problema

#Entrada:
#Nombre del estudiante.
#Nota del estudiante.
#Nota mínima para aprobar.

#Proceso:
#Guardar estudiantes y notas en un diccionario.
#Recorrer el diccionario para encontrar estudiantes aprobados.
#Comparar notas para encontrar la mayor calificación.

#Salida:
#Lista de estudiantes aprobados.
#Nombre y nota del mejor estudiante.



#2. Bosquejo a mano

#Crear clase RegistroNotas.

#Crear atributo notas como diccionario vacío.

#Método registrar():
#Recibir estudiante y nota.
#Guardar estudiante como clave y nota como valor.

#Método estudiantes_aprobados():
#Crear lista vacía.
#Recorrer diccionario.
#Comparar nota con nota mínima.
#Agregar estudiante si cumple.

#Método mejor_estudiante():
#Crear variable para guardar mayor nota.
#Recorrer diccionario.
#Comparar notas.
#Guardar estudiante con mayor nota.



#3. Descubrir el patrón

#Se utiliza diccionario porque existe una relación:

#Estudiante -> Nota

#Ejemplo:

#{
#"Juan": 80,
#"Maria": 95
#}


#Se utiliza items() porque necesitamos la clave y el valor:

#clave = estudiante
#valor = nota


#4. Escribir código


class RegistroNotas:

    def __init__(self):

        self.notas = {}


    def registrar(self, estudiante, nota):

        self.notas[estudiante] = nota



    def estudiantes_aprobados(self, nota_minima):

        aprobados = []

        for estudiante, nota in self.notas.items():

            if nota >= nota_minima:

                aprobados.append(estudiante)

        return aprobados



    def mejor_estudiante(self):

        if len(self.notas) == 0:

            return None


        mayor = 0

        estudiante_mayor = None


        for estudiante, nota in self.notas.items():

            if nota > mayor:

                mayor = nota

                estudiante_mayor = estudiante


        return estudiante_mayor, mayor



#Parámetros de prueba


registro = RegistroNotas()


registro.registrar("Carlos", 85)

registro.registrar("Ana", 95)

registro.registrar("Luis", 70)

registro.registrar("Maria", 90)



print(registro.notas)


print(registro.estudiantes_aprobados(80))


print(registro.mejor_estudiante())



#5. Prueba de escritorio


#Después de registrar:

#self.notas queda:

#{
#"Carlos":85,
#"Ana":95,
#"Luis":70,
#"Maria":90
#}



#Método estudiantes_aprobados(80)


#Carlos:
#85 >= 80
#Se agrega.


#Ana:
#95 >= 80
#Se agrega.


#Luis:
#70 >= 80
#No se agrega.


#Maria:
#90 >= 80
#Se agrega.


#Resultado:

#["Carlos","Ana","Maria"]



#Método mejor_estudiante()


#mayor = 0


#Carlos:
#85 > 0
#mayor = 85


#Ana:
#95 > 85
#mayor = 95


#Luis:
#70 > 95
#No cambia.


#Maria:
#90 > 95
#No cambia.


#Resultado:

#("Ana",95)

#EJERCICIO 15: Divisores de un número

#Clase DivisorFinder que:
#(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores
#(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él
#(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}



#1. Entender el problema

#Entrada:
#Un número entero.
#Varios números enteros.

#Proceso:
#Encontrar números que dividen exactamente al número original.
#Guardar los divisores en una tupla.
#Sumar los divisores excepto el mismo número.
#Comparar la suma con el número original.

#Salida:
#Tupla de divisores.
#True o False si es perfecto.
#Diccionario con números y sus divisores.



#2. Bosquejo a mano

#Crear clase DivisorFinder.

#Método encontrar_divisores():

#Crear lista vacía.
#Recorrer desde 1 hasta el número.
#Comprobar si el residuo es 0.
#Guardar divisor.
#Convertir lista a tupla.


#Método es_perfecto():

#Llamar encontrar_divisores().
#Recorrer divisores.
#Excluir el mismo número.
#Sumar divisores.
#Comparar resultado.


#Método encontrar_multiples_divisores():

#Crear diccionario vacío.
#Recorrer números recibidos con *numeros.
#Guardar número como clave.
#Guardar sus divisores como valor.



#3. Descubrir el patrón

#Se utiliza:

#numero % i == 0

#porque indica que i divide exactamente al número.


#Se usa una tupla porque el resultado de divisores no debería modificarse.


#Se usa un diccionario porque relaciona:

#Número -> divisores



#4. Código


class DivisorFinder:

    def encontrar_divisores(self, numero):

        divisores = []

        for i in range(1, numero + 1):

            if numero % i == 0:

                divisores.append(i)

        return tuple(divisores)



    def es_perfecto(self, numero):

        divisores = self.encontrar_divisores(numero)

        suma = 0


        for divisor in divisores:

            if divisor != numero:

                suma += divisor


        return suma == numero



    def encontrar_multiples_divisores(self, *numeros):

        resultado = {}


        for numero in numeros:

            resultado[numero] = self.encontrar_divisores(numero)


        return resultado



#Parámetros de prueba


buscador = DivisorFinder()


print(buscador.encontrar_divisores(12))


print(buscador.es_perfecto(6))


print(buscador.es_perfecto(20))


print(
    buscador.encontrar_multiples_divisores(
        6,
        10,
        12,
        28
    )
)



#5. Prueba de escritorio


#Prueba 1:

#numero = 12


#Recorrido:

#i=1 -> 12 % 1 == 0 -> guarda 1
#i=2 -> guarda 2
#i=3 -> guarda 3
#i=4 -> guarda 4
#i=5 -> no guarda
#i=6 -> guarda 6
#...
#i=12 -> guarda 12


#Resultado:

#(1,2,3,4,6,12)



#Prueba 2:

#numero = 6


#Divisores:

#(1,2,3,6)


#Se excluye 6:

#1+2+3 = 6


#Resultado:

#True



#Prueba 3:

#numero = 20


#Divisores:

#(1,2,4,5,10,20)


#Sin el mismo número:

#1+2+4+5+10 = 22


#22 != 20


#Resultado:

#False

#EJERCICIO 16: Codificador/Decodificador

#Clase CodificadorCesar que:
#(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %)
#(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra
#(3) tenga un diccionario como atributo para historial de codificaciones.



#1. Entender el problema

#Entrada:
#Una letra.
#Un número de desplazamiento.
#Una palabra.

#Proceso:
#Buscar la posición de la letra dentro del alfabeto.
#Sumar el desplazamiento.
#Aplicar módulo (%) para regresar al inicio si supera la última letra.
#Repetir el proceso para todas las letras de una palabra.

#Salida:
#Letra codificada.
#Palabra codificada.
#Diccionario con historial.



#2. Bosquejo a mano

#Crear clase CodificadorCesar.

#Crear atributo historial como diccionario vacío.

#Método codificar_letra():

#Guardar alfabeto.
#Comprobar si la letra existe.
#Buscar posición.
#Mover posición.
#Retornar nueva letra.


#Método codificar_palabra():

#Crear variable resultado vacía.
#Recorrer cada letra.
#Llamar codificar_letra().
#Concatenar letras.
#Guardar palabra original y codificada en historial.



#3. Descubrir el patrón

#Ejemplo:

#Letra = z
#Desplazamiento = 3


#Posición de z:

#25


#Operación:

#(25 + 3) % 26

#28 % 26 = 2


#Posición 2 del alfabeto:

#c


#Resultado:

#z + 3 = c



#4. Código


class CodificadorCesar:

    def __init__(self):

        self.historial = {}


    def codificar_letra(self, letra, desplazamiento):

        alfabeto = "abcdefghijklmnopqrstuvwxyz"


        if letra.lower() in alfabeto:

            posicion = alfabeto.index(letra.lower())

            nueva_posicion = (posicion + desplazamiento) % len(alfabeto)

            return alfabeto[nueva_posicion]


        return letra



    def codificar_palabra(self, palabra, desplazamiento):

        resultado = ""


        for letra in palabra:

            resultado += self.codificar_letra(letra, desplazamiento)


        self.historial[palabra] = resultado


        return resultado



#5. Parámetros de prueba


cesar = CodificadorCesar()


print(cesar.codificar_letra("a", 3))


print(cesar.codificar_letra("z", 3))


print(cesar.codificar_palabra("hola", 3))


print(cesar.historial)



#Resultado esperado:

#d
#c
#krod

#{
#'hola': 'krod'
#}

#EJERCICIO 17: Grupo de edades

#Clase AgrupadorEdades que:
#(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor")
#(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}
#(3) tenga método edad_promedio_categoria(categoria).



#1. Entender el problema

#Entrada:
#Edades individuales.
#Varias edades.
#Categoría para buscar promedio.

#Proceso:
#Comparar la edad con rangos establecidos.
#Guardar cada edad dentro de su categoría.
#Sumar edades de una categoría.
#Dividir entre la cantidad de edades.

#Salida:
#Categoría de una edad.
#Diccionario agrupado.
#Promedio de una categoría.



#2. Bosquejo a mano

#Crear clase AgrupadorEdades.

#Crear atributo grupos como diccionario vacío.


#Método clasificar_edad():

#Si edad <= 12:
#niño

#Si edad <= 17:
#adolescente

#Si edad < 60:
#adulto

#Caso contrario:
#mayor



#Método agrupar_por_categoria():

#Crear diccionario con listas vacías.

#Recorrer edades.

#Clasificar cada edad.

#Agregar edad a la lista correspondiente.



#Método edad_promedio_categoria():

#Buscar categoría.

#Recorrer edades.

#Sumar.

#Dividir entre cantidad.



#3. Descubrir el patrón

#Se utiliza un diccionario porque relaciona:

#Categoría -> lista de edades


#Ejemplo:

#{
#"adulto": [25,40]
#}


#Se usa:

#self.clasificar_edad()

#para reutilizar el método anterior.



#4. Código

class AgrupadorEdades:

    def __init__(self):

        self.grupos = {}


    def clasificar_edad(self, edad):

        if edad <= 12:

            return "niño"

        elif edad <= 17:

            return "adolescente"

        elif edad < 60:

            return "adulto"

        else:

            return "mayor"



    def agrupar_por_categoria(self, *edades):

        self.grupos = {

            "niño": [],

            "adolescente": [],

            "adulto": [],

            "mayor": []

        }


        for edad in edades:

            categoria = self.clasificar_edad(edad)

            self.grupos[categoria].append(edad)


        return self.grupos



    def edad_promedio_categoria(self, categoria):

        if categoria not in self.grupos:

            return 0


        if len(self.grupos[categoria]) == 0:

            return 0


        suma = 0


        for edad in self.grupos[categoria]:

            suma += edad


        return suma / len(self.grupos[categoria])

agrupador = AgrupadorEdades()


print(agrupador.clasificar_edad(8))


print(
    agrupador.agrupar_por_categoria(
        5,
        10,
        15,
        17,
        25,
        35,
        60,
        80
    )
)


print(
    agrupador.edad_promedio_categoria("adulto")
)

#5. Pruebas de escritorio
# PRUEBA 1:
# Método: clasificar_edad(edad)

# Parámetro de prueba:
# edad = 15


# Llamada:
# agrupador.clasificar_edad(15)


# Proceso:

# edad = 15

# Primera condición:
# if edad <= 12

# 15 <= 12 → False


# Segunda condición:
# elif edad <= 17

# 15 <= 17 → True


# Retorna:

# "adolescente"

# PRUEBA 2:
# Método: agrupar_por_categoria(*edades)

# Parámetros de prueba:

# edades = (5, 15, 30, 70)


# Llamada:

# agrupador.agrupar_por_categoria(5, 15, 30, 70)



# Inicio del diccionario:

# {
# "niño": [],
# "adolescente": [],
# "adulto": [],
# "mayor": []
# }



# Primera vuelta del for:

# edad = 5


# Se llama:

# clasificar_edad(5)


# 5 <= 12 → True


# Categoría:

# "niño"


# Agrega:

# "niño": [5]



# Segunda vuelta del for:

# edad = 15


# Se llama:

# clasificar_edad(15)


# 15 <= 12 → False

# 15 <= 17 → True


# Categoría:

# "adolescente"


# Agrega:

# "adolescente": [15]



# Tercera vuelta del for:

# edad = 30


# Se llama:

# clasificar_edad(30)


# 30 <= 12 → False

# 30 <= 17 → False

# 30 < 60 → True


# Categoría:

# "adulto"


# Agrega:

# "adulto": [30]



# Cuarta vuelta del for:

# edad = 70


# Se llama:

# clasificar_edad(70)


# 70 <= 12 → False

# 70 <= 17 → False

# 70 < 60 → False


# Entra en else:


# Categoría:

# "mayor"


# Agrega:

# "mayor": [70]



# Resultado final:

# {
# "niño": [5],
# "adolescente": [15],
# "adulto": [30],
# "mayor": [70]
# }



# PRUEBA 3:
# Método: edad_promedio_categoria(categoria)


# Parámetro de prueba:

# categoria = "adulto"


# Estado del diccionario:

# {
# "niño": [5],
# "adolescente": [15],
# "adulto": [30],
# "mayor": [70]
# }



# Busca:

# self.grupos["adulto"]


# Obtiene:

# [30]


# Inicializa:

# suma = 0



# Recorrido:

# edad = 30


# suma = suma + edad

# suma = 0 + 30

# suma = 30



# Cantidad de elementos:

# len([30]) = 1



# Promedio:

# 30 / 1 = 30



# Resultado:

# Retorna 30

#EJERCICIO 18: Matriz de distancias

#Clase CalculadorDistancia que:
#(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia
#(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia
#(3) tenga un atributo lista para guardar todas las distancias calculadas.



#1. Entender el problema

#Entrada:

#Dos puntos representados como tuplas:

#p1 = (x1, y1)

#p2 = (x2, y2)


#Un punto de referencia y varios puntos para comparar.



#Proceso:

#Separar las coordenadas de cada punto.

#Aplicar la fórmula de distancia euclidiana:

#√((x2-x1)^2 + (y2-y1)^2)


#Guardar cada distancia calculada en una lista.


#Comparar las distancias obtenidas para encontrar
#el punto más cercano.



#Salida:

#Retornar la distancia entre dos puntos.

#Retornar el punto con menor distancia.

#Guardar historial de distancias calculadas.



#2. Bosquejo a mano


#Crear clase CalculadorDistancia.


#Crear atributo:

#self.distancias = []


#Método distancia_euclidiana():

#Recibir dos tuplas.

#Separar coordenadas.

#Calcular distancia.

#Guardar distancia en la lista.

#Retornar distancia.



#Método punto_mas_cercano():

#Recibir punto referencia y varias tuplas.

#Tomar el primer punto como candidato.

#Calcular su distancia.

#Recorrer los demás puntos.

#Comparar si la nueva distancia es menor.

#Actualizar el punto más cercano.



#3. Descubrir el patrón


#Las tuplas representan coordenadas:

#(x,y)


#Se pueden separar directamente:

#x, y = punto



#Para encontrar el menor valor se utiliza una variable
#que guarda la menor distancia encontrada.


#Ejemplo:

#menor_distancia = primera distancia


#Luego se compara:

#if distancia < menor_distancia:

#    actualizar valor



#Se utiliza *puntos porque el método puede recibir
#una cantidad variable de puntos.



#4. Escribir código



class CalculadorDistancia:

    def __init__(self):

        self.distancias = []



    def distancia_euclidiana(self, p1, p2):

        x1, y1 = p1

        x2, y2 = p2


        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5


        self.distancias.append(distancia)


        return distancia



    def punto_mas_cercano(self, referencia, *puntos):

        if len(puntos) == 0:

            return None


        punto_cercano = puntos[0]


        menor_distancia = self.distancia_euclidiana(
            referencia,
            punto_cercano
        )


        for punto in puntos[1:]:


            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )


            if distancia < menor_distancia:

                menor_distancia = distancia

                punto_cercano = punto


        return punto_cercano




#Parámetros de prueba



calculador = CalculadorDistancia()



#Prueba de distancia entre dos puntos

print(
    calculador.distancia_euclidiana(
        (0,0),
        (3,4)
    )
)



#Prueba de punto más cercano


print(
    calculador.punto_mas_cercano(
        (0,0),
        (5,5),
        (2,2),
        (10,10)
    )
)



#Mostrar historial de distancias


print(calculador.distancias)




#5. Prueba de escritorio



#Objeto creado:

#calculador = CalculadorDistancia()


#Estado inicial:

#distancias = []



#Prueba 1:


#Parámetros:

#p1 = (0,0)

#p2 = (3,4)



#Separación de coordenadas:

#x1 = 0

#y1 = 0

#x2 = 3

#y2 = 4



#Aplicación de fórmula:


#distancia = ((3-0)^2 + (4-0)^2)^0.5


#distancia = (9 + 16)^0.5


#distancia = 25^0.5


#distancia = 5



#Guarda:

#distancias = [5]


#Retorna:

#5.0





#Prueba 2:



#Parámetros:


#referencia = (0,0)


#puntos:

#(5,5)

#(2,2)

#(10,10)



#Primer punto:

#punto_cercano = (5,5)



#Calcula distancia:


#√((5-0)^2 + (5-0)^2)


#√50


#7.07



#Guarda:

#menor_distancia = 7.07



#Segundo punto:

#punto = (2,2)



#Calcula distancia:


#√((2-0)^2 + (2-0)^2)


#√8


#2.82



#Comparación:


#2.82 < 7.07


#Verdadero



#Actualiza:


#menor_distancia = 2.82

#punto_cercano = (2,2)



#Tercer punto:


#punto = (10,10)



#Calcula distancia:


#√((10-0)^2 + (10-0)^2)


#√200


#14.14



#Comparación:


#14.14 < 2.82


#Falso



#No cambia el resultado.



#Resultado final:


#Punto más cercano:

#(2,2)

#EJERCICIO 19: Inventario de productos

#Clase Inventario que:
#(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario
#(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente
#(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.



#1. Entender el problema


#Entrada:

#Nombre del producto.

#Cantidad del producto.

#Cantidad que se desea retirar.

#Cantidad mínima para buscar productos con poco stock.



#Proceso:

#Guardar productos y cantidades dentro de un diccionario.

#Cada producto será una clave del diccionario.

#Cada cantidad será el valor asociado a esa clave.


#Al agregar stock:

#Si el producto existe, aumentar la cantidad.

#Si no existe, crear un nuevo producto.


#Al restar stock:

#Verificar que el producto exista.

#Verificar que la cantidad disponible sea suficiente.

#Restar la cantidad solicitada.


#Para buscar bajo stock:

#Recorrer el diccionario.

#Comparar las cantidades con el mínimo.



#Salida:

#Diccionario con productos y cantidades.

#True si se pudo retirar stock.

#False si no existe producto o no hay suficiente cantidad.

#Lista con productos debajo del mínimo.



#2. Bosquejo a mano


#Crear clase Inventario.


#Crear atributo:

#self.stock = {}



#Método agregar_stock(producto, cantidad):

#Recibir producto y cantidad.

#Verificar si el producto existe.

#Si existe:

#sumar cantidad existente.


#Si no existe:

#crear producto con esa cantidad.



#Método restar_stock(producto, cantidad):

#Buscar producto.

#Comparar cantidad disponible con cantidad solicitada.

#Si hay suficiente:

#restar cantidad.

#retornar True.


#Si no hay suficiente:

#retornar False.



#Método productos_bajo_stock(minimo):

#Crear lista vacía.

#Recorrer productos.

#Si cantidad < minimo:

#agregar producto a la lista.



#3. Descubrir el patrón


#Se utiliza un diccionario porque existe una relación:

#Producto -> Cantidad


#Ejemplo:


#{
#"Mouse":10,
#"Teclado":5
#}



#La clave representa el producto.

#El valor representa la cantidad disponible.



#Para recorrer claves y valores:

#Se utiliza items().


#Ejemplo:


#for producto, cantidad in self.stock.items():



#Para modificar un valor del diccionario:

#self.stock[producto] += cantidad



#Para verificar existencia:

#if producto in self.stock:



#4. Escribir código



class Inventario:

    def __init__(self):

        self.stock = {}



    def agregar_stock(self, producto, cantidad):

        if producto in self.stock:

            self.stock[producto] += cantidad

        else:

            self.stock[producto] = cantidad



    def restar_stock(self, producto, cantidad):

        if producto in self.stock:

            if self.stock[producto] >= cantidad:

                self.stock[producto] -= cantidad

                return True


        return False



    def productos_bajo_stock(self, minimo):

        productos = []


        for producto, cantidad in self.stock.items():

            if cantidad < minimo:

                productos.append(producto)


        return productos



inventario = Inventario()


inventario.agregar_stock(
    "Mouse",
    10
)


inventario.agregar_stock(
    "Teclado",
    5
)


inventario.agregar_stock(
    "Monitor",
    2
)



print(inventario.stock)



#Restar stock

print(
    inventario.restar_stock(
        "Mouse",
        3
    )
)


print(inventario.stock)


print(
    inventario.productos_bajo_stock(
        5
    )
)




#5. Prueba de escritorio



#Objeto creado:


#inventario = Inventario()



#Estado inicial:


#stock = {}

#Prueba 1:


#agregar_stock("Mouse",10)



#Producto no existe.


#Se crea:


#stock = {

#"Mouse":10

#}

#Prueba 2:


#agregar_stock("Teclado",5)



#Producto no existe.


#Se crea:


#stock = {

#"Mouse":10,

#"Teclado":5

#}



#Prueba 3:


#agregar_stock("Mouse",3)



#Producto existe.


#Busca:


#stock["Mouse"]


#Valor actual:

#10



#Realiza:


#10 + 3 = 13



#Nuevo estado:


#stock = {

#"Mouse":13,

#"Teclado":5

#}


#Prueba 4:


#restar_stock("Mouse",4)



#Verifica:


#Producto existe.


#Cantidad disponible:

#13



#Cantidad solicitada:

#4



#Comparación:


#13 >= 4


#Verdadero



#Realiza:


#13 - 4 = 9



#Retorna:


#True



#Nuevo estado:


#stock = {

#"Mouse":9,

#"Teclado":5

#}



#Prueba 5:


#productos_bajo_stock(5)



#Recorre:


#Mouse:

#9 < 5

#Falso



#Teclado:

#5 < 5

#Falso



#Monitor:

#2 < 5

#Verdadero



#Agrega:


#"Monitor"



#Resultado final:


#["Monitor"]

#EJERCICIO 20: Analizador de patrones en textos

#Clase AnalizadorPatrones que:
#(1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista
#(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}
#(3) tenga método palabras_unicas() usando un conjunto.



#1. Entender el problema


#Entrada:

#Un texto con varias palabras.

#Un patrón de búsqueda.



#Proceso:

#Separar el texto en palabras usando split().

#Comparar el inicio de cada palabra con el patrón.

#Guardar las palabras que coincidan.


#Para agrupar por longitud:

#Obtener la cantidad de caracteres de cada palabra.

#Crear grupos según la longitud.



#Para palabras únicas:

#Usar un conjunto para eliminar palabras repetidas.



#Salida:

#Lista de palabras que empiezan con el patrón.

#Diccionario agrupado por longitud.

#Conjunto de palabras sin repetir.



#2. Bosquejo a mano


#Crear clase AnalizadorPatrones.


#Crear atributo para guardar las palabras analizadas.


#Método encontrar_palabras():

#Recibir texto y patrón.

#Separar texto en palabras.

#Crear lista vacía.

#Recorrer palabras.

#Verificar si empiezan con el patrón.

#Agregar coincidencias.

#Retornar lista.



#Método agrupar_por_longitud():

#Separar texto.

#Crear diccionario vacío.

#Recorrer palabras.

#Obtener longitud.

#Guardar palabra dentro de su grupo.



#Método palabras_unicas():

#Convertir lista de palabras a conjunto.

#Retornar conjunto.



#3. Descubrir el patrón


#Se utiliza split() para convertir un texto
#en una lista de palabras.


#Ejemplo:


#texto = "hola mundo python"


#split() genera:


#["hola","mundo","python"]



#Se utiliza startswith()
#para verificar si una palabra comienza
#con un patrón.


#Ejemplo:


#"python".startswith("py")


#Resultado:

#True



#Se utiliza len()
#para conocer la longitud de una palabra.



#Se utiliza un conjunto porque no permite
#elementos repetidos.



#4. Escribir código



class AnalizadorPatrones:

    def __init__(self):

        self.palabras = []



    def encontrar_palabras(self, texto, patron):

        palabras_encontradas = []


        palabras = texto.split()


        for palabra in palabras:

            if palabra.startswith(patron):

                palabras_encontradas.append(palabra)



        self.palabras = palabras


        return palabras_encontradas



    def agrupar_por_longitud(self, texto):

        agrupacion = {}


        palabras = texto.split()


        for palabra in palabras:

            longitud = len(palabra)


            if longitud not in agrupacion:

                agrupacion[longitud] = []


            agrupacion[longitud].append(palabra)



        return agrupacion



    def palabras_unicas(self):

        return set(self.palabras)




#Parámetros de prueba



analizador = AnalizadorPatrones()



texto = "python programación prueba casa carro python"



print(
    analizador.encontrar_palabras(
        texto,
        "pro"
    )
)



print(
    analizador.agrupar_por_longitud(
        texto
    )
)



print(
    analizador.palabras_unicas()
)




#5. Prueba de escritorio



#Objeto creado:


#analizador = AnalizadorPatrones()



#Estado inicial:


#palabras = []



#Prueba 1:


#texto:

#"python programación prueba casa carro python"


#patron:

#"pro"



#split:


#[
#"python",
#"programación",
#"prueba",
#"casa",
#"carro",
#"python"
#]



#Comparaciones:


#python empieza con pro

#False



#programación empieza con pro

#True



#Agrega:

#"programación"



#prueba empieza con pro

#True



#Agrega:

#"prueba"



#Resultado:


#[
#"programación",
#"prueba"
#]




#Prueba 2:


#agrupar_por_longitud()



#Palabras:


#python = 6

#programación = 12

#prueba = 6

#casa = 4

#carro = 5

#python = 6



#Diccionario generado:


#{

#6:[
#"python",
#"prueba",
#"python"
#],

#12:[
#"programación"
#],

#4:[
#"casa"
#],

#5:[
#"carro"
#]

#}



#Resultado:


#Diccionario agrupado por longitud.



#Prueba 3:


#palabras_unicas()



#Lista guardada:


#[
#"python",
#"programación",
#"prueba",
#"casa",
#"carro",
#"python"
#]



#Convertir a conjunto elimina repetidos:


#{

#"python",

#"programación",

#"prueba",

#"casa",

#"carro"

#}



#Resultado:


#Conjunto de palabras únicas.
