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

elif letra.isdigit():

#por:

elif self.es_digito(letra):


#Y cambiar:

elif letra.isalpha():

#por:

elif self.es_consonante(letra):



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