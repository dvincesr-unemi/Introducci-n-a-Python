# KEY EN PYTHON

# La palabra key significa "criterio de comparación".
#
# Se utiliza en funciones como:
#
# - max()
# - min()
# - sorted()
#
# para decirle a Python:
#
# "¿Qué valor debe usar para comparar los elementos?"

# EJEMPLO:
def libro_mas_largo(self):

    if len(self.libros) == 0:
        return None

    return max(self.libros, key=self.libros.get)

# -------------------------------------------------

# EJEMPLO SIN KEY

numeros = [5, 10, 2, 8]

mayor = max(numeros)

print(mayor)

# Python compara directamente los números:
#
# 5, 10, 2, 8
#
# Resultado:
# 10


# -------------------------------------------------

# EJEMPLO CON KEY

productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Monitor", "precio": 300}
]


producto_caro = max(
    productos,
    key=lambda producto: producto["precio"]
)


print(producto_caro)


# Aquí Python no compara los diccionarios completos.
#
# Usa el key para saber qué debe comparar.
#
# El lambda devuelve:
#
# Laptop  -> 850
# Mouse   -> 25
# Monitor -> 300
#
# Entonces max() compara:
#
# 850, 25, 300
#
# y devuelve el producto que tenga el mayor precio.


# -------------------------------------------------

# SIN KEY Python no sabe qué comparar:

# Ejemplo:

productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 25}
]


# max(productos)
#
# No tiene un criterio claro:
#
# ¿Comparo por nombre?
# ¿Por precio?
# ¿Por todo el diccionario?


# Por eso usamos:

max(
    productos,
    key=lambda producto: producto["precio"]
)


# -------------------------------------------------

# KEY CON SORTED()

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 18},
    {"nombre": "Carlos", "edad": 30}
]


ordenadas = sorted(
    personas,
    key=lambda persona: persona["edad"]
)


# Ordena usando la edad:
#
# Luis   18
# Ana    25
# Carlos 30


# -------------------------------------------------

# RESUMEN:
#
# key = "usa este valor para comparar"
#
# Ejemplo:
#
# max(lista, key=lambda x: x["precio"])
#
# significa:
#
# "Busca el elemento máximo,
# pero decide cuál es máximo usando el precio."

# LAMBDA EN PYTHON

# Lambda es una forma de crear funciones pequeñas
# en una sola línea.
#
# Estructura:
#
# lambda parametros: resultado
#
# Ejemplo:

duplicar = lambda numero: numero * 2

print(duplicar(5))

# Salida:
# 10
#
# Esto es equivalente a crear una función normal:

def duplicar(numero):
    return numero * 2


# -------------------------------------------------

# USO PRINCIPAL DE LAMBDA:
#
# Lambda se usa mucho cuando una función
# necesita recibir otra función temporalmente.
#
# Ejemplo con max():

productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Monitor", "precio": 300}
]


producto_caro = max(
    productos,
    key=lambda producto: producto["precio"]
)


print(producto_caro)


# ¿Qué significa?
#
# max() necesita saber qué valor debe comparar.
#
# Los elementos son diccionarios:
#
# {
#    "nombre": "Laptop",
#    "precio": 850
# }
#
# Entonces usamos:
#
# lambda producto: producto["precio"]
#
# Que significa:
#
# "Recibe un producto y devuelve su precio
# para usarlo como criterio de comparación."


# Python internamente hace algo parecido a:

# Laptop  -> 850
# Mouse   -> 25
# Monitor -> 300
#
# Luego max() compara esos valores
# y devuelve el producto con mayor precio.


# -------------------------------------------------

# USO CON MIN()

producto_barato = min(
    productos,
    key=lambda producto: producto["precio"]
)


# Devuelve:
# {"nombre": "Mouse", "precio": 25}


# -------------------------------------------------

# USO CON sorted()

productos_ordenados = sorted(
    productos,
    key=lambda producto: producto["precio"]
)


# Ordena los productos de menor a mayor precio.


# Si queremos de mayor a menor:

productos_ordenados = sorted(
    productos,
    key=lambda producto: producto["precio"],
    reverse=True
)


# -------------------------------------------------

# EJEMPLO CON LISTAS NORMALES

numeros = [5, 10, 2, 8]

mayor_cuadrado = max(
    numeros,
    key=lambda numero: numero ** 2
)


# Compara los números usando su cuadrado:
#
# 5  -> 25
# 10 -> 100
# 2  -> 4
# 8  -> 64
#
# Resultado:
# 10


# -------------------------------------------------

# REGLA PARA RECORDAR:
#
# Cuando veas:
#
# key=lambda x: algo
#
# Léelo como:
#
# "Usa algo de cada elemento para comparar."
#
#
# Ejemplos:
#
# max(personas, key=lambda p: p["edad"])
#
# Busca la persona con mayor edad.
#
#
# min(productos, key=lambda p: p["precio"])
#
# Busca el producto más barato.
#
#
# sorted(nombres, key=lambda n: len(n))
#
# Ordena nombres según su longitud.

class NumeroPrimo:

    # Atributo de clase (compartido por todas las instancias)
    primos_verificados = []

    def __init__(self):
        self.historial = []

    def es_primo(self, numero):

        self.historial.append(numero)

        primo = True

        if numero < 2:
            primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

        if primo:
            NumeroPrimo.primos_verificados.append(numero)

        return primo

    def primos_en_rango(self, *args):

        primos = []

        for numero in args:

            if self.es_primo(numero):
                primos.append(numero)

        return primos

    def cantidad_verificados(self):

        return len(self.historial)

    def obtener_primos_verificados(self):

        return NumeroPrimo.primos_verificados


obj = NumeroPrimo()

print(obj.es_primo(7))
print(obj.es_primo(10))

print(obj.primos_en_rango(11, 12, 13, 14, 15, 16, 17))

print("Historial:", obj.historial)
print("Cantidad verificados:", obj.cantidad_verificados())
print("Primos verificados:", obj.obtener_primos_verificados())

#EJERCICIO 1: Validador de notas con promedio
#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario
#(2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista 
#(3) tenga método promedio() que retorne el promedio de notas almacenadas.

class Calificador:

    def __init__ (self):
        self.notas = []

    def validar_nota(self, nota):
        return 0<= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas      
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas)/len(self.notas)

estudiante1 = Calificador()
estudiante1.cargar_notas(90,-67,78,90,78,96)
print(estudiante1.notas)
print(estudiante1.promedio())



# 1. Eliminar una nota
# Elimina una nota específica si existe.

def eliminar_nota(self, nota):

    if nota in self.notas:
        self.notas.remove(nota)



# 2. Vaciar todas las notas
# Borra completamente la lista de notas.

def limpiar_notas(self):

    self.notas.clear()



# 3. Mostrar la nota más alta
# Devuelve la mayor nota almacenada.

def nota_maxima(self):

    if len(self.notas) == 0:
        return 0

    return max(self.notas)


# ==========================================================
# 4. Mostrar la nota más baja
# ==========================================================
# Devuelve la menor nota almacenada.

def nota_minima(self):

    if len(self.notas) == 0:
        return 0

    return min(self.notas)


# ==========================================================
# 5. Contar cuántas notas hay
# ==========================================================
# Devuelve la cantidad de notas almacenadas.

def cantidad_notas(self):

    return len(self.notas)


# ==========================================================
# 6. Saber si el estudiante aprueba
# ==========================================================
# Retorna True si el promedio es mayor o igual a 70.

def aprobado(self):

    return self.promedio() >= 70


# ==========================================================
# 7. Buscar si existe una nota
# ==========================================================
# Devuelve True si la nota está almacenada.

def buscar_nota(self, nota):

    return nota in self.notas


# ==========================================================
# 8. Ordenar las notas
# ==========================================================
# Ordena las notas de menor a mayor.

def ordenar_notas(self):

    self.notas.sort()


# ==========================================================
# 9. Ordenar de mayor a menor
# ==========================================================
# Ordena las notas de mayor a menor.

def ordenar_descendente(self):

    self.notas.sort(reverse=True)


# ==========================================================
# 10. Mostrar todas las notas
# ==========================================================
# Retorna la lista completa.

def mostrar_notas(self):

    return self.notas


# ==========================================================
# 11. Obtener la suma de todas las notas
# ==========================================================
# Devuelve la suma total.

def suma_notas(self):

    return sum(self.notas)


# ==========================================================
# 12. Reemplazar una nota por otra
# ==========================================================
# Busca una nota y la cambia por una nueva.

def reemplazar_nota(self, vieja, nueva):

    if vieja in self.notas and self.validar_nota(nueva):

        indice = self.notas.index(vieja)
        self.notas[indice] = nueva


# ==========================================================
# 13. Agregar una sola nota
# ==========================================================
# Similar a cargar_notas(), pero recibe una sola.

def agregar_nota(self, nota):

    if self.validar_nota(nota):

        self.notas.append(nota)


# ==========================================================
# 14. Contar aprobadas
# ==========================================================
# Cuenta cuántas notas son mayores o iguales a 70.

def contar_aprobadas(self):

    contador = 0

    for nota in self.notas:

        if nota >= 70:
            contador += 1

    return contador


# ==========================================================
# 15. Contar reprobadas
# ==========================================================
# Cuenta cuántas notas son menores a 70.

def contar_reprobadas(self):

    contador = 0

    for nota in self.notas:

        if nota < 70:
            contador += 1

    return contador


# ==========================================================
# 16. Mostrar solo notas aprobadas
# ==========================================================
# Devuelve una lista con notas >= 70.

def notas_aprobadas(self):

    lista = []

    for nota in self.notas:

        if nota >= 70:
            lista.append(nota)

    return lista


# ==========================================================
# 17. Mostrar solo notas reprobadas
# ==========================================================
# Devuelve una lista con notas < 70.

def notas_reprobadas(self):

    lista = []

    for nota in self.notas:

        if nota < 70:
            lista.append(nota)

    return lista


# ==========================================================
# 18. Calcular porcentaje de aprobación
# ==========================================================
# Devuelve el porcentaje de notas aprobadas.

def porcentaje_aprobacion(self):

    if len(self.notas) == 0:
        return 0

    return self.contar_aprobadas() * 100 / len(self.notas)


# ==========================================================
# 19. Mostrar un resumen
# ==========================================================
# Devuelve un diccionario con información importante.

def resumen(self):

    return {
        "cantidad": len(self.notas),
        "promedio": self.promedio(),
        "maxima": self.nota_maxima(),
        "minima": self.nota_minima()
    }


# 20. Reiniciar el objeto

# Elimina todas las notas.

def reiniciar(self):

    self.notas = []

#Contador de palabras únicas
#Clase AnalizadorTexto que: 
#(1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden)
#(2) tenga método contar_palabras() que retorne cuántas palabras únicas hay
#(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.

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


# 1. Método para saber si una palabra existe
# Verifica si una palabra ya fue agregada al conjunto

def existe_palabra(self, palabra):
    return palabra in self.palabra_conjunto


# 2. Método para eliminar una palabra
# Elimina la palabra del conjunto y de la lista

def eliminar_palabra(self, palabra):
    if palabra in self.palabra_conjunto:
        self.palabra_conjunto.remove(palabra)

    if palabra in self.palabra_lista:
        self.palabra_lista.remove(palabra)


# 3. Método para contar todas las palabras ingresadas
# Cuenta incluyendo palabras repetidas

def contar_total_palabras(self):
    return len(self.palabra_lista)


# 4. Método para mostrar todas las palabras sin repetir
# Retorna el conjunto convertido en lista

def mostrar_unicas(self):
    return list(self.palabra_conjunto)


# 5. Método para limpiar todos los datos
# Vacía la lista y el conjunto

def limpiar_texto(self):
    self.palabra_conjunto.clear()
    self.palabra_lista.clear()


# 6. Método para convertir todas las palabras a minúsculas
# Evita que "Hola" y "hola" sean palabras diferentes

def convertir_minusculas(self):
    self.palabra_lista = [palabra.lower() for palabra in self.palabra_lista]
    self.palabra_conjunto = set(self.palabra_lista)


# 7. Método para buscar palabras por letra inicial
# Retorna palabras que comienzan con una letra específica

def buscar_por_letra(self, letra):
    resultado = []

    for palabra in self.palabra_lista:
        if palabra.startswith(letra):
            resultado.append(palabra)

    return resultado


# 8. Método para contar cuántas veces aparece una palabra
# Usa la lista porque el conjunto elimina duplicados

def frecuencia_palabra(self, palabra):
    return self.palabra_lista.count(palabra)


# 9. Método para obtener la palabra más larga

def palabra_mas_larga(self):
    if len(self.palabra_lista) == 0:
        return ""

    return max(self.palabra_lista, key=len)


# 10. Método para ordenar palabras alfabéticamente

def ordenar_palabras(self):
    return sorted(self.palabra_lista)

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

#CAMBIO 1: Eliminar un articulo
#Elimina un producto del diccionario usando su nombre.

def eliminar_articulo(self, nombre):
    if nombre in self.productos:
        del self.productos[nombre]
        return True
    return False


#CAMBIO 2: Actualizar precio
#Cambia el precio de un producto existente.

def actualizar_precio(self, nombre, nuevo_precio):
    if nombre in self.productos:
        self.productos[nombre] = nuevo_precio
        return True
    return False


#CAMBIO 3: Buscar producto
#Verifica si un producto existe en el diccionario.

def buscar_producto(self, nombre):
    return nombre in self.productos


#CAMBIO 4: Cantidad de artículos
#Retorna la cantidad de productos registrados.

def cantidad_articulos(self):
    return len(self.productos)


#CAMBIO 5: Producto más caro
#Retorna el nombre del producto con mayor precio.

def producto_mas_caro(self):
    if len(self.productos) == 0:
        return None

    return max(self.productos, key=self.productos.get)


#CAMBIO 6: Producto más barato
#Retorna el nombre del producto con menor precio.

def producto_mas_barato(self):
    if len(self.productos) == 0:
        return None

    return min(self.productos, key=self.productos.get)


#CAMBIO 7: Mostrar productos
#Muestra todos los productos con sus precios.

def mostrar_productos(self):
    for nombre, precio in self.productos.items():
        print(nombre, precio)


#CAMBIO 8: Promedio de precios
#Calcula el precio promedio de todos los productos.

def promedio_precios(self):
    if len(self.productos) == 0:
        return 0

    return sum(self.productos.values()) / len(self.productos)


#CAMBIO 9: Aplicar descuento
#Reduce el precio de un producto según un porcentaje.

def aplicar_descuento(self, nombre, porcentaje):
    if nombre in self.productos:
        descuento = self.productos[nombre] * porcentaje / 100
        self.productos[nombre] -= descuento


#CAMBIO 10: Ordenar productos por precio
#Retorna los productos ordenados de menor a mayor precio.

# Ordena los productos del diccionario según su precio utilizando items() para obtener nombre y valor.
# lambda toma cada tupla y usa la posición [1], que corresponde al precio, para realizar el ordenamiento.

def ordenar_productos(self):
    return sorted(self.productos.items(), key=lambda producto: producto[1])

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

#CAMBIO 1: Método invertir_con_texto(lista)
#Invierte una lista y muestra un mensaje indicando el resultado.

def invertir_con_texto(self, lista):

    invertida = self.invertir_lista(lista)

    return f"La lista {lista} invertida es {invertida}"


#CAMBIO 2: Método contar_elementos(lista)
#Retorna la cantidad de elementos que tiene una lista.

def contar_elementos(self, lista):

    return len(lista)


#CAMBIO 3: Método verificar_palindromo(lista)
#Verifica si una lista es igual al revés de sí misma.

def verificar_palindromo(self, lista):

    invertida = self.invertir_lista(lista)

    return lista == invertida


#CAMBIO 4: Método invertir_desde_posicion(lista, posicion)
#Invierte una lista empezando desde una posición indicada.

def invertir_desde_posicion(self, lista, posicion):

    resultado = []

    for i in range(posicion, -1, -1):

        resultado.append(lista[i])

    return resultado


#CAMBIO 5: Método unir_listas(*listas)
#Une varias listas recibidas en una sola lista.

def unir_listas(self, *listas):

    resultado = []

    for lista in listas:

        resultado.extend(lista)

    return resultado


#CAMBIO 6: Método eliminar_repetidos(lista)
#Elimina elementos repetidos usando un conjunto y retorna una lista.

def eliminar_repetidos(self, lista):

    return list(set(lista))


#CAMBIO 7: Método mayor_elemento(lista)
#Retorna el elemento más grande de una lista.

def mayor_elemento(self, lista):

    return max(lista)


#CAMBIO 8: Método menor_elemento(lista)
#Retorna el elemento más pequeño de una lista.

def menor_elemento(self, lista):

    return min(lista)


#CAMBIO 9: Método ordenar_lista(lista)
#Ordena una lista de menor a mayor.

def ordenar_lista(self, lista):

    return sorted(lista)


#CAMBIO 10: Método frecuencia_elementos(lista)
#Cuenta cuántas veces aparece cada elemento usando un diccionario.

def frecuencia_elementos(self, lista):

    frecuencia = {}

    for elemento in lista:

        if elemento in frecuencia:
            frecuencia[elemento] += 1

        else:
            frecuencia[elemento] = 1

    return frecuencia


#CAMBIO 11: Método separar_pares_impares(lista)
#Separa los números pares e impares en dos listas.

def separar_pares_impares(self, lista):

    pares = []
    impares = []

    for numero in lista:

        if numero % 2 == 0:
            pares.append(numero)

        else:
            impares.append(numero)

    return pares, impares


#CAMBIO 12: Método buscar_elemento(lista, elemento)
#Verifica si un elemento existe dentro de la lista.

def buscar_elemento(self, lista, elemento):

    return elemento in lista

#EJERCICIO 5: Detector de números pares e impares
# Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False
#(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par
#(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).   

class AnalizarNumeros:

    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        return False

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
                           

#CAMBIO 1: Método suma_pares()
#Suma todos los números pares almacenados en la clase y retorna el resultado.

def suma_pares(self):

    return sum(self.pares)


#CAMBIO 2: Método suma_impares()
#Suma todos los números impares almacenados en la clase y retorna el resultado.

def suma_impares(self):

    return sum(self.impares)


#CAMBIO 3: Método mayor_numero()
#Retorna el número más grande entre todos los números ingresados.

def mayor_numero(self):

    todos = self.pares + self.impares

    return max(todos)


#CAMBIO 4: Método menor_numero()
#Retorna el número más pequeño entre todos los números ingresados.

def menor_numero(self):

    todos = self.pares + self.impares

    return min(todos)


#CAMBIO 5: Método promedio()
#Calcula el promedio de todos los números ingresados.

def promedio(self):

    todos = self.pares + self.impares

    return sum(todos) / len(todos)


#CAMBIO 6: Método cantidad_total()
#Retorna la cantidad total de números analizados.

def cantidad_total(self):

    return len(self.pares) + len(self.impares)


#CAMBIO 7: Método buscar_numero(numero)
#Verifica si un número existe dentro de los pares o impares.

def buscar_numero(self, numero):

    return numero in self.pares or numero in self.impares


#CAMBIO 8: Método limpiar_datos()
#Elimina todos los números almacenados en la clase.

def limpiar_datos(self):

    self.pares.clear()
    self.impares.clear()


#CAMBIO 9: Método ordenar_numeros()
#Retorna todos los números ordenados de menor a mayor.

def ordenar_numeros(self):

    todos = self.pares + self.impares

    return sorted(todos)


#CAMBIO 10: Método separar_negativos_positivos()
#Clasifica los números positivos y negativos además de pares e impares.

def separar_negativos_positivos(self):

    positivos = []
    negativos = []

    todos = self.pares + self.impares

    for numero in todos:

        if numero >= 0:
            positivos.append(numero)

        else:
            negativos.append(numero)

    return {
        "positivos": positivos,
        "negativos": negativos
    }


#CAMBIO 11: Método porcentaje_pares()
#Calcula qué porcentaje de los números ingresados son pares.

def porcentaje_pares(self):

    total = len(self.pares) + len(self.impares)

    return (len(self.pares) / total) * 100


#CAMBIO 12: Método frecuencia_numeros()
#Cuenta cuántas veces aparece cada número utilizando un diccionario.

def frecuencia_numeros(self):

    frecuencia = {}

    todos = self.pares + self.impares

    for numero in todos:

        if numero in frecuencia:
            frecuencia[numero] += 1

        else:
            frecuencia[numero] = 1

    return frecuencia
#EJERCICIO 6: Estadísticas de temperatura
#Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista
#(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas
#(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.

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

#CAMBIO 1: Método temperatura_promedio_diaria()
#Permite calcular el promedio pero indicando que son temperaturas registradas durante un día.

def temperatura_promedio_diaria(self):

    return sum(self.temperaturas) / len(self.temperaturas)


#CAMBIO 2: Método contar_temperaturas()
#Retorna la cantidad de temperaturas registradas.

def contar_temperaturas(self):

    return len(self.temperaturas)


#CAMBIO 3: Método eliminar_temperatura(temp)
#Elimina una temperatura específica de la lista.

def eliminar_temperatura(self, temp):

    if temp in self.temperaturas:
        self.temperaturas.remove(temp)


#CAMBIO 4: Método buscar_temperatura(temp)
#Verifica si una temperatura existe dentro de los registros.

def buscar_temperatura(self, temp):

    return temp in self.temperaturas


#CAMBIO 5: Método ordenar_temperaturas()
#Ordena las temperaturas de menor a mayor.

def ordenar_temperaturas(self):

    return sorted(self.temperaturas)


#CAMBIO 6: Método rango_temperatura()
#Retorna la diferencia entre la temperatura máxima y mínima.

def rango_temperatura(self):

    return max(self.temperaturas) - min(self.temperaturas)


#CAMBIO 7: Método clasificar_temperaturas()
#Separa temperaturas altas y bajas según un límite indicado.

def clasificar_temperaturas(self, limite):

    altas = []
    bajas = []

    for temp in self.temperaturas:

        if temp >= limite:
            altas.append(temp)

        else:
            bajas.append(temp)

    return {
        "altas": altas,
        "bajas": bajas
    }


#CAMBIO 8: Método convertir_fahrenheit()
#Convierte todas las temperaturas Celsius a Fahrenheit.

def convertir_fahrenheit(self):

    resultado = []

    for temp in self.temperaturas:

        fahrenheit = (temp * 9/5) + 32

        resultado.append(fahrenheit)

    return resultado


#CAMBIO 9: Método temperatura_mas_repetida()
#Retorna la temperatura que más veces aparece.

def temperatura_mas_repetida(self):

    frecuencia = {}

    for temp in self.temperaturas:

        if temp in frecuencia:

            frecuencia[temp] += 1

        else:

            frecuencia[temp] = 1

    return max(frecuencia, key=frecuencia.get)


#CAMBIO 10: Método limpiar_registros()
#Elimina todas las temperaturas almacenadas.

def limpiar_registros(self):

    self.temperaturas.clear()


#CAMBIO 11: Método agregar_lista(lista)
#Permite registrar temperaturas enviadas dentro de una lista.

def agregar_lista(self, lista):

    for temp in lista:

        self.registrar_temperatura(temp)


#CAMBIO 12: Método estado_clima()
#Retorna un resumen de los datos registrados usando un diccionario.

def estado_clima(self):

    return {
        "minima": self.minima(),
        "maxima": self.maxima(),
        "promedio": self.promedio(),
        "cantidad": len(self.temperaturas)
    }

#EJERCICIO 7: Mapeador de edades
#Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario
#(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥
#(3) tenga método edad_promedio() que retorne el promedio de edades.

class GestorPersonas: 
    def __init__(self):
        self.edades=[]
    def agregar_personas(self, nombre, edad):
        personas = {
            "nombre": "",
            "edad": 0
        }
        personas["nombre"]= nombre
        personas["edad"]= edad

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

#CAMBIO 1: Método buscar_persona()
#Busca una persona por su nombre y retorna sus datos.

def buscar_persona(self, nombre):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            return persona

    return None


#CAMBIO 2: Método eliminar_persona()
#Elimina una persona por su nombre.

def eliminar_persona(self, nombre):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            self.edades.remove(persona)

            return True

    return False


#CAMBIO 3: Método actualizar_edad()
#Modifica la edad de una persona.

def actualizar_edad(self, nombre, nueva_edad):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            persona["edad"] = nueva_edad

            return True

    return False


#CAMBIO 4: Método contar_personas()
#Retorna la cantidad de personas registradas.

def contar_personas(self):

    return len(self.edades)


#CAMBIO 5: Método persona_mayor()
#Retorna la persona con mayor edad.

def persona_mayor(self):

    return max(self.edades, key=lambda persona: persona["edad"])


#CAMBIO 6: Método persona_menor()
#Retorna la persona con menor edad.

def persona_menor(self):

    return min(self.edades, key=lambda persona: persona["edad"])


#CAMBIO 7: Método ordenar_por_edad()
#Ordena las personas de menor a mayor edad.

def ordenar_por_edad(self):

    return sorted(self.edades, key=lambda persona: persona["edad"])


#CAMBIO 8: Método ordenar_por_nombre()
#Ordena las personas alfabéticamente.

def ordenar_por_nombre(self):

    return sorted(self.edades, key=lambda persona: persona["nombre"])


#CAMBIO 9: Método mayores_de_edad()
#Retorna únicamente las personas de 18 años o más.

def mayores_de_edad(self):

    resultado = []

    for persona in self.edades:

        if persona["edad"] >= 18:

            resultado.append(persona)

    return resultado


#CAMBIO 10: Método menores_de_edad()
#Retorna únicamente las personas menores de 18 años.

def menores_de_edad(self):

    resultado = []

    for persona in self.edades:

        if persona["edad"] < 18:

            resultado.append(persona)

    return resultado


#CAMBIO 11: Método existe_persona()
#Verifica si una persona ya está registrada.

def existe_persona(self, nombre):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            return True

    return False


#CAMBIO 12: Método limpiar_personas()
#Elimina todas las personas registradas.

def limpiar_personas(self):

    self.edades.clear()

#EJERCICIO 8: Asignador de equipos
#Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario
#(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo
#(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.

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

#CAMBIO 1: Método eliminar_jugador(equipo, jugador)
#Elimina un jugador específico de un equipo.

def eliminar_jugador(self, equipo, jugador):

    if jugador in self.equipos[equipo]:

        self.equipos[equipo].remove(jugador)

        return True

    return False


#CAMBIO 2: Método cantidad_jugadores(equipo)
#Retorna la cantidad de jugadores que tiene un equipo.

def cantidad_jugadores(self, equipo):

    return len(self.equipos[equipo])


#CAMBIO 3: Método listar_jugadores(equipo)
#Retorna la lista de jugadores de un equipo.

def listar_jugadores(self, equipo):

    return self.equipos[equipo]


#CAMBIO 4: Método buscar_jugador(jugador)
#Busca en qué equipo se encuentra un jugador.

def buscar_jugador(self, jugador):

    for equipo, jugadores in self.equipos.items():

        if jugador in jugadores:

            return equipo

    return None


#CAMBIO 5: Método eliminar_equipo(nombre_equipo)
#Elimina un equipo completo del diccionario.

def eliminar_equipo(self, equipo):

    if equipo in self.equipos:

        del self.equipos[equipo]

        return True

    return False


#CAMBIO 6: Método cantidad_equipos()
#Retorna cuántos equipos existen.

def cantidad_equipos(self):

    return len(self.equipos)


#CAMBIO 7: Método equipos_con_mas_jugadores(cantidad)
#Retorna equipos que tienen una cantidad mínima de jugadores.

def equipos_con_mas_jugadores(self, cantidad):

    resultado = []

    for equipo, jugadores in self.equipos.items():

        if len(jugadores) >= cantidad:

            resultado.append(equipo)

    return resultado


#CAMBIO 8: Método ordenar_equipos()
#Retorna los equipos ordenados por cantidad de jugadores.

def ordenar_equipos(self):

    return sorted(
        self.equipos.items(),
        key=lambda equipo: len(equipo[1]),
        reverse=True
    )


#CAMBIO 9: Método transferir_jugador(jugador, equipo_actual, equipo_nuevo)
#Mueve un jugador de un equipo a otro.

def transferir_jugador(self, jugador, equipo_actual, equipo_nuevo):

    if jugador in self.equipos[equipo_actual]:

        self.equipos[equipo_actual].remove(jugador)

        self.equipos[equipo_nuevo].append(jugador)

        return True

    return False


#CAMBIO 10: Método equipo_menor_integrantes()
#Retorna el equipo con menos jugadores.

def equipo_menor_integrantes(self):

    menor = ""
    cantidad = float("inf")

    for equipo, jugadores in self.equipos.items():

        if len(jugadores) < cantidad:

            cantidad = len(jugadores)

            menor = equipo

    return menor

#Ejercicio 9: Validador de caracteres
#Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal
#(2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos;
#(3) tenga atributo que guarde el texto más largo analizado.

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

    #CAMBIO 1: Método es_digito(numero)
#Comprueba manualmente si un carácter es un número.

def es_digito(self, letra):

    digitos = "0123456789"

    return letra in digitos


#CAMBIO 2: Método es_letra(letra)
#Comprueba manualmente si un carácter pertenece al alfabeto.

def es_letra(self, letra):

    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return letra in letras


#CAMBIO 3: Método es_consonante(letra)
#Determina si una letra es consonante reutilizando métodos.

def es_consonante(self, letra):

    if self.es_letra(letra) and not self.solo_vocales(letra):

        return True

    return False



#CAMBIO 4: Reemplazar isdigit() e isalpha()
#En contar_por_tipo() cambiar:

#elif letra.isdigit():

#por:

#elif self.es_digito(letra):


#Y cambiar:

##elif letra.isalpha():

#por:

#elif self.es_consonante(letra):



#CAMBIO 5: Método contar_mayusculas()
#Cuenta cuántas letras mayúsculas tiene el texto.

def contar_mayusculas(self, texto):

    cantidad = 0

    for letra in texto:

        if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            cantidad += 1

    return cantidad


#CAMBIO 6: Método contar_minusculas()
#Cuenta cuántas letras minúsculas tiene el texto.

def contar_minusculas(self, texto):

    cantidad = 0

    for letra in texto:

        if letra in "abcdefghijklmnopqrstuvwxyz":

            cantidad += 1

    return cantidad


#CAMBIO 7: Método eliminar_espacios()
#Retorna el texto sin espacios.

def eliminar_espacios(self, texto):

    nuevo_texto = ""

    for letra in texto:

        if letra != " ":

            nuevo_texto += letra

    return nuevo_texto


#CAMBIO 8: Método invertir_texto()
#Invierte el texto manualmente sin usar reverse().

def invertir_texto(self, texto):

    invertido = ""

    for i in range(len(texto)-1, -1, -1):

        invertido += texto[i]

    return invertido

#CAMBIO 1: Método cantidad_total_caracteres()
#Retorna cuántos caracteres tiene el texto.

def cantidad_total_caracteres(self, texto):

    return len(texto)



#CAMBIO 2: Método eliminar_espacios()
#Retorna una nueva cadena sin espacios.

def eliminar_espacios(self, texto):

    resultado = ""

    for letra in texto:

        if letra != " ":

            resultado += letra

    return resultado



#CAMBIO 3: Método invertir_texto()
#Invierte una cadena usando ciclos.

def invertir_texto(self, texto):

    invertido = ""

    for letra in texto:

        invertido = letra + invertido

    return invertido



#CAMBIO 4: Método contar_caracter()
#Cuenta cuántas veces aparece un carácter.

def contar_caracter(self, texto, caracter):

    contador = 0

    for letra in texto:

        if letra == caracter:

            contador += 1

    return contador



#CAMBIO 5: Método frecuencia_caracteres()
#Guarda la frecuencia de cada carácter en un diccionario.

def frecuencia_caracteres(self, texto):

    frecuencia = {}

    for letra in texto:

        if letra in frecuencia:

            frecuencia[letra] += 1

        else:

            frecuencia[letra] = 1

    return frecuencia



#CAMBIO 6: Método guardar_textos()
#Guarda varios textos analizados.

def __init__(self):

    self.texto_mas_largo = ""

    self.textos = []



def guardar_texto(self, texto):

    self.textos.append(texto)



#CAMBIO 7: Método texto_mas_repetido()
#Busca el texto que más veces aparece.

def texto_mas_repetido(self):

    frecuencia = {}

    for texto in self.textos:

        if texto in frecuencia:

            frecuencia[texto] += 1

        else:

            frecuencia[texto] = 1

    return max(frecuencia, key=frecuencia.get)



#CAMBIO 8: Método separar_caracteres()
#Separa letras y números en listas.

def separar_caracteres(self, texto):

    letras = []

    numeros = []

    for caracter in texto:

        if caracter in "0123456789":

            numeros.append(caracter)

        else:

            letras.append(caracter)

    return {
        "letras": letras,
        "numeros": numeros
    }
#EJERCICIO 10: Gestor de tareas con prioridad
#Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad)
#(2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta
#(3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.
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

#CAMBIO 1: Método cantidad_tareas()
#Retorna la cantidad total de tareas registradas.

def cantidad_tareas(self):

    return len(self.lista_tuplas)



#CAMBIO 2: Método mostrar_tareas()
#Retorna todas las tareas registradas.

def mostrar_tareas(self):

    return self.lista_tuplas



#CAMBIO 3: Método buscar_tarea()
#Busca una tarea por su descripción.

def buscar_tarea(self, descripcion):

    for desc, prioridad in self.lista_tuplas:

        if desc == descripcion:

            return (desc, prioridad)

    return None



#CAMBIO 4: Método cambiar_prioridad()
#Cambia la prioridad de una tarea existente.

def cambiar_prioridad(self, descripcion, nueva_prioridad):

    for i in range(len(self.lista_tuplas)):

        desc, prioridad = self.lista_tuplas[i]

        if desc == descripcion:

            self.lista_tuplas[i] = (desc, nueva_prioridad)

            return True

    return False



#CAMBIO 5: Método eliminar_todas()
#Elimina todas las tareas registradas.

def eliminar_todas(self):

    self.lista_tuplas.clear()



#CAMBIO 6: Método tareas_por_prioridad()
#Retorna todas las tareas de una prioridad indicada.

def tareas_por_prioridad(self, prioridad_busqueda):

    lista = []

    for descripcion, prioridad in self.lista_tuplas:

        if prioridad.lower() == prioridad_busqueda.lower():

            lista.append(descripcion)

    return lista



#CAMBIO 7: Método existe_tarea()
#Comprueba si una tarea ya está registrada.

def existe_tarea(self, descripcion):

    for desc, prioridad in self.lista_tuplas:

        if desc == descripcion:

            return True

    return False



#CAMBIO 8: Método cantidad_por_prioridad()
#Cuenta cuántas tareas hay de prioridad Alta, Media y Baja.

def cantidad_por_prioridad(self):

    contador = {
        "Alta": 0,
        "Media": 0,
        "Baja": 0
    }

    for descripcion, prioridad in self.lista_tuplas:

        contador[prioridad.capitalize()] += 1

    return contador



#CAMBIO 9: Método primera_tarea()
#Retorna la primera tarea registrada.

def primera_tarea(self):

    if len(self.lista_tuplas) == 0:

        return None

    return self.lista_tuplas[0]



#CAMBIO 10: Método ultima_tarea()
#Retorna la última tarea registrada.

def ultima_tarea(self):

    if len(self.lista_tuplas) == 0:

        return None

    return self.lista_tuplas[-1]



#CAMBIO 11: Método ordenar_por_prioridad()
#Ordena las tareas alfabéticamente por prioridad.

def ordenar_por_prioridad(self):

    return sorted(self.lista_tuplas, key=lambda tarea: tarea[1])



#CAMBIO 12: Método descripcion_mas_larga()
#Retorna la descripción con mayor cantidad de caracteres.

def descripcion_mas_larga(self):

    if len(self.lista_tuplas) == 0:

        return None

    mayor = self.lista_tuplas[0][0]

    for descripcion, prioridad in self.lista_tuplas:

        if len(descripcion) > len(mayor):

            mayor = descripcion

    return mayor



#CAMBIO 13: Método eliminar_por_prioridad()
#Elimina todas las tareas de una prioridad indicada.

def eliminar_por_prioridad(self, prioridad_busqueda):

    nuevas = []

    for descripcion, prioridad in self.lista_tuplas:

        if prioridad.lower() != prioridad_busqueda.lower():

            nuevas.append((descripcion, prioridad))

    self.lista_tuplas = nuevas



#CAMBIO 14: Método cantidad_prioritarias()
#Retorna cuántas tareas tienen prioridad alta.

def cantidad_prioritarias(self):

    contador = 0

    for descripcion, prioridad in self.lista_tuplas:

        if prioridad.lower() == "alta":

            contador += 1

    return contador



#CAMBIO 15: Método actualizar_descripcion()
#Modifica la descripción de una tarea.

def actualizar_descripcion(self, descripcion, nueva_descripcion):

    for i in range(len(self.lista_tuplas)):

        desc, prioridad = self.lista_tuplas[i]

        if desc == descripcion:

            self.lista_tuplas[i] = (nueva_descripcion, prioridad)

            return True

    return False

#EJERCICIO 11: Contador de frecuencia
#Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones
#(2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia
#(3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.

class ContadoeFrecuencia:
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

#CAMBIO 1: Método elemento_mas_frecuente()
#Versión manual sin utilizar max().

def elemento_mas_frecuente(self):

    mayor = 0

    elemento = None

    for clave, valor in self.frecuencias.items():

        if valor > mayor:

            mayor = valor

            elemento = clave

    return elemento



#CAMBIO 2: Método frecuencia_elemento()
#Versión manual sin utilizar get().

def frecuencia_elemento(self, elemento):

    if elemento in self.frecuencias:

        return self.frecuencias[elemento]

    return 0



#CAMBIO 3: Método cantidad_elementos()
#Retorna cuántos elementos diferentes existen.

def cantidad_elementos(self):

    return len(self.frecuencias)



#CAMBIO 4: Método mostrar_frecuencias()
#Retorna el diccionario completo.

def mostrar_frecuencias(self):

    return self.frecuencias



#CAMBIO 5: Método eliminar_elemento()
#Elimina un elemento del diccionario.

def eliminar_elemento(self, elemento):

    if elemento in self.frecuencias:

        del self.frecuencias[elemento]

        return True

    return False



#CAMBIO 6: Método reiniciar()
#Vacía completamente el diccionario.

def reiniciar(self):

    self.frecuencias.clear()



#CAMBIO 7: Método existe_elemento()
#Comprueba si un elemento está registrado.

def existe_elemento(self, elemento):

    return elemento in self.frecuencias



#CAMBIO 8: Método elementos_repetidos()
#Retorna una lista de los elementos cuya frecuencia sea mayor que 1.

def elementos_repetidos(self):

    repetidos = []

    for elemento, frecuencia in self.frecuencias.items():

        if frecuencia > 1:

            repetidos.append(elemento)

    return repetidos



#CAMBIO 9: Método elementos_unicos()
#Retorna una lista de los elementos que aparecen una sola vez.

def elementos_unicos(self):

    unicos = []

    for elemento, frecuencia in self.frecuencias.items():

        if frecuencia == 1:

            unicos.append(elemento)

    return unicos



#CAMBIO 10: Método suma_frecuencias()
#Retorna la suma de todas las frecuencias.

def suma_frecuencias(self):

    return sum(self.frecuencias.values())



#CAMBIO 11: Método menor_frecuencia()
#Retorna el elemento con menor frecuencia usando min().

def menor_frecuencia(self):

    return min(self.frecuencias, key=self.frecuencias.get)



#CAMBIO 12: Método menor_frecuencia()
#Versión manual sin utilizar min().

def menor_frecuencia(self):

    menor = None

    elemento = None

    for clave, valor in self.frecuencias.items():

        if menor is None or valor < menor:

            menor = valor

            elemento = clave

    return elemento



#CAMBIO 13: Método ordenar_frecuencias()
#Ordena de mayor a menor frecuencia.

def ordenar_frecuencias(self):

    return sorted(self.frecuencias.items(), key=lambda dato: dato[1], reverse=True)



#CAMBIO 14: Método promedio_frecuencias()
#Retorna el promedio de las frecuencias.

def promedio_frecuencias(self):

    if len(self.frecuencias) == 0:

        return 0

    return sum(self.frecuencias.values()) / len(self.frecuencias)



#CAMBIO 15: Método elemento_menos_frecuente()
#Retorna el elemento con menor frecuencia utilizando lógica manual.

def elemento_menos_frecuente(self):

    menor = None

    elemento = None

    for clave, valor in self.frecuencias.items():

        if menor is None or valor < menor:

            menor = valor

            elemento = clave

    return elemento

#EJERCICIO 12: Selector de rango con tuplas
#Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango
#(2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.


class SelectorRango:

    def crear_rango(self, inicio, fin):

        return tuple(range(inicio, fin + 1))


    def elementos_en_multiples_rangos(self, *rangos):

        conjunto = set()

        for inicio, fin in rangos:

            for numero in range(inicio, fin + 1):

                conjunto.add(numero)

        return list(conjunto)

#CAMBIO 1: Método crear_rango()
#Versión manual sin utilizar range().

def crear_rango(self, inicio, fin):

    numeros = []

    while inicio <= fin:

        numeros.append(inicio)

        inicio += 1

    return tuple(numeros)



#CAMBIO 2: Método elementos_en_multiples_rangos()
#Versión manual sin utilizar set() directamente para eliminar duplicados.

def elementos_en_multiples_rangos(self, *rangos):

    lista = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero not in lista:

                lista.append(numero)

    return lista



#CAMBIO 3: Método buscar_elemento()
#Indica si un número pertenece a alguno de los rangos.

def buscar_elemento(self, numero_buscar, *rangos):

    for inicio, fin in rangos:

        if numero_buscar >= inicio and numero_buscar <= fin:

            return True

    return False



#CAMBIO 4: Método cantidad_elementos()
#Retorna la cantidad de números sin repetir.

def cantidad_elementos(self, *rangos):

    conjunto = set()

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            conjunto.add(numero)

    return len(conjunto)



#CAMBIO 5: Método rango_mayor()
#Retorna la tupla con el rango más grande.

def rango_mayor(self, *rangos):

    mayor = 0

    rango_mayor = None

    for inicio, fin in rangos:

        cantidad = fin - inicio + 1

        if cantidad > mayor:

            mayor = cantidad

            rango_mayor = (inicio, fin)

    return rango_mayor



#CAMBIO 6: Método rango_menor()
#Retorna la tupla con menos elementos.

def rango_menor(self, *rangos):

    menor = None

    resultado = None

    for inicio, fin in rangos:

        cantidad = fin - inicio + 1

        if menor is None or cantidad < menor:

            menor = cantidad

            resultado = (inicio, fin)

    return resultado



#CAMBIO 7: Método suma_elementos()
#Suma todos los números de los rangos sin repetir.

def suma_elementos(self, *rangos):

    conjunto = set()

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            conjunto.add(numero)

    suma = 0

    for numero in conjunto:

        suma += numero

    return suma



#CAMBIO 8: Método elementos_pares()
#Retorna únicamente los números pares.

def elementos_pares(self, *rangos):

    pares = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero % 2 == 0 and numero not in pares:

                pares.append(numero)

    return pares



#CAMBIO 9: Método elementos_impares()
#Retorna únicamente los números impares.

def elementos_impares(self, *rangos):

    impares = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero % 2 != 0 and numero not in impares:

                impares.append(numero)

    return impares



#CAMBIO 10: Método ordenar_elementos()
#Retorna los elementos ordenados.

def ordenar_elementos(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    return sorted(elementos)



#CAMBIO 11: Método invertir_resultado()
#Retorna los elementos en orden inverso.

def invertir_resultado(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    elementos.reverse()

    return elementos



#CAMBIO 12: Método rango_contiene()
#Comprueba si un rango contiene un número.

def rango_contiene(self, inicio, fin, numero):

    if numero >= inicio and numero <= fin:

        return True

    return False



#CAMBIO 13: Método unir_rangos_manual()
#Une rangos sin utilizar set().

def unir_rangos_manual(self, *rangos):

    lista = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero not in lista:

                lista.append(numero)

    return lista



#CAMBIO 14: Método promedio_elementos()
#Retorna el promedio de los elementos.

def promedio_elementos(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    if len(elementos) == 0:

        return 0

    suma = 0

    for numero in elementos:

        suma += numero

    return suma / len(elementos)



#CAMBIO 15: Método mayor_elemento()
#Retorna el número más grande usando lógica manual.

def mayor_elemento(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    mayor = elementos[0]

    for numero in elementos:

        if numero > mayor:

            mayor = numero

    return mayor

#EJERCICIO 14: Combinador de listas
#Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas
#(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.

class CombinadorListas:

    def intercalar(self, lista1, lista2):

        resultado = []

        longitud = min(len(lista1), len(lista2))

        for i in range(longitud):

            resultado.append(lista1[i])

            resultado.append(lista2[i])

        # Si una lista tiene más elementos que la otra

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

# POSIBLES CAMBIOS O MÉTODOS AGREGADOS
# EJERCICIO 14: Combinador de listas


# CAMBIO 1: Intercalar de forma manual sin usar min()

def intercalar(self, lista1, lista2):

    resultado = []

    i = 0

    while i < len(lista1) and i < len(lista2):

        resultado.append(lista1[i])

        resultado.append(lista2[i])

        i += 1


    while i < len(lista1):

        resultado.append(lista1[i])

        i += 1


    while i < len(lista2):

        resultado.append(lista2[i])

        i += 1


    return resultado



# CAMBIO 2: Intercalar múltiples listas con lógica más manual
# (sin reutilizar intercalar)

def intercalar_multiples(self, *listas):

    resultado = []

    mayor = 0

    for lista in listas:

        if len(lista) > mayor:

            mayor = len(lista)


    for i in range(mayor):

        for lista in listas:

            if i < len(lista):

                resultado.append(lista[i])


    return resultado



# CAMBIO 3: Método unir_listas()
# Une varias listas sin alternar.

def unir_listas(self, *listas):

    resultado = []

    for lista in listas:

        resultado.extend(lista)

    return resultado



# CAMBIO 4: Método eliminar_repetidos()
# Retorna una lista sin elementos repetidos.

def eliminar_repetidos(self, lista):

    resultado = []

    for elemento in lista:

        if elemento not in resultado:

            resultado.append(elemento)

    return resultado



# CAMBIO 5: Método elementos_comunes()
# Encuentra elementos que aparecen en ambas listas.

def elementos_comunes(self, lista1, lista2):

    comunes = []

    for elemento in lista1:

        if elemento in lista2:

            comunes.append(elemento)

    return comunes



# CAMBIO 6: Método diferencia_listas()
# Elementos que están en la primera lista pero no en la segunda.

def diferencia_listas(self, lista1, lista2):

    diferencia = []

    for elemento in lista1:

        if elemento not in lista2:

            diferencia.append(elemento)

    return diferencia



# CAMBIO 7: Método invertir_lista()
# Invierte una lista manualmente.

def invertir_lista(self, lista):

    invertida = []

    for i in range(len(lista)-1, -1, -1):

        invertida.append(lista[i])

    return invertida



# CAMBIO 8: Método contar_elementos()
# Cuenta cuántos elementos tiene una lista.

def contar_elementos(self, lista):

    contador = 0

    for elemento in lista:

        contador += 1

    return contador



# CAMBIO 9: Método buscar_elemento()
# Verifica si un elemento existe.

def buscar_elemento(self, lista, elemento):

    for dato in lista:

        if dato == elemento:

            return True

    return False



# CAMBIO 10: Método posicion_elemento()
# Retorna la posición de un elemento.

def posicion_elemento(self, lista, elemento):

    for i in range(len(lista)):

        if lista[i] == elemento:

            return i

    return -1



# CAMBIO 11: Método lista_mayor()
# Retorna la lista con más elementos.

def lista_mayor(self, *listas):

    mayor = listas[0]

    for lista in listas:

        if len(lista) > len(mayor):

            mayor = lista

    return mayor



# CAMBIO 12: Método lista_menor()
# Retorna la lista con menos elementos.

def lista_menor(self, *listas):

    menor = listas[0]

    for lista in listas:

        if len(lista) < len(menor):

            menor = lista

    return menor



# CAMBIO 13: Método ordenar_lista()
# Ordena una lista.

def ordenar_lista(self, lista):

    return sorted(lista)



# CAMBIO 14: Método separar_pares_impares()
# Divide una lista numérica.

def separar_pares_impares(self, lista):

    pares = []

    impares = []

    for numero in lista:

        if numero % 2 == 0:

            pares.append(numero)

        else:

            impares.append(numero)

    return pares, impares



# CAMBIO 15: Método intercalar_tres_listas()
# Ejemplo específico para tres listas.

def intercalar_tres_listas(self, lista1, lista2, lista3):

    resultado = []

    mayor = max(len(lista1), len(lista2), len(lista3))


    for i in range(mayor):

        if i < len(lista1):

            resultado.append(lista1[i])

        if i < len(lista2):

            resultado.append(lista2[i])

        if i < len(lista3):

            resultado.append(lista3[i])


    return resultado

#EJERCICIO 14: Mapeo de estudiantes a notas

#Clase RegistroNotas que:
#(1) tenga método registrar(estudiante, nota) que guarde en un diccionario
#(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes
#(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.


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

# POSIBLES CAMBIOS O MÉTODOS AGREGADOS
# EJERCICIO: Mapeo de estudiantes a notas


# CAMBIO 1: Registrar varias notas
# Permite ingresar varios estudiantes al mismo tiempo.

def registrar_multiples(self, **estudiantes):

    for nombre, nota in estudiantes.items():

        self.notas[nombre] = nota



# Ejemplo:
# registro.registrar_multiples(
#     Juan=80,
#     Maria=95,
#     Pedro=70
# )



# CAMBIO 2: Buscar nota de un estudiante

def buscar_nota(self, estudiante):

    if estudiante in self.notas:

        return self.notas[estudiante]

    return "Estudiante no registrado"



# CAMBIO 3: Modificar nota existente

def modificar_nota(self, estudiante, nueva_nota):

    if estudiante in self.notas:

        self.notas[estudiante] = nueva_nota

        return True

    return False



# CAMBIO 4: Eliminar estudiante

def eliminar_estudiante(self, estudiante):

    if estudiante in self.notas:

        del self.notas[estudiante]

        return True

    return False



# CAMBIO 5: Promedio general de notas

def promedio_notas(self):

    if len(self.notas) == 0:

        return 0


    suma = 0

    for nota in self.notas.values():

        suma += nota


    return suma / len(self.notas)



# CAMBIO 6: Contar aprobados

def cantidad_aprobados(self, nota_minima):

    contador = 0

    for nota in self.notas.values():

        if nota >= nota_minima:

            contador += 1

    return contador



# CAMBIO 7: Contar reprobados

def cantidad_reprobados(self, nota_minima):

    contador = 0

    for nota in self.notas.values():

        if nota < nota_minima:

            contador += 1

    return contador



# CAMBIO 8: Retornar estudiante con menor nota

def peor_estudiante(self):

    if len(self.notas) == 0:

        return None


    menor = None

    estudiante_menor = None


    for estudiante, nota in self.notas.items():

        if menor is None or nota < menor:

            menor = nota

            estudiante_menor = estudiante


    return estudiante_menor, menor



# CAMBIO 9: Lista ordenada de estudiantes por nota

def ordenar_por_nota(self):

    return sorted(
        self.notas.items(),
        key=lambda estudiante: estudiante[1],
        reverse=True
    )



# CAMBIO 10: Separar aprobados y reprobados

def clasificar_estudiantes(self, nota_minima):

    aprobados = []

    reprobados = []


    for estudiante, nota in self.notas.items():

        if nota >= nota_minima:

            aprobados.append(estudiante)

        else:

            reprobados.append(estudiante)


    return aprobados, reprobados



# CAMBIO 11: Nota más repetida

def nota_mas_comun(self):

    frecuencia = {}


    for nota in self.notas.values():

        if nota in frecuencia:

            frecuencia[nota] += 1

        else:

            frecuencia[nota] = 1


    mayor = 0

    nota_repetida = None


    for nota, cantidad in frecuencia.items():

        if cantidad > mayor:

            mayor = cantidad

            nota_repetida = nota


    return nota_repetida



# CAMBIO 12: Buscar estudiantes con una nota exacta

def estudiantes_con_nota(self, nota_buscar):

    estudiantes = []


    for estudiante, nota in self.notas.items():

        if nota == nota_buscar:

            estudiantes.append(estudiante)


    return estudiantes



# CAMBIO 13: Aumentar puntos a todos los estudiantes

def subir_nota(self, puntos):

    for estudiante in self.notas:

        self.notas[estudiante] += puntos



# CAMBIO 14: Mostrar todos los estudiantes

def mostrar_estudiantes(self):

    lista = []


    for estudiante, nota in self.notas.items():

        lista.append(
            (estudiante, nota)
        )


    return lista



# CAMBIO 15: Mejor estudiante usando max()

def mejor_estudiante_max(self):

    if len(self.notas) == 0:

        return None


    estudiante = max(
        self.notas,
        key=self.notas.get
    )


    return estudiante, self.notas[estudiante]

#EJERCICIO 15: Divisores de un número

#Clase DivisorFinder que:
#(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores
#(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él
#(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.



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

# POSIBLES CAMBIOS O MÉTODOS AGREGADOS
# EJERCICIO 15: Divisores de un número


# CAMBIO 1: Encontrar divisores sin incluir el mismo número
# Retorna solamente divisores propios.

def encontrar_divisores_propios(self, numero):

    divisores = []

    for i in range(1, numero):

        if numero % i == 0:

            divisores.append(i)

    return tuple(divisores)



# CAMBIO 2: Encontrar divisores usando lógica más eficiente
# Solo recorre hasta la mitad del número.

def encontrar_divisores_optimizado(self, numero):

    divisores = []

    for i in range(1, numero // 2 + 1):

        if numero % i == 0:

            divisores.append(i)


    divisores.append(numero)

    return tuple(divisores)



# CAMBIO 3: Contar cantidad de divisores

def cantidad_divisores(self, numero):

    divisores = self.encontrar_divisores(numero)

    return len(divisores)



# CAMBIO 4: Encontrar el divisor más grande

def mayor_divisor(self, numero):

    divisores = self.encontrar_divisores(numero)

    mayor = 0


    for divisor in divisores:

        if divisor > mayor:

            mayor = divisor


    return mayor



# CAMBIO 5: Encontrar el menor divisor diferente de 1

def menor_divisor(self, numero):

    for i in range(2, numero + 1):

        if numero % i == 0:

            return i



# CAMBIO 6: Verificar si un número es primo

def es_primo(self, numero):

    cantidad = 0


    for i in range(1, numero + 1):

        if numero % i == 0:

            cantidad += 1


    return cantidad == 2



# CAMBIO 7: Encontrar números primos dentro de varios números

def filtrar_primos(self, *numeros):

    primos = []


    for numero in numeros:

        if self.es_primo(numero):

            primos.append(numero)


    return primos



# CAMBIO 8: Sumar todos los divisores

def suma_divisores(self, numero):

    divisores = self.encontrar_divisores(numero)

    suma = 0


    for divisor in divisores:

        suma += divisor


    return suma



# CAMBIO 9: Verificar si es abundante
# La suma de divisores propios es mayor que el número.

def es_abundante(self, numero):

    divisores = self.encontrar_divisores(numero)

    suma = 0


    for divisor in divisores:

        if divisor != numero:

            suma += divisor


    return suma > numero



# CAMBIO 10: Verificar si es deficiente
# La suma de divisores propios es menor que el número.

def es_deficiente(self, numero):

    divisores = self.encontrar_divisores(numero)

    suma = 0


    for divisor in divisores:

        if divisor != numero:

            suma += divisor


    return suma < numero



# CAMBIO 11: Buscar números perfectos dentro de varios números

def perfectos_en_lista(self, *numeros):

    perfectos = []


    for numero in numeros:

        if self.es_perfecto(numero):

            perfectos.append(numero)


    return perfectos



# CAMBIO 12: Encontrar divisores comunes entre dos números

def divisores_comunes(self, numero1, numero2):

    comunes = []

    divisores1 = self.encontrar_divisores(numero1)

    divisores2 = self.encontrar_divisores(numero2)


    for divisor in divisores1:

        if divisor in divisores2:

            comunes.append(divisor)


    return tuple(comunes)



# CAMBIO 13: Encontrar máximo común divisor (MCD) manual

def mcd(self, numero1, numero2):

    comunes = self.divisores_comunes(numero1, numero2)

    mayor = 0


    for divisor in comunes:

        if divisor > mayor:

            mayor = divisor


    return mayor



# CAMBIO 14: Factorización prima básica

def factores_primos(self, numero):

    factores = []


    divisor = 2


    while numero > 1:

        if numero % divisor == 0:

            factores.append(divisor)

            numero = numero // divisor

        else:

            divisor += 1


    return tuple(factores)



# CAMBIO 15: Encontrar múltiplos de un número

def encontrar_multiplos(self, numero, limite):

    multiplos = []


    for i in range(1, limite + 1):

        if i % numero == 0:

            multiplos.append(i)


    return tuple(multiplos)

#EJERCICIO 16: Codificador/Decodificador

#Clase CodificadorCesar que:
#(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %)
#(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra
#(3) tenga un diccionario como atributo para historial de codificaciones.


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

# POSIBLES CAMBIOS O MÉTODOS AGREGADOS
# EJERCICIO 16: Codificador/Decodificador César


# CAMBIO 1: Codificar sin usar index()
# Programación más manual buscando la posición con un contador.

def codificar_letra_manual(self, letra, desplazamiento):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    posicion = 0


    for caracter in alfabeto:

        if caracter == letra.lower():

            break

        posicion += 1


    nueva_posicion = (posicion + desplazamiento) % len(alfabeto)


    return alfabeto[nueva_posicion]



# CAMBIO 2: Codificar sin usar len()
# Usando una variable fija porque el alfabeto tiene 26 letras.

def codificar_letra_sin_len(self, letra, desplazamiento):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"


    posicion = alfabeto.index(letra.lower())


    nueva_posicion = (posicion + desplazamiento) % 26


    return alfabeto[nueva_posicion]



# CAMBIO 3: Decodificar palabra
# Revierte la codificación usando desplazamiento negativo.

def decodificar_palabra(self, palabra, desplazamiento):

    resultado = ""


    for letra in palabra:

        resultado += self.codificar_letra(
            letra,
            -desplazamiento
        )


    return resultado



# CAMBIO 4: Guardar historial con más información

def guardar_historial_completo(self, original, desplazamiento, resultado):

    self.historial[original] = {

        "desplazamiento": desplazamiento,

        "resultado": resultado

    }



# Resultado:

# {
#   "hola":{
#       "desplazamiento":3,
#       "resultado":"krod"
#   }
# }



# CAMBIO 5: Codificar frases completas
# Mantiene espacios y símbolos.

def codificar_texto(self, texto, desplazamiento):

    resultado = ""


    for letra in texto:

        resultado += self.codificar_letra(
            letra,
            desplazamiento
        )


    return resultado



# CAMBIO 6: Mantener mayúsculas
# Devuelve la letra con el mismo formato original.

def codificar_letra_mayusculas(self, letra, desplazamiento):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    mayuscula = letra.isupper()


    letra = letra.lower()


    posicion = alfabeto.index(letra)


    nueva_posicion = (posicion + desplazamiento) % 26


    nueva_letra = alfabeto[nueva_posicion]


    if mayuscula:

        return nueva_letra.upper()


    return nueva_letra



# CAMBIO 7: Contar codificaciones realizadas

def cantidad_codificaciones(self):

    return len(self.historial)



# CAMBIO 8: Buscar una palabra en historial

def buscar_historial(self, palabra):

    if palabra in self.historial:

        return self.historial[palabra]


    return "No existe en historial"



# CAMBIO 9: Eliminar una codificación del historial

def eliminar_historial(self, palabra):

    if palabra in self.historial:

        del self.historial[palabra]

        return True


    return False



# CAMBIO 10: Codificar varias palabras

def codificar_multiples(self, palabras, desplazamiento):

    resultado = {}


    for palabra in palabras:

        resultado[palabra] = self.codificar_palabra(
            palabra,
            desplazamiento
        )


    return resultado



# CAMBIO 11: Cambiar alfabeto para incluir números
# Ejemplo: letras + números.

def codificar_con_numeros(self, texto, desplazamiento):

    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"

    resultado = ""


    for letra in texto:

        if letra in caracteres:

            posicion = caracteres.index(letra)

            nueva_posicion = (
                posicion + desplazamiento
            ) % len(caracteres)

            resultado += caracteres[nueva_posicion]

        else:

            resultado += letra


    return resultado



# CAMBIO 12: Hacer desplazamiento negativo

def retroceder_letra(self, letra, desplazamiento):

    return self.codificar_letra(
        letra,
        -desplazamiento
    )



# CAMBIO 13: Validar desplazamiento

def validar_desplazamiento(self, desplazamiento):

    if desplazamiento >= 0:

        return True

    return False



# CAMBIO 14: Codificar usando while
# En lugar de for.

def codificar_palabra_while(self, palabra, desplazamiento):

    resultado = ""

    i = 0


    while i < len(palabra):

        resultado += self.codificar_letra(
            palabra[i],
            desplazamiento
        )

        i += 1


    return resultado



# CAMBIO 15: Buscar frecuencia de letras codificadas

def frecuencia_letras(self, palabra):

    frecuencia = {}


    for letra in palabra:

        if letra in frecuencia:

            frecuencia[letra] += 1

        else:

            frecuencia[letra] = 1


    return frecuencia  

#EJERCICIO 17: Grupo de edades

#Clase AgrupadorEdades que:
#(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor")
#(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}
#(3) tenga método edad_promedio_categoria(categoria).


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

# POSIBLES CAMBIOS O MÉTODOS AGREGADOS
# EJERCICIO 17: Grupo de edades


# CAMBIO 1: Agregar más categorías

# Ejemplo:
# Bebé: 0 - 3 años
# Niño: 4 - 12 años
# Adolescente: 13 - 17 años
# Adulto: 18 - 59 años
# Mayor: 60 en adelante


def clasificar_edad_ampliada(self, edad):

    if edad <= 3:

        return "bebé"

    elif edad <= 12:

        return "niño"

    elif edad <= 17:

        return "adolescente"

    elif edad < 60:

        return "adulto"

    else:

        return "mayor"



# ----------------------------------------------------


# CAMBIO 2: Contar cantidad de personas por categoría


def cantidad_categoria(self, categoria):

    if categoria in self.grupos:

        return len(self.grupos[categoria])

    return 0



# Ejemplo:

# adulto = [25,30,40]

# retorna:

# 3



# ----------------------------------------------------


# CAMBIO 3: Encontrar edad máxima de una categoría
# Sin usar max()


def mayor_edad_categoria(self, categoria):

    if categoria not in self.grupos:

        return None


    mayor = 0


    for edad in self.grupos[categoria]:

        if edad > mayor:

            mayor = edad


    return mayor



# ----------------------------------------------------


# CAMBIO 4: Encontrar edad mínima de una categoría
# Sin usar min()


def menor_edad_categoria(self, categoria):

    if categoria not in self.grupos:

        return None


    menor = self.grupos[categoria][0]


    for edad in self.grupos[categoria]:

        if edad < menor:

            menor = edad


    return menor



# ----------------------------------------------------


# CAMBIO 5: Promedio más manual
# Sin usar len() directamente


def promedio_manual(self, categoria):

    suma = 0

    contador = 0


    for edad in self.grupos[categoria]:

        suma += edad

        contador += 1


    if contador == 0:

        return 0


    return suma / contador



# ----------------------------------------------------


# CAMBIO 6: Buscar personas de una categoría


def obtener_edades_categoria(self, categoria):

    if categoria in self.grupos:

        return self.grupos[categoria]


    return []



# ----------------------------------------------------


# CAMBIO 7: Agrupar desde una lista
# En lugar de recibir *edades


def agrupar_lista(self, edades):

    resultado = {}


    for edad in edades:

        categoria = self.clasificar_edad(edad)


        if categoria not in resultado:

            resultado[categoria] = []


        resultado[categoria].append(edad)


    return resultado



# ----------------------------------------------------


# CAMBIO 8: Encontrar categoría con más personas


def categoria_mas_grande(self):

    mayor = ""

    cantidad = 0


    for categoria, edades in self.grupos.items():

        if len(edades) > cantidad:

            cantidad = len(edades)

            mayor = categoria


    return mayor



# ----------------------------------------------------


# CAMBIO 9: Filtrar edades mayores a una edad dada


def mayores_a(self, edad_minima):

    resultado = []


    for categoria, edades in self.grupos.items():

        for edad in edades:

            if edad >= edad_minima:

                resultado.append(edad)


    return resultado



# ----------------------------------------------------


# CAMBIO 10: Guardar historial de agrupaciones


# En __init__ agregar:

# self.historial = []



def guardar_historial(self):

    self.historial.append(self.grupos)



# ----------------------------------------------------


# CAMBIO 11: Mezclar con diccionario de personas


# En vez de recibir solo edades:

# [
# {"nombre":"Ana","edad":15},
# {"nombre":"Luis","edad":30}
# ]


def agrupar_personas(self, personas):

    resultado = {

        "niño": [],

        "adolescente": [],

        "adulto": [],

        "mayor": []

    }


    for persona in personas:

        categoria = self.clasificar_edad(persona["edad"])


        resultado[categoria].append(
            persona["nombre"]
        )


    return resultado



# ----------------------------------------------------


# CAMBIO 12: Verificar si una categoría existe


def existe_categoria(self, categoria):

    return categoria in self.grupos


#EJERCICIO 18: Matriz de distancias

#Clase CalculadorDistancia que:
#(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia
#(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia
#(3) tenga un atributo lista para guardar todas las distancias calculadas.


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

# POSIBLES MEZCLAS, CAMBIOS O MÉTODOS AGREGADOS
# EJERCICIO 18: Matriz de distancias



# CAMBIO 1: Método punto_mas_lejano()

# Similar a punto_mas_cercano(),
# pero busca la distancia más grande.


def punto_mas_lejano(self, referencia, *puntos):

    if len(puntos) == 0:

        return None


    punto_lejano = puntos[0]


    mayor_distancia = self.distancia_euclidiana(
        referencia,
        punto_lejano
    )


    for punto in puntos[1:]:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if distancia > mayor_distancia:

            mayor_distancia = distancia

            punto_lejano = punto


    return punto_lejano



# ----------------------------------------------------


# CAMBIO 2: Método distancia_manhattan()

# Cambia la fórmula euclidiana por distancia Manhattan.


# Fórmula:

# |x2-x1| + |y2-y1|



def distancia_manhattan(self, p1, p2):

    x1, y1 = p1

    x2, y2 = p2


    distancia = abs(x2-x1) + abs(y2-y1)


    self.distancias.append(distancia)


    return distancia



# ----------------------------------------------------


# CAMBIO 3: Método obtener_menor_distancia()

# Retorna la distancia más pequeña guardada.


def obtener_menor_distancia(self):

    if len(self.distancias) == 0:

        return None


    menor = self.distancias[0]


    for distancia in self.distancias:

        if distancia < menor:

            menor = distancia


    return menor



# ----------------------------------------------------


# CAMBIO 4: Método obtener_mayor_distancia()

# Busca la distancia más grande manualmente.


def obtener_mayor_distancia(self):

    if len(self.distancias) == 0:

        return None


    mayor = self.distancias[0]


    for distancia in self.distancias:

        if distancia > mayor:

            mayor = distancia


    return mayor



# ----------------------------------------------------


# CAMBIO 5: Método promedio_distancias()

# Calcula promedio de todas las distancias.


def promedio_distancias(self):

    if len(self.distancias) == 0:

        return 0


    suma = 0


    for distancia in self.distancias:

        suma += distancia


    return suma / len(self.distancias)



# ----------------------------------------------------


# CAMBIO 6: Guardar puntos junto con sus distancias.


# Cambiar atributo:

# self.distancias = []


# Por:


# self.distancias = {}



# Guardaría:

# {
# ((0,0),(3,4)):5,
# ((1,1),(4,5)):5
# }



# ----------------------------------------------------


# CAMBIO 7: Método historial_distancias()

# Mostrar todas las distancias calculadas.


def historial_distancias(self):

    return self.distancias



# ----------------------------------------------------


# CAMBIO 8: Método cantidad_calculos()

# Saber cuántas distancias fueron calculadas.


def cantidad_calculos(self):

    return len(self.distancias)



# ----------------------------------------------------


# CAMBIO 9: Método puntos_dentro_radio()

# Buscar puntos que estén dentro de una distancia máxima.


def puntos_dentro_radio(self, referencia, radio, *puntos):

    resultado = []


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if distancia <= radio:

            resultado.append(punto)


    return resultado



# ----------------------------------------------------


# CAMBIO 10: Método ordenar_puntos_por_distancia()

# Retorna puntos ordenados desde el más cercano
# hasta el más lejano.


def ordenar_puntos_por_distancia(self, referencia, *puntos):

    lista = []


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        lista.append(
            (punto, distancia)
        )


    lista.sort(
        key=lambda x: x[1]
    )


    return lista



# ----------------------------------------------------


# CAMBIO 11: Mezclar con lista de puntos.


# En lugar de:

# *puntos


# Recibir:

# puntos = [(1,2),(3,4),(5,6)]



def punto_mas_cercano_lista(self, referencia, puntos):

    cercano = None

    menor = None


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if menor is None or distancia < menor:

            menor = distancia

            cercano = punto


    return cercano



# ----------------------------------------------------


# CAMBIO 12: Validar puntos incorrectos.


def validar_punto(self, punto):

    if len(punto) != 2:

        return False


    return True



# ----------------------------------------------------


# CAMBIO 13: Guardar coordenadas separadas.


# Crear atributo:


# self.puntos = []



# Guardar:

# [
# {"x":2,"y":3},
# {"x":5,"y":8}
# ]



# ----------------------------------------------------


# CAMBIO 14: Método distancia_origen()

# Calcula distancia de un punto respecto al origen (0,0).


def distancia_origen(self, punto):

    origen = (0,0)


    return self.distancia_euclidiana(
        origen,
        punto
    )



# ----------------------------------------------------


# CAMBIO 15: Método cantidad_puntos_cercanos()

# Retorna cuántos puntos están cerca de una referencia.


def cantidad_puntos_cercanos(self, referencia, limite, *puntos):

    contador = 0


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if distancia <= limite:

            contador += 1


    return contador

#EJERCICIO 19: Inventario de productos
#Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario
#(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente
#(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.

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

# POSIBLES CAMBIOS, MEZCLAS O MÉTODOS AGREGADOS
# EJERCICIO 19: Inventario de productos



# CAMBIO 1:
# Método eliminar_producto(producto)

# Permite borrar completamente un producto del inventario.



def eliminar_producto(self, producto):

    if producto in self.stock:

        del self.stock[producto]

        return True

    return False



# CAMBIO 2:
# Método consultar_stock(producto)

# Retorna la cantidad disponible de un producto.



def consultar_stock(self, producto):

    if producto in self.stock:

        return self.stock[producto]

    return 0



# CAMBIO 3:
# Método producto_mayor_stock()

# Busca el producto con mayor cantidad.
# Se realiza con lógica manual sin usar max().



def producto_mayor_stock(self):

    if len(self.stock) == 0:

        return None


    mayor = 0

    producto_mayor = None


    for producto, cantidad in self.stock.items():

        if cantidad > mayor:

            mayor = cantidad

            producto_mayor = producto


    return producto_mayor, mayor



# CAMBIO 4:
# Método productos_agotados()

# Retorna productos cuya cantidad sea igual a cero.



def productos_agotados(self):

    agotados = []


    for producto, cantidad in self.stock.items():

        if cantidad == 0:

            agotados.append(producto)


    return agotados



# CAMBIO 5:
# Método total_stock()

# Calcula la cantidad total de unidades almacenadas.



def total_stock(self):

    total = 0


    for cantidad in self.stock.values():

        total += cantidad


    return total



# CAMBIO 6:
# Método actualizar_stock(producto, cantidad)

# Cambia directamente la cantidad de un producto.



def actualizar_stock(self, producto, cantidad):

    if producto in self.stock:

        self.stock[producto] = cantidad

        return True


    return False



# CAMBIO 7:
# Agregar historial de movimientos.

# En __init__ agregar:

# self.historial = []


# Cada operación puede guardar:

# ("Mouse", "Agregado", 10)

# ("Mouse", "Retirado", 3)



# CAMBIO 8:
# Manejar productos con más información.

# En lugar de guardar solo cantidad:

# {
# "Mouse": 10
# }


# Guardar:

# {
# "Mouse": {
#     "cantidad": 10,
#     "precio": 15
# }
# }



# CAMBIO 9:
# Usar lista de tuplas en lugar de diccionario.

# Ejemplo:

# [
# ("Mouse",10),
# ("Teclado",5)
# ]


# Luego recorrer:

# for producto, cantidad in lista:



# CAMBIO 10:
# Buscar productos por rango de stock.

# Ejemplo:

# Productos entre 5 y 20 unidades.



def productos_por_rango(self, minimo, maximo):

    resultado = []


    for producto, cantidad in self.stock.items():

        if cantidad >= minimo and cantidad <= maximo:

            resultado.append(producto)


    return resultado



# CAMBIO 11:
# Método vender_producto()

# Similar a restar_stock(),
# pero pensado como una venta.



def vender_producto(self, producto, cantidad):

    if producto in self.stock:

        if self.stock[producto] >= cantidad:

            self.stock[producto] -= cantidad

            return True


    return False



# CAMBIO 12:
# Método agregar_stock_manual()

# Versión más manual sin usar "in".

# Se podría recorrer el diccionario
# buscando si existe el producto.



def agregar_stock_manual(self, producto, cantidad):

    encontrado = False


    for clave in self.stock:

        if clave == producto:

            self.stock[clave] += cantidad

            encontrado = True


    if encontrado == False:

        self.stock[producto] = cantidad

#EJERCICIO 20: Analizador de patrones en textos
#Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una listA
#(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}
#(3) tenga método palabras_unicas() usando un conjunto.
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


# POSIBLES CAMBIOS, MEZCLAS O MÉTODOS AGREGADOS
# EJERCICIO 20: Analizador de patrones en textos



# CAMBIO 1:
# Método encontrar_palabras_manual()

# Reemplaza startswith() por lógica manual.
# Compara los primeros caracteres de la palabra
# con el patrón.



def encontrar_palabras_manual(self, texto, patron):

    resultado = []


    palabras = texto.split()


    for palabra in palabras:

        coincide = True


        if len(palabra) < len(patron):

            coincide = False


        else:

            for i in range(len(patron)):

                if palabra[i] != patron[i]:

                    coincide = False


        if coincide:

            resultado.append(palabra)


    return resultado



# CAMBIO 2:
# Método agrupar_por_longitud_manual()

# Realiza la agrupación sin usar directamente
# not in para crear claves.



def agrupar_por_longitud_manual(self, texto):

    resultado = {}


    palabras = texto.split()


    for palabra in palabras:

        longitud = len(palabra)


        encontrado = False


        for clave in resultado:

            if clave == longitud:

                encontrado = True



        if encontrado:

            resultado[longitud].append(palabra)


        else:

            resultado[longitud] = [palabra]


    return resultado



# CAMBIO 3:
# Método palabras_unicas_manual()

# Busca palabras repetidas sin usar set().



def palabras_unicas_manual(self):

    unicas = []


    for palabra in self.palabras:

        repetida = False


        for elemento in unicas:

            if palabra == elemento:

                repetida = True



        if repetida == False:

            unicas.append(palabra)


    return unicas



# CAMBIO 4:
# Método contar_palabras()

# Cuenta cuántas palabras tiene un texto.



def contar_palabras(self, texto):

    palabras = texto.split()


    contador = 0


    for palabra in palabras:

        contador += 1


    return contador



# CAMBIO 5:
# Método palabra_mas_larga()

# Encuentra la palabra con mayor longitud
# sin usar max().



def palabra_mas_larga(self, texto):

    palabras = texto.split()


    if len(palabras) == 0:

        return None


    mayor = palabras[0]


    for palabra in palabras:

        if len(palabra) > len(mayor):

            mayor = palabra


    return mayor



# CAMBIO 6:
# Método palabra_mas_corta()

# Encuentra la palabra más pequeña
# sin usar min().



def palabra_mas_corta(self, texto):

    palabras = texto.split()


    if len(palabras) == 0:

        return None


    menor = palabras[0]


    for palabra in palabras:

        if len(palabra) < len(menor):

            menor = palabra


    return menor



# CAMBIO 7:
# Guardar historial de textos analizados.


# En __init__ agregar:


# self.historial = []



# En cada método agregar:


# self.historial.append(texto)



# Permite saber todos los textos procesados.



# CAMBIO 8:
# Método contar_repeticiones()

# Cuenta cuántas veces aparece cada palabra
# usando diccionario.



def contar_repeticiones(self, texto):

    frecuencia = {}


    palabras = texto.split()


    for palabra in palabras:

        if palabra in frecuencia:

            frecuencia[palabra] += 1


        else:

            frecuencia[palabra] = 1


    return frecuencia



# CAMBIO 9:
# Método buscar_palabras_por_longitud()

# Retorna palabras que tengan una longitud específica.



def buscar_por_longitud(self, texto, longitud):

    resultado = []


    palabras = texto.split()


    for palabra in palabras:

        if len(palabra) == longitud:

            resultado.append(palabra)


    return resultado



# CAMBIO 10:
# Método convertir_mayusculas()

# Convierte palabras manualmente usando upper().



def convertir_mayusculas(self, texto):

    palabras = texto.split()


    resultado = []


    for palabra in palabras:

        resultado.append(
            palabra.upper()
        )


    return resultado



# CAMBIO 11:
# Método encontrar_patron_sin_distincion()

# Busca patrones sin diferenciar mayúsculas
# y minúsculas usando lower().



def encontrar_patron_sin_distincion(self, texto, patron):

    resultado = []


    palabras = texto.split()


    patron = patron.lower()


    for palabra in palabras:

        if palabra.lower().startswith(patron):

            resultado.append(palabra)


    return resultado



# CAMBIO 12:
# Elimina palabras repetidas manteniendo el orden original sin usar set().
# Sirve para ejercicios de palabras únicas y eliminación de duplicados.


class AnalizadorPalabras:

    def __init__(self):

        self.palabras = []


    def cargar_texto(self, texto):

        self.palabras = texto.split()



    def palabras_unicas(self):

        resultado = []


        for palabra in self.palabras:

            if palabra not in resultado:

                resultado.append(palabra)


        return resultado



# Parámetros de prueba


analizador = AnalizadorPalabras()


analizador.cargar_texto(
    "python casa python carro casa libro"
)


print(analizador.palabras_unicas())



# CAMBIO 13:
# Guarda frecuencia y longitud de cada palabra usando un diccionario.
# Sirve para mezclar contador de frecuencia con análisis de texto.


class AnalizadorFrecuencia:

    def __init__(self):

        self.datos = {}



    def analizar_texto(self, texto):

        palabras = texto.split()


        for palabra in palabras:

            if palabra in self.datos:

                self.datos[palabra]["cantidad"] += 1


            else:

                self.datos[palabra] = {

                    "cantidad": 1,

                    "longitud": len(palabra)

                }


        return self.datos



# Parámetros de prueba


analizador = AnalizadorFrecuencia()


texto = "python casa python carro casa"


print(analizador.analizar_texto(texto))



# CAMBIO 14:
# Filtra palabras según una longitud mínima.
# Sirve para búsquedas y análisis de textos.


class FiltroPalabras:

    def eliminar_palabras_cortas(self, texto, minimo):

        resultado = []


        palabras = texto.split()


        for palabra in palabras:

            if len(palabra) >= minimo:

                resultado.append(palabra)


        return resultado



# Parámetros de prueba


filtro = FiltroPalabras()


texto = "sol python casa computadora"


print(
    filtro.eliminar_palabras_cortas(texto, 5)
)


def eliminar_palabras_cortas(self, texto, minimo):

    resultado = []


    palabras = texto.split()


    for palabra in palabras:

        if len(palabra) >= minimo:

            resultado.append(palabra)


    return resultado



# CAMBIO 15:
# Método invertir_palabras()

# Invierte el orden de las palabras.



def invertir_palabras(self, texto):

    palabras = texto.split()


    resultado = []


    for i in range(len(palabras)-1, -1, -1):

        resultado.append(palabras[i])


    return resultado

# CLASE 1: Calculadora
# Sirve para agrupar operaciones matemáticas como suma, promedio, conversiones y cálculos.
# Relacionado con ejercicios: 2, 3, 4, 13 y 14.


class Calculadora:

    def promedio(self, n1, n2, n3):

        return (n1 + n2 + n3) / 3


    def convertir_celsius_fahrenheit(self, celsius):

        return celsius * 1.8 + 32


    def calcular_imc(self, peso, estatura):

        return peso / (estatura ** 2)



# CLASE 2: ConversorTiempo
# Sirve para transformar segundos, minutos y horas usando división entera y residuo.
# Relacionado con ejercicios: 5, 9 y 12.


class ConversorTiempo:

    def segundos_a_hora(self, segundos):

        horas = segundos // 3600

        resto = segundos % 3600

        minutos = resto // 60

        segundos_final = resto % 60

        return horas, minutos, segundos_final



    def minutos_a_horas(self, minutos):

        horas = minutos // 60

        minutos_restantes = minutos % 60

        return horas, minutos_restantes



# CLASE 3: AnalizadorNumeros
# Sirve para analizar números mediante condiciones y operadores matemáticos.
# Relacionado con ejercicios: 8, 11 y 15.


class AnalizadorNumeros:


    def es_par(self, numero):

        return numero % 2 == 0



    def suma_digitos(self, numero):

        suma = 0

        while numero > 0:

            digito = numero % 10

            suma += digito

            numero = numero // 10


        return suma



    def es_multiplo(self, numero, multiplo):

        return numero % multiplo == 0



# CLASE 4: Cajero
# Sirve para calcular cantidades mínimas de billetes y monedas.
# Relacionado con ejercicio 10.


class Cajero:


    def calcular_billetes(self, monto):

        resultado = {}


        billetes = [50, 20, 10, 5, 1]


        for billete in billetes:

            cantidad = monto // billete

            resultado[billete] = cantidad

            monto = monto % billete


        return resultado



# CLASE 5: Producto
# Sirve para representar productos con precio, cantidad y descuentos.
# Relacionado con ejercicios 7 y 15.


class Producto:


    def __init__(self, nombre, precio, cantidad):

        self.nombre = nombre

        self.precio = precio

        self.cantidad = cantidad



    def calcular_total(self):

        return self.precio * self.cantidad



    def aplicar_descuento(self, porcentaje):

        descuento = self.precio * porcentaje

        return self.precio - descuento



# CLASE 6: Inventario
# Sirve para controlar productos almacenados y cantidades disponibles.
# Relacionado con ejercicios 7, 10 y 15.


class Inventario:


    def __init__(self):

        self.productos = {}



    def agregar_producto(self, nombre, cantidad):

        if nombre in self.productos:

            self.productos[nombre] += cantidad

        else:

            self.productos[nombre] = cantidad



    def retirar_producto(self, nombre, cantidad):

        if nombre in self.productos:

            if self.productos[nombre] >= cantidad:

                self.productos[nombre] -= cantidad

                return True


        return False



# CLASE 7: RegistroEstudiante
# Sirve para almacenar notas y calcular resultados académicos.
# Relacionado con ejercicio 2.


class RegistroEstudiante:


    def __init__(self):

        self.notas = []



    def agregar_nota(self, nota):

        self.notas.append(nota)



    def promedio(self):

        suma = 0

        for nota in self.notas:

            suma += nota


        return suma / len(self.notas)



    def aprobado(self):

        return self.promedio() >= 7



# CLASE 8: ConversorGeometrico
# Sirve para realizar cálculos de figuras geométricas.
# Relacionado con ejercicio 3.


import math


class ConversorGeometrico:


    def area_rectangulo(self, base, altura):

        return base * altura



    def perimetro_rectangulo(self, base, altura):

        return 2 * (base + altura)



    def area_circulo(self, radio):

        return math.pi * radio ** 2



    def perimetro_circulo(self, radio):

        return 2 * math.pi * radio



# CLASE 9: SistemaCompra
# Sirve para simular compras aplicando descuentos e impuestos.
# Relacionado con ejercicios 7 y 15.


class SistemaCompra:


    def calcular_total(self, precio, cantidad):

        subtotal = precio * cantidad


        if cantidad >= 10:

            descuento = subtotal * 0.15

        elif cantidad >= 5:

            descuento = subtotal * 0.05

        else:

            descuento = 0


        total = subtotal - descuento


        return total



# CLASE 10: ProcesadorTexto
# Sirve para analizar palabras, contar frecuencia y buscar patrones.
# Relacionado con ejercicios futuros de diccionarios y conjuntos.


class ProcesadorTexto:


    def contar_palabras(self, texto):

        palabras = texto.split()

        frecuencia = {}


        for palabra in palabras:

            if palabra in frecuencia:

                frecuencia[palabra] += 1

            else:

                frecuencia[palabra] = 1


        return frecuencia



    def buscar_palabra(self, texto, palabra):

        return palabra in texto.split()

#EJERCICIO 1: Saludo con nombre y edad

#Clase Persona.
#Guarda datos de una persona y tiene un método para mostrar información.


class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad


    def saludar(self):

        return f"Hola {self.nombre}, tienes {self.edad} años"



#EJERCICIO 2: Promedio de notas

#Clase Estudiante.
#Guarda notas y calcula promedio además de determinar estado.


class Estudiante:

    def __init__(self, nombre):

        self.nombre = nombre
        self.notas = []


    def agregar_nota(self, nota):

        self.notas.append(nota)


    def promedio(self):

        suma = 0

        for nota in self.notas:

            suma += nota

        return suma / len(self.notas)


    def estado(self):

        if self.promedio() >= 7:

            return "Aprobado"

        else:

            return "Reprobado"



#EJERCICIO 3: Figuras geométricas

#Clase Figura.
#Permite agrupar cálculos de áreas y perímetros.


class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura


    def area(self):

        return self.base * self.altura


    def perimetro(self):

        return 2 * (self.base + self.altura)



#EJERCICIO 4: Conversión de temperatura

#Clase Conversor.
#Agrupa diferentes conversiones.


class Conversor:

    def celsius_fahrenheit(self, celsius):

        return celsius * 1.8 + 32



#EJERCICIO 5: Conversión de segundos

#Clase Tiempo.
#Guarda segundos y los convierte en formato horas:minutos:segundos.


class Tiempo:

    def __init__(self, segundos):

        self.segundos = segundos


    def convertir(self):

        horas = self.segundos // 3600

        resto = self.segundos % 3600

        minutos = resto // 60

        segundos = resto % 60

        return horas, minutos, segundos



#EJERCICIO 6: Intercambio de valores

#Clase Intercambiador.
#Manipula valores almacenados.


class Intercambiador:

    def __init__(self, a, b):

        self.a = a
        self.b = b


    def intercambiar(self):

        self.a, self.b = self.b, self.a



#EJERCICIO 7: IVA y descuentos

#Clase Producto.
#Guarda precio y aplica operaciones comerciales.


class Producto:

    def __init__(self, precio):

        self.precio = precio


    def descuento(self, porcentaje):

        return self.precio * porcentaje


    def iva(self):

        return self.precio * 0.15


    def total(self):

        return self.precio + self.iva()



#EJERCICIO 8: Par, impar y múltiplos

#Clase Numero.
#Permite analizar características de un número.


class Numero:

    def __init__(self, valor):

        self.valor = valor


    def es_par(self):

        return self.valor % 2 == 0


    def es_multiplo(self, numero):

        return self.valor % numero == 0



#EJERCICIO 9: Tiempo en formato hh:mm:ss

#Clase Tiempo.
#Puede reutilizarse para conversiones de tiempo.


class TiempoFormato:

    def __init__(self, hora):

        self.hora = hora


    def segundos_totales(self):

        horas, minutos, segundos = self.hora.split(":")

        return int(horas)*3600 + int(minutos)*60 + int(segundos)



#EJERCICIO 10: Billetes y monedas

#Clase Cajero.
#Calcula cantidades mínimas de billetes.


class Cajero:

    def __init__(self, monto):

        self.monto = monto


    def calcular_billetes(self):

        resultado = {}

        valores = [50,20,10,5,1]

        for valor in valores:

            resultado[valor] = self.monto // valor

            self.monto %= valor


        return resultado



#EJERCICIO 11 y 23: Dígitos de números

#Clase AnalizadorNumero.
#Trabaja con divisiones y análisis de números.


class AnalizadorNumero:

    def __init__(self, numero):

        self.numero = numero


    def cantidad_digitos(self):

        numero = abs(self.numero)

        contador = 0


        while numero > 0:

            contador += 1

            numero //= 10


        return contador



#EJERCICIO 16 al 30: Ciclos, factorial, primos, Fibonacci

#Clase AnalizadorMatematico.
#Agrupa operaciones numéricas usando ciclos.


class AnalizadorMatematico:


    def factorial(self, n):

        resultado = 1

        for i in range(1, n + 1):

            resultado *= i

        return resultado



    def es_primo(self, n):

        for i in range(2, n):

            if n % i == 0:

                return False

        return True



    def fibonacci(self, cantidad):

        lista = []

        a = 0

        b = 1


        for i in range(cantidad):

            lista.append(a)

            a, b = b, a+b


        return lista



#EJERCICIO 19 y 20: Notas, máximos y mínimos

#Clase RegistroNotas.
#Guarda varias notas y permite obtener estadísticas.


class RegistroNotas:

    def __init__(self):

        self.notas = []


    def agregar(self, nota):

        self.notas.append(nota)


    def nota_mayor(self):

        mayor = self.notas[0]

        for nota in self.notas:

            if nota > mayor:

                mayor = nota

        return mayor



#EJERCICIO 26: Juego de adivinar número

#Clase Juego.
#Guarda estado del juego e intentos.


class JuegoNumero:

    def __init__(self, secreto):

        self.secreto = secreto
        self.intentos = 0


    def jugar(self, numero):

        self.intentos += 1

        return numero == self.secreto



#EJERCICIO 28: IVA con funciones

#Clase Factura.
#Reutiliza métodos para calcular valores finales.


class Factura:

    def __init__(self, precio):

        self.precio = precio


    def calcular_iva(self):

        return self.precio * 0.15


    def total(self):

        return self.precio + self.calcular_iva()



#EJERCICIO 29 y 30: Primos y números especiales

#Clase AnalizadorAvanzado.
#Combina métodos matemáticos reutilizables.


class AnalizadorAvanzado:


    def contar_primos(self, inicio, fin):

        contador = 0


        for numero in range(inicio, fin + 1):

            if self.es_primo(numero):

                contador += 1


        return contador



    def es_primo(self, numero):

        if numero <= 1:

            return False


        for i in range(2, numero):

            if numero % i == 0:

                return False


        return True

# EJERCICIO 31:
# Uso de clases para organizar funciones de un menú.
# Cada método representa una acción diferente del programa.


class Menu:

    def __init__(self):
        pass

    def saludar(self):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicación: {num1 * num2}")

        if num2 != 0:
            print(f"División: {num1 / num2}")
        else:
            print("No se puede dividir para cero")

    def mostrar_menu(self):

        while True:

            print("\n--- MENÚ ---")
            print("1. Saludar")
            print("2. Despedir")
            print("3. Calcular")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.saludar()

            elif opcion == "2":
                self.despedir()

            elif opcion == "3":
                self.calcular()

            elif opcion == "4":
                print("Programa finalizado")
                break

            else:
                print("Opción inválida")


menu = Menu()

menu.mostrar_menu()

# EJERCICIO 31: Menú con funciones separadas usando clase

class Menu:
    def saludar(self):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print("Suma:", a + b)
        print("Resta:", a - b)
        print("Multiplicación:", a * b)

        if b != 0:
            print("División:", a / b)
        else:
            print("No se puede dividir para cero")

    def iniciar(self):
        while True:
            print("\n1. Saludar")
            print("2. Despedir")
            print("3. Calcular")
            print("4. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.saludar()
            elif opcion == "2":
                self.despedir()
            elif opcion == "3":
                self.calcular()
            elif opcion == "4":
                break
            else:
                print("Opción inválida")


#Menu().iniciar()



# EJERCICIO 32

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


base = float(input("Base: "))
altura = float(input("Altura: "))

rect = Rectangulo(base, altura)

print("Área:", rect.area())



# EJERCICIO 33

class Numeros:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def maximo(self):
        return max(self.a, self.b, self.c)


n = Numeros(10, 25, 7)

print("Mayor:", n.maximo())



# EJERCICIO 34

class Año:
    def __init__(self, anio):
        self.anio = anio

    def es_bisiesto(self):
        return (self.anio % 4 == 0 and self.anio % 100 != 0) or self.anio % 400 == 0


a = Año(2024)

print(a.es_bisiesto())



# EJERCICIO 35

class Combinatoria:

    def factorial(self, n):
        resultado = 1

        for i in range(1, n + 1):
            resultado *= i

        return resultado


    def calcular(self, n, k):
        if k > n:
            return None

        return self.factorial(n) / (
            self.factorial(k) * self.factorial(n-k)
        )


c = Combinatoria()

print(c.calcular(5, 2))



# EJERCICIO 36

class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return None

        return a / b


calc = Calculadora()

print(calc.sumar(5, 3))
print(calc.restar(5, 3))
print(calc.multiplicar(5, 3))
print(calc.dividir(5, 3))



# EJERCICIO 37

class Texto:

    def __init__(self, frase):
        self.frase = frase

    def contar_vocales(self):
        contador = 0

        for letra in self.frase.lower():

            if letra in "aeiouáéíóú":
                contador += 1

        return contador


texto = Texto("Programación Python")

print("Vocales:", texto.contar_vocales())



# EJERCICIO 38

class Notas:

    def __init__(self, lista):
        self.lista = lista

    def promedio(self):
        return sum(self.lista) / len(self.lista)

    def maxima(self):
        return max(self.lista)

    def minima(self):
        return min(self.lista)


notas = Notas([7, 8.5, 6, 9, 10, 5.5])

print("Promedio:", notas.promedio())
print("Máxima:", notas.maxima())
print("Mínima:", notas.minima())

# EJERCICIO 31: Menú con funciones separadas

class Menu:
    
    def saludar(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print(f"Suma: {a + b}")
        print(f"Resta: {a - b}")
        print(f"Multiplicación: {a * b}")

        if b != 0:
            print(f"División: {a / b}")
        else:
            print("No se puede dividir para cero")

    def mostrar_menu(self):
        print("\n--- MENU ---")
        print("1. Saludar")
        print("2. Despedir")
        print("3. Calcular")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()

            opcion = input("Seleccione: ")

            if opcion == "1":
                self.saludar()

            elif opcion == "2":
                self.despedir()

            elif opcion == "3":
                self.calcular()

            elif opcion == "4":
                print("Programa finalizado")
                break

            else:
                print("Opción inválida")


#objeto = Menu()
#objeto.ejecutar()



# EJERCICIO 32: Área de rectángulo

class Rectangulo:

    def area(self, base, altura):
        return base * altura


rect = Rectangulo()

base = float(input("Base: "))
altura = float(input("Altura: "))

print(f"Área: {rect.area(base, altura)}")



# EJERCICIO 33: Máximo de tres números

class Numeros:

    def maximo(self, a, b, c):

        if a >= b and a >= c:
            return a

        elif b >= a and b >= c:
            return b

        return c


n = Numeros()

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

print(f"Mayor: {n.maximo(a,b,c)}")



# EJERCICIO 34: Año bisiesto

class Fecha:

    def es_bisiesto(self, anio):

        return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


fecha = Fecha()

anio = int(input("Ingrese año: "))

print(fecha.es_bisiesto(anio))

# EJERCICIO 3:
# Clase para calcular área y perímetro de figuras geométricas.

import math

class Figura:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.radio = 0

    def rectangulo(self):
        self.base = float(input("Base: "))
        self.altura = float(input("Altura: "))

        area = self.base * self.altura
        perimetro = 2 * (self.base + self.altura)

        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")

    def circulo(self):
        self.radio = float(input("Radio: "))

        area = math.pi * self.radio ** 2
        perimetro = 2 * math.pi * self.radio

        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")


figura = Figura()

figura.rectangulo()
figura.circulo()

# EJERCICIO 2:
# Clase para calcular promedio de notas y determinar si aprueba o reprueba.

class PromedioEstudiante:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.promedio = 0

    def ingresar_notas(self):
        self.n1 = float(input("Nota 1: "))
        self.n2 = float(input("Nota 2: "))
        self.n3 = float(input("Nota 3: "))

    def calcular_promedio(self):
        self.promedio = (self.n1 + self.n2 + self.n3) / 3

    def mostrar_resultado(self):
        if self.promedio >= 7:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"Promedio: {self.promedio:.2f}")
        print(f"Estado: {estado}")


estudiante = PromedioEstudiante()
estudiante.ingresar_notas()
estudiante.calcular_promedio()
estudiante.mostrar_resultado()

# EJERCICIO 4:
# Clase para convertir temperatura Celsius a Fahrenheit.

class ConversorTemperatura:
    def __init__(self):
        self.celsius = 0
        self.fahrenheit = 0

    def ingresar_temperatura(self):
        self.celsius = float(input("Temperatura en Celsius: "))

    def convertir(self):
        self.fahrenheit = self.celsius * 9 / 5 + 32

    def mostrar(self):
        print(f"{self.celsius}°C equivalen a {self.fahrenheit}°F")


temp = ConversorTemperatura()
temp.ingresar_temperatura()
temp.convertir()
temp.mostrar()

# EJERCICIO 5:
# Clase para convertir segundos totales a horas, minutos y segundos.

class Tiempo:
    def __init__(self):
        self.segundos_totales = 0

    def ingresar(self):
        self.segundos_totales = int(input("Segundos totales: "))

    def convertir(self):
        horas = self.segundos_totales // 3600

        resto = self.segundos_totales % 3600

        minutos = resto // 60

        segundos = resto % 60

        print(f"{horas}:{minutos:02d}:{segundos:02d}")


tiempo = Tiempo()
tiempo.ingresar()
tiempo.convertir()

# EJERCICIO 31: Menú con funciones separadas usando clases

class Menu:

    def saludar(self):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print("Suma:", a + b)
        print("Resta:", a - b)
        print("Multiplicación:", a * b)

        if b != 0:
            print("División:", a / b)
        else:
            print("No se puede dividir para cero")

    def mostrar_menu(self):

        while True:
            print("\n--- MENU ---")
            print("1. Saludar")
            print("2. Despedir")
            print("3. Calcular")
            print("4. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.saludar()

            elif opcion == "2":
                self.despedir()

            elif opcion == "3":
                self.calcular()

            elif opcion == "4":
                break

            else:
                print("Opción inválida")


menu = Menu()
#menu.mostrar_menu()



# EJERCICIO 32: Área rectángulo

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = float(input("Base: "))
altura = float(input("Altura: "))

rectangulo = Rectangulo(base, altura)

print("Área:", rectangulo.calcular_area())



# EJERCICIO 33: Máximo de tres números

class Numeros:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def maximo(self):

        if self.a >= self.b and self.a >= self.c:
            return self.a

        elif self.b >= self.a and self.b >= self.c:
            return self.b

        return self.c


a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

numeros = Numeros(a,b,c)

print("Mayor:", numeros.maximo())



# EJERCICIO 34: Año bisiesto

class Anio:

    def __init__(self, anio):
        self.anio = anio

    def es_bisiesto(self):

        return (self.anio % 4 == 0 and self.anio % 100 != 0) or self.anio % 400 == 0


anio = int(input("Ingrese año: "))

objeto = Anio(anio)

print(objeto.es_bisiesto())



# EJERCICIO 35: Factorial y combinatoria

class Matematicas:

    def factorial(self, n):

        resultado = 1

        for i in range(1,n+1):
            resultado *= i

        return resultado


    def combinatoria(self,n,k):

        if k > n or k < 0:
            return None

        return self.factorial(n) / (self.factorial(k) * self.factorial(n-k))


mat = Matematicas()

n = int(input("n: "))
k = int(input("k: "))

print("Combinatoria:", mat.combinatoria(n,k))



# EJERCICIO 36: Calculadora con clases

class Calculadora:

    def sumar(self,a,b):
        return a+b

    def restar(self,a,b):
        return a-b

    def multiplicar(self,a,b):
        return a*b

    def dividir(self,a,b):

        if b == 0:
            return None

        return a/b



calc = Calculadora()

a = float(input("Número 1: "))
b = float(input("Número 2: "))

print("Suma:", calc.sumar(a,b))
print("Resta:", calc.restar(a,b))
print("Multiplicación:", calc.multiplicar(a,b))
print("División:", calc.dividir(a,b))



# EJERCICIO 37: Contar vocales

class Texto:

    def __init__(self, frase):
        self.frase = frase


    def contar_vocales(self):

        contador = 0

        for letra in self.frase.lower():

            if letra in "aeiouáéíóú":
                contador += 1

        return contador



frase = input("Ingrese frase: ")

texto = Texto(frase)

print("Vocales:", texto.contar_vocales())



# EJERCICIO 38: Analizar notas

class Notas:

    def __init__(self, lista_notas):
        self.notas = lista_notas


    def promedio(self):

        return sum(self.notas) / len(self.notas)


    def maxima(self):

        return max(self.notas)


    def minima(self):

        return min(self.notas)



notas = [7,8.5,6,9,10,5.5]

objeto = Notas(notas)

print(f"Promedio: {objeto.promedio():.2f}")
print(f"Máxima: {objeto.maxima():.2f}")
print(f"Mínima: {objeto.minima():.2f}")


# EJERCICIO 39:
# Clase ListaDatos que elimina duplicados respetando el orden.

class ListaDatos:

    def __init__(self, lista):
        self.lista = lista

    def eliminar_duplicados(self):

        resultado = []
        vistos = set()

        for elemento in self.lista:

            if elemento not in vistos:
                resultado.append(elemento)
                vistos.add(elemento)

        return resultado

    # NUEVO MÉTODO
    def cantidad_elementos(self):

        return len(self.lista)


lista = ListaDatos(["a", "b", "a", "c", "b", "d"])

print("Lista sin duplicados:", lista.eliminar_duplicados())
print("Cantidad de elementos:", lista.cantidad_elementos())



# EJERCICIO 40:
# Clase Texto que cuenta frecuencia de palabras.

class Texto:

    def __init__(self, texto):

        self.texto = texto
        self.frecuencia = {}


    def contar_palabras(self):

        palabras = self.texto.lower().split()

        for palabra in palabras:

            self.frecuencia[palabra] = self.frecuencia.get(palabra, 0) + 1

        return self.frecuencia


    def palabra_mas_repetida(self):

        if not self.frecuencia:
            self.contar_palabras()

        return max(self.frecuencia, key=self.frecuencia.get)


    # NUEVO MÉTODO
    def cantidad_palabras(self):

        return len(self.texto.split())



texto = Texto("Python es fácil y Python es poderoso")

print(texto.contar_palabras())
print("Más repetida:", texto.palabra_mas_repetida())
print("Cantidad palabras:", texto.cantidad_palabras())



# EJERCICIO 41:
# Clase Pasajero

class Pasajero:


    def __init__(self, nombre, cedula, edad):

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad


    def cumplir_anios(self):

        self.edad += 1


    def mostrar(self):

        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")


    # NUEVO MÉTODO
    def es_mayor_edad(self):

        return self.edad >= 18



pasajero1 = Pasajero("Ana", "123456", 20)
pasajero2 = Pasajero("Luis", "987654", 15)
pasajero3 = Pasajero("Maria", "456789", 30)


pasajero1.cumplir_anios()


pasajero1.mostrar()
print("Mayor de edad:", pasajero1.es_mayor_edad())

pasajero2.mostrar()
print("Mayor de edad:", pasajero2.es_mayor_edad())

pasajero3.mostrar()
print("Mayor de edad:", pasajero3.es_mayor_edad())



# EJERCICIO 42:
# Clase CuentaBancaria

class CuentaBancaria:


    def __init__(self):

        self.saldo_actual = 0
        self.historial = []


    def depositar(self, cantidad):

        self.saldo_actual += cantidad
        self.historial.append(f"+{cantidad}")


    def retirar(self, cantidad):

        if cantidad <= self.saldo_actual:

            self.saldo_actual -= cantidad
            self.historial.append(f"-{cantidad}")

        else:

            print("Fondos insuficientes")


    def saldo(self):

        return self.saldo_actual


    def ver_historial(self):

        return self.historial


    def __str__(self):

        return f"Saldo: ${self.saldo_actual}"


    # NUEVO MÉTODO
    def cantidad_operaciones(self):

        return len(self.historial)



cuenta = CuentaBancaria()

cuenta.depositar(100)
cuenta.depositar(50)
cuenta.retirar(30)

print(cuenta)
print("Historial:", cuenta.ver_historial())
print("Operaciones:", cuenta.cantidad_operaciones())



# EJERCICIO 43:
# Clase Producto

class Producto:


    productos_creados = []


    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        Producto.productos_creados.append(self)



    def vender(self, cantidad):

        if cantidad <= self.stock:

            self.stock -= cantidad
            print("Venta realizada")

        else:

            print("No hay stock")



    def reabastecer(self, cantidad):

        self.stock += cantidad



    def valor_inventario(self):

        return self.precio * self.stock



    @classmethod
    def total_inventario(cls):

        total = 0

        for producto in cls.productos_creados:

            total += producto.valor_inventario()

        return total



    # NUEVO MÉTODO
    def tiene_stock(self):

        return self.stock > 0



    def __str__(self):

        return f"{self.nombre} - Stock: {self.stock}"



p1 = Producto("Mouse",20,10)
p2 = Producto("Teclado",30,5)


p1.vender(2)
p2.reabastecer(3)


print(p1)
print("Tiene stock:",p1.tiene_stock())

print(p2)

print("Inventario total:",Producto.total_inventario())

# EJERCICIO 39
# Clase ListaDatos para eliminar duplicados respetando orden

class ListaDatos:

    def __init__(self, lista):
        self.lista = lista

    def eliminar_duplicados(self):
        resultado = []
        vistos = set()

        for elemento in self.lista:
            if elemento not in vistos:
                resultado.append(elemento)
                vistos.add(elemento)

        return resultado

    def mostrar(self):
        print(self.lista)


datos = ListaDatos(["a", "b", "a", "c", "b", "d"])

print("Lista original:")
datos.mostrar()

print("Sin duplicados:")
print(datos.eliminar_duplicados())



# EJERCICIO 40
# Clase AnalizadorTexto para contar palabras

class AnalizadorTexto:

    def __init__(self, texto):
        self.texto = texto.lower()
        self.frecuencia = {}

    def contar_palabras(self):

        palabras = self.texto.split()

        for palabra in palabras:

            if palabra in self.frecuencia:
                self.frecuencia[palabra] += 1

            else:
                self.frecuencia[palabra] = 1

        return self.frecuencia


    def palabra_mas_repetida(self):

        mayor = 0
        palabra_mayor = ""

        for palabra, cantidad in self.frecuencia.items():

            if cantidad > mayor:
                mayor = cantidad
                palabra_mayor = palabra

        return palabra_mayor


texto = input("Ingrese un texto: ")

analizador = AnalizadorTexto(texto)

print("Frecuencia:")
print(analizador.contar_palabras())

print("Palabra más repetida:")
print(analizador.palabra_mas_repetida())



# EJERCICIO 41
# Clase Pasajero

class Pasajero:

    cantidad_pasajeros = 0

    def __init__(self, nombre, cedula, edad):

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

        Pasajero.cantidad_pasajeros += 1


    def cumplir_anios(self):

        self.edad += 1


    def mostrar(self):

        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")


    @classmethod
    def mostrar_cantidad(cls):

        print(f"Cantidad pasajeros: {cls.cantidad_pasajeros}")



pasajero1 = Pasajero("Ana", "123", 20)
pasajero2 = Pasajero("Luis", "456", 25)
pasajero3 = Pasajero("Maria", "789", 30)


pasajero1.cumplir_anios()


pasajero1.mostrar()
print()

pasajero2.mostrar()
print()

pasajero3.mostrar()

Pasajero.mostrar_cantidad()



# EJERCICIO 42
# Clase CuentaBancaria

class CuentaBancaria:

    def __init__(self, titular):

        self.titular = titular
        self._saldo = 0
        self.historial = []


    def depositar(self, cantidad):

        if cantidad > 0:

            self._saldo += cantidad
            self.historial.append(f"+{cantidad}")


    def retirar(self, cantidad):

        if cantidad <= self._saldo:

            self._saldo -= cantidad
            self.historial.append(f"-{cantidad}")

        else:

            print("Fondos insuficientes")


    def consultar_saldo(self):

        return self._saldo


    def ver_historial(self):

        return self.historial


    def cantidad_operaciones(self):

        return len(self.historial)


    def __str__(self):

        return f"Cuenta de {self.titular} - Saldo: ${self._saldo}"



cuenta = CuentaBancaria("Derick")


cuenta.depositar(500)
cuenta.depositar(200)
cuenta.retirar(100)


print(cuenta)

print("Saldo:", cuenta.consultar_saldo())

print("Historial:")
print(cuenta.ver_historial())

print("Operaciones realizadas:")
print(cuenta.cantidad_operaciones())

class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print("Venta realizada correctamente")
        else:
            print("Stock insuficiente")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print("Producto reabastecido")

    def valor_inventario(self):
        return self.precio * self.stock

    # Método nuevo: cambiar precio
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método nuevo: verificar disponibilidad
    def disponible(self):
        return self.stock > 0

    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:
            total += producto.valor_inventario()

        return total

    def __str__(self):
        return f"{self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"


producto1 = Producto("Mouse", 20, 10)
producto2 = Producto("Teclado", 35, 5)
producto3 = Producto("Monitor", 180, 3)


producto1.vender(2)
producto2.reabastecer(5)

producto3.cambiar_precio(200)


print(producto1)
print("Valor inventario:", producto1.valor_inventario())

print(producto2)
print("Valor inventario:", producto2.valor_inventario())

print(producto3)
print("Valor inventario:", producto3.valor_inventario())


productos = [producto1, producto2, producto3]


print("Total inventario:",
      Producto.total_inventario(productos))


print("¿Mouse disponible?",
      producto1.disponible())

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def area(self):
        return self.base * self.altura


    def perimetro(self):
        return 2 * (self.base + self.altura)


    # Método nuevo: cambiar dimensiones
    def cambiar_dimensiones(self, base, altura):
        self.base = base
        self.altura = altura


    # Método nuevo: verificar si es cuadrado
    def es_cuadrado(self):
        return self.base == self.altura


    def __str__(self):
        return f"Rectángulo Base: {self.base} Altura: {self.altura}"



rectangulo = Rectangulo(10, 5)


print(rectangulo)

print("Área:",
      rectangulo.area())

print("Perímetro:",
      rectangulo.perimetro())


print("¿Es cuadrado?",
      rectangulo.es_cuadrado())


rectangulo.cambiar_dimensiones(8,8)


print("\nDespués del cambio")

print(rectangulo)

print("Área:",
      rectangulo.area())

print("¿Es cuadrado?",
      rectangulo.es_cuadrado())

import math


class Circulo:


    def __init__(self, radio):
        self.radio = radio


    def area(self):
        return math.pi * self.radio ** 2


    def circunferencia(self):
        return 2 * math.pi * self.radio


    def diametro(self):
        return self.radio * 2


    # Método nuevo: cambiar radio
    def cambiar_radio(self, nuevo_radio):
        self.radio = nuevo_radio


    # Método nuevo: mostrar información
    def mostrar_datos(self):

        print("Radio:", self.radio)
        print("Área:", self.area())
        print("Circunferencia:",
              self.circunferencia())
        print("Diámetro:",
              self.diametro())



circulo = Circulo(5)


circulo.mostrar_datos()


circulo.cambiar_radio(10)


print("\nDespués del cambio")

circulo.mostrar_datos()

class Estudiante:


    def __init__(self, nombre):

        self.nombre = nombre
        self.notas = []


    def agregar_nota(self, nota):

        self.notas.append(nota)



    def promedio(self):

        return sum(self.notas) / len(self.notas)



    def aprobado(self):

        return self.promedio() >= 7



    def cantidad_notas(self):

        return len(self.notas)



    # Método nuevo: eliminar nota
    def eliminar_nota(self, posicion):

        if posicion < len(self.notas):

            self.notas.pop(posicion)



    # Método nuevo: nota más alta
    def nota_maxima(self):

        return max(self.notas)



    # Método nuevo: nota más baja
    def nota_minima(self):

        return min(self.notas)



    def mostrar(self):

        print("Nombre:",
              self.nombre)

        print("Notas:",
              self.notas)

        print("Promedio:",
              self.promedio())

        print("Aprobado:",
              self.aprobado())



estudiante = Estudiante("Derick")


estudiante.agregar_nota(8)
estudiante.agregar_nota(9)
estudiante.agregar_nota(7)


estudiante.mostrar()


print("Cantidad notas:",
      estudiante.cantidad_notas())


print("Nota máxima:",
      estudiante.nota_maxima())


print("Nota mínima:",
      estudiante.nota_minima())


estudiante.eliminar_nota(1)


print("\nDespués de eliminar")

estudiante.mostrar()


class Vehiculo:


    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.km = 0



    def recorrer(self, kilometros):

        self.km += kilometros



    def necesita_mantenimiento(self):

        return self.km >= 10000



    def reiniciar_mantenimiento(self):

        self.km = 0



    # Método nuevo: calcular costo mantenimiento

    def costo_mantenimiento(self):

        return 150



    # Método nuevo: obtener estado

    def estado(self):

        if self.necesita_mantenimiento():

            return "Necesita mantenimiento"

        else:

            return "Vehículo en buen estado"



    def __str__(self):

        return f"""
Marca: {self.marca}
Modelo: {self.modelo}
Kilómetros: {self.km}
"""



vehiculo = Vehiculo("Toyota",
                    "Corolla")


vehiculo.recorrer(12000)


print(vehiculo)


print(vehiculo.estado())


print("Costo mantenimiento:",
      vehiculo.costo_mantenimiento())


vehiculo.reiniciar_mantenimiento()


print("\nDespués del mantenimiento")


print(vehiculo)


print(vehiculo.estado())

# ==========================================
# EJERCICIO 43
# Clase Producto con métodos:
# vender(), reabastecer(), valor_inventario()
# Nuevo método: total_inventario()
# Nuevos cambios:
# - aplicar_descuento()
# - tiene_stock()
# - mostrar_estado()
# ==========================================


class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):

        if cantidad <= self.stock:
            self.stock -= cantidad
            print("Venta realizada")
        else:
            print("No existe suficiente stock")


    def reabastecer(self, cantidad):

        self.stock += cantidad


    def valor_inventario(self):

        return self.precio * self.stock


    def aplicar_descuento(self, porcentaje):

        descuento = self.precio * (porcentaje / 100)

        self.precio -= descuento


    def tiene_stock(self):

        return self.stock > 0


    def mostrar_estado(self):

        print(f"Producto: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")


    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:

            total += producto.valor_inventario()

        return total


    def __str__(self):

        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"



producto1 = Producto("Mouse", 20, 10)
producto2 = Producto("Teclado", 35, 5)
producto3 = Producto("Monitor", 200, 3)


producto1.vender(2)

producto2.reabastecer(10)

producto3.aplicar_descuento(10)


productos = [producto1, producto2, producto3]


print(producto1)
print(producto2)
print(producto3)


print("Valor total inventario:",
      Producto.total_inventario(productos))


print("Tiene stock:",
      producto1.tiene_stock())



# ==========================================
# EJERCICIO 44
# Clase Rectangulo
# Métodos:
# area()
# perimetro()
# __str__()
# Nuevos cambios:
# - cambiar_dimensiones()
# - es_cuadrado()
# ==========================================


class Rectangulo:


    def __init__(self, base, altura):

        self.base = base
        self.altura = altura



    def area(self):

        return self.base * self.altura



    def perimetro(self):

        return 2 * (self.base + self.altura)



    def cambiar_dimensiones(self, nueva_base, nueva_altura):

        self.base = nueva_base
        self.altura = nueva_altura



    def es_cuadrado(self):

        return self.base == self.altura



    def __str__(self):

        return f"Rectángulo Base:{self.base} Altura:{self.altura}"




rectangulo = Rectangulo(10,5)


print(rectangulo)

print("Área:", rectangulo.area())

print("Perímetro:", rectangulo.perimetro())


print("¿Es cuadrado?",
      rectangulo.es_cuadrado())


rectangulo.cambiar_dimensiones(8,8)


print(rectangulo)

print("¿Es cuadrado?",
      rectangulo.es_cuadrado())




# ==========================================
# EJERCICIO 45
# Clase Circulo
# Métodos:
# area()
# circunferencia()
# diametro()
# Nuevos cambios:
# - cambiar_radio()
# - es_mayor_que()
# ==========================================


import math



class Circulo:


    def __init__(self, radio):

        self.radio = radio



    def area(self):

        return math.pi * self.radio ** 2



    def circunferencia(self):

        return 2 * math.pi * self.radio



    def diametro(self):

        return self.radio * 2



    def cambiar_radio(self, nuevo_radio):

        self.radio = nuevo_radio



    def es_mayor_que(self, otro):

        return self.area() > otro.area()



    def __str__(self):

        return f"Círculo Radio: {self.radio}"




circulo1 = Circulo(5)

circulo2 = Circulo(3)



print(circulo1)

print("Área:", circulo1.area())

print("Circunferencia:",
      circulo1.circunferencia())

print("Diámetro:",
      circulo1.diametro())


print("¿Círculo 1 es mayor que círculo 2?",
      circulo1.es_mayor_que(circulo2))





# ==========================================
# EJERCICIO 46
# Clase Estudiante
# Métodos:
# agregar_nota()
# promedio()
# aprobado()
# cantidad_notas()
# Nuevos cambios:
# - nota_maxima()
# - nota_minima()
# - eliminar_nota()
# ==========================================



class Estudiante:


    def __init__(self, nombre):

        self.nombre = nombre

        self.notas = []



    def agregar_nota(self, nota):

        self.notas.append(nota)



    def promedio(self):

        return sum(self.notas) / len(self.notas)



    def aprobado(self):

        return self.promedio() >= 7



    def cantidad_notas(self):

        return len(self.notas)



    def nota_maxima(self):

        return max(self.notas)



    def nota_minima(self):

        return min(self.notas)



    def eliminar_nota(self, posicion):

        self.notas.pop(posicion)



    def mostrar(self):

        print("Nombre:", self.nombre)

        print("Notas:", self.notas)

        print("Promedio:", self.promedio())

        print("Aprobado:", self.aprobado())




estudiante = Estudiante("Derick")


estudiante.agregar_nota(8)

estudiante.agregar_nota(9)

estudiante.agregar_nota(7)


estudiante.mostrar()


print("Cantidad:",
      estudiante.cantidad_notas())


print("Nota mayor:",
      estudiante.nota_maxima())


print("Nota menor:",
      estudiante.nota_minima())




# ==========================================
# EJERCICIO 47
# Clase Vehiculo
# Métodos:
# recorrer()
# necesita_mantenimiento()
# reiniciar_mantenimiento()
# Nuevos cambios:
# - acelerar()
# - mostrar_km()
# - comparar_km()
# ==========================================



class Vehiculo:


    def __init__(self, marca, modelo):

        self.marca = marca

        self.modelo = modelo

        self.km = 0

        self.velocidad = 0



    def recorrer(self, kilometros):

        self.km += kilometros



    def necesita_mantenimiento(self):

        return self.km >= 10000



    def reiniciar_mantenimiento(self):

        self.km = 0



    def acelerar(self, aumento):

        self.velocidad += aumento



    def mostrar_km(self):

        return self.km



    def comparar_km(self, otro):

        if self.km > otro.km:

            return f"{self.marca} tiene más kilómetros"

        elif otro.km > self.km:

            return f"{otro.marca} tiene más kilómetros"

        else:

            return "Ambos tienen los mismos kilómetros"



    def __str__(self):

        return f"{self.marca} {self.modelo} - KM: {self.km} - Velocidad: {self.velocidad}"





vehiculo1 = Vehiculo("Toyota","Corolla")

vehiculo2 = Vehiculo("Mazda","3")



vehiculo1.recorrer(12000)

vehiculo2.recorrer(8000)


vehiculo1.acelerar(80)


print(vehiculo1)

print(vehiculo2)


print("Mantenimiento:",
      vehiculo1.necesita_mantenimiento())


print(vehiculo1.comparar_km(vehiculo2))


vehiculo1.reiniciar_mantenimiento()


print(vehiculo1)


# LISTAS (list)

lista = [1, 2, 3]
tupla = (4, 5)
conjunto = {6, 7}
diccionario = {"a": 1}

# append(x)
# Agrega un elemento al final de la lista.
lista.append(5)

# extend(iterable)
# Agrega todos los elementos de otra lista o colección.
lista.extend([6, 7, 8])

# insert(pos, x)
# Inserta un elemento en una posición específica.
lista.insert(1, 10)

# remove(x)
# Elimina la primera aparición del elemento indicado.
lista.remove(10)

# pop()
# Elimina y devuelve el último elemento.
lista.pop()

# pop(pos)
# Elimina y devuelve el elemento de una posición específica.
lista.pop(2)

# clear()
# Elimina todos los elementos de la lista.
lista.clear()

# index(x)
# Devuelve la posición de la primera aparición del elemento.
lista.index(5)

# count(x)
# Cuenta cuántas veces aparece un elemento.
lista.count(5)

# sort()
# Ordena la lista de menor a mayor.
lista.sort()

# sort(reverse=True)
# Ordena la lista de mayor a menor.
lista.sort(reverse=True)

# reverse()
# Invierte el orden de los elementos.
lista.reverse()

# copy()
# Crea una copia de la lista.
nueva_lista = lista.copy()

# len(lista)
# Devuelve la cantidad de elementos.
len(lista)

# sum(lista)
# Suma todos los números de la lista.
sum(lista)

# max(lista)
# Devuelve el mayor elemento.
max(lista)

# min(lista)
# Devuelve el menor elemento.
min(lista)

# sorted(lista)
# Devuelve una nueva lista ordenada sin modificar la original.
sorted(lista)

# enumerate(lista)
# Recorre la lista mostrando índice y valor.
for i, valor in enumerate(lista):
    print(i, valor)

# in
# Verifica si un elemento existe.
if 5 in lista:
    print("Existe")

# not in
# Verifica si un elemento no existe.
if 10 not in lista:
    print("No existe")



# =========================
# TUPLAS (tuple)
# =========================

# count(x)
# Cuenta cuántas veces aparece un elemento.
tupla.count(5)

# index(x)
# Devuelve la posición de un elemento.
tupla.index(5)

# len(tupla)
# Devuelve la cantidad de elementos.
len(tupla)

# max(tupla)
# Devuelve el mayor elemento.
max(tupla)

# min(tupla)
# Devuelve el menor elemento.
min(tupla)

# sum(tupla)
# Suma todos los elementos numéricos.
sum(tupla)

# sorted(tupla)
# Devuelve una lista ordenada con los elementos.
sorted(tupla)

# in
# Verifica si un elemento existe.
5 in tupla

# not in
# Verifica si un elemento no existe.
10 not in tupla



# =========================
# CONJUNTOS (set)
# =========================

# add(x)
# Agrega un elemento.
conjunto.add(5)

# update(iterable)
# Agrega varios elementos.
conjunto.update([6, 7])

# remove(x)
# Elimina un elemento. Da error si no existe.
conjunto.remove(5)

# discard(x)
# Elimina un elemento. No da error si no existe.
conjunto.discard(5)

# pop()
# Elimina un elemento cualquiera.
conjunto.pop()

# clear()
# Vacía el conjunto.
conjunto.clear()
conjunto2 = set()
# copy()
# Crea una copia.
nuevo = conjunto.copy()

# union()
# Une dos conjuntos.
conjunto.union(conjunto2)

# intersection()
# Devuelve los elementos comunes.
conjunto.intersection(conjunto2)

# difference()
# Devuelve los elementos que solo están en el primer conjunto.
conjunto.difference(conjunto2)

# symmetric_difference()
# Devuelve los elementos diferentes entre ambos conjuntos.
conjunto.symmetric_difference(conjunto2)

# issubset()
# Verifica si un conjunto está contenido en otro.
conjunto.issubset(conjunto2)

# issuperset()
# Verifica si contiene completamente a otro conjunto.
conjunto.issuperset(conjunto2)

# isdisjoint()
# Verifica si no tienen elementos en común.
conjunto.isdisjoint(conjunto2)

# len(conjunto)
# Cantidad de elementos.
len(conjunto)

# in
# Verifica si existe un elemento.
5 in conjunto

# not in
# Verifica si no existe un elemento.
10 not in conjunto



# =========================
# DICCIONARIOS (dict)
# =========================

# get(clave)
# Obtiene el valor de una clave. Devuelve None si no existe.
diccionario.get("nombre")

# get(clave, valor)
# Devuelve un valor por defecto si la clave no existe.
diccionario.get("edad", 0)

# keys()
# Devuelve todas las claves.
diccionario.keys()

# values()
# Devuelve todos los valores.
diccionario.values()

# items()
# Devuelve clave y valor.
diccionario.items()

# update()
# Agrega o actualiza varias claves.
diccionario.update({"edad": 20})

# pop(clave)
# Elimina una clave y devuelve su valor.
diccionario.pop("edad")

# popitem()
# Elimina el último par clave-valor.
diccionario.popitem()

# clear()
# Vacía el diccionario.
diccionario.clear()

# copy()
# Crea una copia.
nuevo = diccionario.copy()

# setdefault(clave, valor)
# Si la clave no existe, la crea con ese valor.
diccionario.setdefault("pais", "Ecuador")

# len(diccionario)
# Cantidad de pares clave-valor.
len(diccionario)

# in
# Verifica si existe una clave.
"nombre" in diccionario

# not in
# Verifica si una clave no existe.
"apellido" not in diccionario



# =========================
# FUNCIONES MUY USADAS EN EJERCICIOS
# =========================

# range()
# Genera una secuencia de números.
range(5)

# enumerate()
# Recorre una colección mostrando índice y valor.
enumerate(lista)
lista1=[]
lista2=[]
# zip()
# Une varias colecciones elemento por elemento.
zip(lista1, lista2)

# sorted()
# Ordena una colección y devuelve una nueva.
sorted(lista)

# reversed()
# Recorre una colección al revés.
reversed(lista)

# any()
# Devuelve True si al menos un elemento es True.
any(lista)

# all()
# Devuelve True si todos los elementos son True.
all(lista)

# abs()
# Devuelve el valor absoluto.
abs(-5)

# round()
# Redondea un número.
round(3.1416, 2)

# isinstance()
# Verifica el tipo de un objeto.
isinstance(lista, list)

# type()
# Devuelve el tipo del objeto.
type(lista)



# =========================
# COMPRENSIONES (MUY USADAS)
# =========================

# Lista por comprensión
cuadrados = [x**2 for x in range(10)]

# Lista con condición
pares = [x for x in range(20) if x % 2 == 0]

# Diccionario por comprensión
dic = {x: x**2 for x in range(5)}

# Conjunto por comprensión
conj = {x for x in range(10) if x % 2 == 0}



# =========================
# RECORRIDOS MÁS COMUNES
# =========================

# Recorrer lista
for elemento in lista:
    print(elemento)

# Recorrer lista con índice
for i, elemento in enumerate(lista):
    print(i, elemento)

# Recorrer tupla
for elemento in tupla:
    print(elemento)

# Recorrer conjunto
for elemento in conjunto:
    print(elemento)

# Recorrer claves
for clave in diccionario:
    print(clave)

# Recorrer valores
for valor in diccionario.values():
    print(valor)

# Recorrer clave y valor
for clave, valor in diccionario.items():
    print(clave, valor)


# ==========================
# CLASES EN PYTHON
# ==========================

# class
# Crea una clase.

class Persona:
    pass


# __init__(self, ...)
# Constructor. Se ejecuta automáticamente al crear un objeto.
# Sirve para inicializar los atributos.

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# self
# Representa al objeto actual.
# Permite acceder a los atributos y métodos de la misma clase.

        self.nombre
        self.edad


# ==========================
# MÉTODOS MÁS USADOS
# ==========================

# Método normal
# Realiza una acción sobre el objeto.

def saludar(self):
    print("Hola")


# Método que retorna un valor
# Devuelve información.

def area(self):
    return self.base * self.altura


# Método que modifica atributos

def cumplir_anios(self):
    self.edad += 1


# Método que recibe parámetros

def depositar(self, cantidad):
    self.saldo += cantidad


# Método que devuelve True o False

def aprobado(self):
    return self.promedio() >= 7


# ==========================
# MÉTODOS ESPECIALES
# ==========================

# __str__
# Define cómo se imprime el objeto.

def __str__(self):
    return f"{self.nombre} - {self.edad}"


# __repr__
# Representación del objeto para depuración.

def __repr__(self):
    return f"Persona('{self.nombre}', {self.edad})"


# __len__
# Permite usar len(objeto).

def __len__(self):
    return len(self.notas)


# __eq__
# Compara dos objetos con ==

def __eq__(self, otro):
    return self.nombre == otro.nombre


# __lt__
# Permite usar <

def __lt__(self, otro):
    return self.edad < otro.edad


# __gt__
# Permite usar >

def __gt__(self, otro):
    return self.edad > otro.edad


# ==========================
# DECORADORES
# ==========================

# @classmethod
# Trabaja con la clase completa, no con un objeto.
# El primer parámetro es cls.

@classmethod
def total(cls, lista):
    pass


# @staticmethod
# No necesita self ni cls.
# Es una función relacionada con la clase.

@staticmethod
def convertir_dolares(valor):
    return valor * 3.8


# @property
# Permite acceder a un método como si fuera un atributo.

@property
def nombre_completo(self):
    return self.nombre + " " + self.apellido


# ==========================
# ATRIBUTOS
# ==========================

# Atributo de instancia
# Cada objeto tiene su propia copia.

    self.nombre
    self.edad
    self.saldo


# Atributo de clase
# Lo comparten todos los objetos.

class Persona:

    especie = "Humano"


# ==========================
# FUNCIONES QUE MÁS SE USAN
# ==========================
objeto={}
# isinstance()
# Verifica si un objeto pertenece a una clase.

isinstance(objeto, Persona)


# type()
# Devuelve el tipo del objeto.

type(objeto)

persona=""
# hasattr()
# Verifica si existe un atributo.

hasattr(persona, "edad")


# getattr()
# Obtiene un atributo.

getattr(persona, "edad")


# setattr()
# Cambia o crea un atributo.

setattr(persona, "edad", 20)


# delattr()
# Elimina un atributo.

delattr(persona, "edad")


# ==========================
# HERENCIA
# ==========================

# Heredar una clase.

class Animal:
    pass

class Perro(Animal):
    pass


# super()
# Llama al constructor o métodos de la clase padre.

super().__init__()


# ==========================
# OBJETOS
# ==========================

# Crear objeto

persona = Persona("Juan", 20)


# Acceder a atributos

persona.nombre
persona.edad


# Modificar atributos

persona.edad = 25


# Llamar métodos

persona.saludar()
persona.cumplir_anios()


# ==========================
# PATRONES MUY USADOS
# ==========================
class numero:
    def __init__(self,cantidad):
        pass
# Aumentar un atributo

#self.stock += cantidad


# Disminuir un atributo
#self.stock -= cantidad


# Reiniciar un atributo

#self.saldo = 0


# Multiplicar atributos
 #return self.precio * self.stock


# Comparar

     #if self.stock >= cantidad:
      #pass


# Validar

     #if cantidad > 0:
      #pass


# ==========================
# RECORRER ATRIBUTOS
# ==========================

# Recorrer una lista de la clase

#for nota in self.notas:
 #   print(nota)


# Recorrer un diccionario

#for clave, valor in self.datos.items():
  #  print(clave, valor)


# ==========================
# MÉTODOS QUE MÁS PIDEN EN EJERCICIOS
# ==========================

# agregar()
# agregar_nota()
# agregar_producto()
# agregar_estudiante()
# agregar_libro()

# eliminar()
# eliminar_producto()
# eliminar_cliente()

# buscar()

# actualizar()

# modificar()

# vender()

# comprar()

# depositar()

# retirar()

# transferir()

# recorrer()

# reabastecer()

# promedio()

# aprobado()

# area()

# perimetro()

# volumen()

# circunferencia()

# valor_inventario()

# total_inventario()

# calcular_total()

# calcular_promedio()

# mayor()

# menor()

# ordenar()

# contar()

# mostrar()

# listar()

# imprimir()

# resumen()

# ver_historial()

# limpiar()

# reiniciar()

# necesita_mantenimiento()

# cumplir_anios()

# es_mayor()

# cambiar_nombre()

# cambiar_precio()

# cambiar_stock()

# ==========================
# PALABRAS CLAVE IMPORTANTES
# ==========================

# class
# def
# self
# cls
# return
# pass
# super
# @classmethod
# @staticmethod
# @property
# __init__
# __str__
# __repr__
# __len__
# __eq__
# __lt__
# __gt__

# ===============================
# MÉTODOS COMUNES PARA CLASES
# ===============================


# -------------------------------
# Cambiar un atributo
# -------------------------------
def cambiar_nombre(self, nuevo_nombre):
    self.nombre = nuevo_nombre


# -------------------------------
# Aumentar un valor
# -------------------------------
def aumentar(self, cantidad):
    self.valor += cantidad


# -------------------------------
# Disminuir un valor
# -------------------------------
def disminuir(self, cantidad):
    self.valor -= cantidad


# -------------------------------
# Sumar un año de edad
# -------------------------------
def cumplir_anios(self):
    self.edad += 1


# -------------------------------
# Verificar si es mayor de edad
# -------------------------------
def es_mayor(self):
    return self.edad >= 18


# -------------------------------
# Agregar elemento a una lista
# -------------------------------
def agregar(self, elemento):
    self.lista.append(elemento)


# -------------------------------
# Eliminar elemento de una lista
# -------------------------------
def eliminar(self, elemento):
    if elemento in self.lista:
        self.lista.remove(elemento)


# -------------------------------
# Vaciar una lista
# -------------------------------
def limpiar(self):
    self.lista.clear()


# -------------------------------
# Contar elementos
# -------------------------------
def cantidad(self):
    return len(self.lista)


# -------------------------------
# Verificar si existe un elemento
# -------------------------------
def existe(self, elemento):
    return elemento in self.lista


# -------------------------------
# Obtener el mayor valor
# -------------------------------
def mayor(self):
    return max(self.lista)


# -------------------------------
# Obtener el menor valor
# -------------------------------
def menor(self):
    return min(self.lista)


# -------------------------------
# Calcular promedio
# -------------------------------
def promedio(self):
    if len(self.lista) == 0:
        return 0
    return sum(self.lista) / len(self.lista)


# -------------------------------
# Sumar todos los elementos
# -------------------------------
def suma(self):
    return sum(self.lista)


# -------------------------------
# Buscar un elemento
# -------------------------------
def buscar(self, elemento):
    return elemento in self.lista


# -------------------------------
# Ordenar lista
# -------------------------------
def ordenar(self):
    self.lista.sort()


# -------------------------------
# Ordenar de mayor a menor
# -------------------------------
def ordenar_desc(self):
    self.lista.sort(reverse=True)


# -------------------------------
# Invertir lista
# -------------------------------
def invertir(self):
    self.lista.reverse()


# -------------------------------
# Obtener último elemento
# -------------------------------
def ultimo(self):
    if len(self.lista) > 0:
        return self.lista[-1]
    return None


# -------------------------------
# Obtener primer elemento
# -------------------------------
def primero(self):
    if len(self.lista) > 0:
        return self.lista[0]
    return None


# -------------------------------
# Vaciar historial
# -------------------------------
def borrar_historial(self):
    self.historial.clear()


# -------------------------------
# Agregar al historial
# -------------------------------
def agregar_historial(self, texto):
    self.historial.append(texto)


# -------------------------------
# Mostrar historial
# -------------------------------
def ver_historial(self):
    for dato in self.historial:
        print(dato)


# -------------------------------
# Reiniciar un valor
# -------------------------------
def reiniciar(self):
    self.valor = 0


# -------------------------------
# Activar estado
# -------------------------------
def activar(self):
    self.activo = True


# -------------------------------
# Desactivar estado
# -------------------------------
def desactivar(self):
    self.activo = False


# -------------------------------
# Cambiar estado
# -------------------------------
def cambiar_estado(self):
    self.activo = not self.activo


# -------------------------------
# Verificar estado
# -------------------------------
def esta_activo(self):
    return self.activo


# -------------------------------
# Agregar dinero
# -------------------------------
def depositar(self, cantidad):
    self.saldo += cantidad


# -------------------------------
# Retirar dinero
# -------------------------------
def retirar(self, cantidad):
    if cantidad <= self.saldo:
        self.saldo -= cantidad
        return True
    return False


# -------------------------------
# Mostrar saldo
# -------------------------------
def mostrar_saldo(self):
    return self.saldo


# -------------------------------
# Aplicar descuento
# -------------------------------
def aplicar_descuento(self, porcentaje):
    self.precio -= self.precio * porcentaje / 100


# -------------------------------
# Incrementar precio
# -------------------------------
def aumentar_precio(self, porcentaje):
    self.precio += self.precio * porcentaje / 100


# -------------------------------
# Calcular IVA
# -------------------------------
def precio_con_iva(self):
    return self.precio * 1.15


# -------------------------------
# Vender unidades
# -------------------------------
def vender(self, cantidad):
    if cantidad <= self.stock:
        self.stock -= cantidad
        return True
    return False


# -------------------------------
# Reabastecer
# -------------------------------
def reabastecer(self, cantidad):
    self.stock += cantidad


# -------------------------------
# Hay stock
# -------------------------------
def hay_stock(self):
    return self.stock > 0


# -------------------------------
# Inventario total
# -------------------------------
def valor_inventario(self):
    return self.precio * self.stock


# -------------------------------
# Recorrer kilómetros
# -------------------------------
def recorrer(self, km):
    self.km += km


# -------------------------------
# Reiniciar odómetro
# -------------------------------
def reiniciar_km(self):
    self.km = 0


# -------------------------------
# Necesita mantenimiento
# -------------------------------
def necesita_mantenimiento(self):
    return self.km >= 10000


# -------------------------------
# Aprobar
# -------------------------------
def aprobado(self):
    return self.promedio() >= 7


# -------------------------------
# Agregar nota
# -------------------------------
def agregar_nota(self, nota):
    self.notas.append(nota)


# -------------------------------
# Mostrar cantidad de notas
# -------------------------------
def cantidad_notas(self):
    return len(self.notas)


# -------------------------------
# Agregar elemento a un conjunto
# -------------------------------
def agregar_conjunto(self, dato):
    self.conjunto.add(dato)


# -------------------------------
# Eliminar elemento de un conjunto
# -------------------------------
def eliminar_conjunto(self, dato):
    self.conjunto.discard(dato)


# -------------------------------
# Agregar dato a un diccionario
# -------------------------------
def agregar_diccionario(self, clave, valor):
    self.diccionario[clave] = valor


# -------------------------------
# Obtener dato de un diccionario
# -------------------------------
def obtener_diccionario(self, clave):
    return self.diccionario.get(clave)


# -------------------------------
# Eliminar dato de un diccionario
# -------------------------------
def eliminar_diccionario(self, clave):
    self.diccionario.pop(clave, None)


# -------------------------------
# Contar claves del diccionario
# -------------------------------
def cantidad_claves(self):
    return len(self.diccionario)


# -------------------------------
# Mostrar información del objeto
# -------------------------------
def __str__(self):
    return f"{self.nombre}"