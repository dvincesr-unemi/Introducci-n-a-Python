#ASIGNATURA: ESTRUCTURA DE DATOS 
#DOCENTE: ING. DANIEL VERA 
#ESTUDIANTE: DERICK VINCES RONQUILLO

#EJERCICIO 1: Leer el nombre del usuario, su edad; saludarlo por su nombre y mostrar su edad.

#1. Entender el problema 
#Entrada: nombre(str) y edad (int)
#Proceso: Concatenar nombre y edad para mostrar un saludo
#Salida: print (Hola {nombre}, tienes {edad} años)

#2. Bosquejo a mano
# nombre= input("Mensaje")
# edad= int(input("Mensaje"))
# print (f"Hola, {nombre}, tienes {edad} años")

#3. Descubrir el patron
#simplemente se debe mostrar un mensaje usando print

#4. Escribrir el coddigo 
def saludar_edad():
    nombre = input( "Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    print (f"Hola {nombre}, tienes {edad} años")

#saludar_edad()

#5. Prueba de escritorio 

#EJERCICIO 2: Leer tres notas de un estudiante y mostrar su promedio
#Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 y «Reprueba» si no. (Necesitas el if del módulo 3).

#1. Entender el problema
#Entrada: n1 (float), n2 (float), n3 (float)
#Proceso: Sumar (n1 + n2 + n3) y dividir (/) para la cantidad de notas (3)
#Utilizar condiciones (if, else) para calcular si esta aprobado o no 
#Salida: Mediante un print() se mostrara un mensaje con su promedio final y ademas su estado (aprobado o reprobado)

#2. Bosquejo a mano
# n1= float(input("Mensaje"))
# n2= float(input("Mensaje"))
# n3= float(input("Mensaje"))
# promedio= (n1 + n2 + n3)/3
#estado= ""
# if promedio >= 7 estado= "Aprobado" else estado = "Reprobado"
# print ("Tu promedio final es {promedio} y tu estado es {estado}" )

#3. Descubrir patron 
# Se reciben 3 notas, se calcula su promedio y se realizan condiciones para definir su estado ("Aprobado o reprobado")

#4. Escribir el codigo
def promedio_estado():
    n1= float(input("Ingrese la nota #1: "))
    n2= float(input("Ingrese la nota #2: "))
    n3= float(input("Ingrese la nota #3: "))
    promedio= (n1 + n2 + n3)/ 3
    estado= ""

    if promedio >= 7: 
        estado= "Aprobado"
    else:
        estado= "Reprobado"

    print (f"Tu promedio final es {promedio:.2f}, y tu estado es {estado}")

#promedio_estado()

#5. Prueba de escritorio 

#EJERCICIO 3: Leer la base y la altura de un rectángulo y mostrar su área y su perímetro. 
#Recuerda: área = base × altura, perímetro = 2 × (base + altura).
#Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r). Usa import math y math.pi

#1. Entender el problema 
#En este caso tenemos dos calculos distintos, por lo tanto es mejor dividirlo en dos funciones 
#Se debe impotar math

#def rectangulo():
#Entrada: Solicitar mediante input el valor de la base (float) y el valor de la altura (float)
#Proceso: Aplicar los calculos correspondientes en este caso: área = base × altura, perímetro = 2 × (base + altura).
#Salida: Mostrar el area y el perimetro mediante un print 

#def circulo():
#Entrada: Solicitar mediante input el valor del radio del circulo (float)
#Proceso: Aplicar los calculos correspondientes: área (π·r²) y perímetro (2·π·r). Usa import math y math.pi
#Salida: Mostrar area y el perimetro mediante un print

#2. Bosquejo a mano 
#importar math
# def rectangulo():
# base= float(input("Mensaje"))
# altura= float(input("Mensaje"))
# area= base * altura 
# perimetro = 2 * (base + altura )
# print("El area es {area} y el perimetro es {perimetro}")

#def circulo():

#radio= float(input("Mensaje"))
#area= math.pi * radio ** 2
#perimetro= 2 * math.pi * radio 
#print ("El area es {area} y el perimetro es {perimetro}")

#3. Descubrir el patron
#En ambos caso se reciben datos por parte del usuario y se realizan los calculos correspondientes mediante la aplicacion de formulas segun la figura geometrica 

#4. Escribir codigo 
import math

def rectangulo():
    base = float(input("Ingrese la base de su rectangulo: "))
    altura = float(input("Ingrese la altura de su rectangulo: "))

    area = base * altura
    perimetro = 2 * (base + altura) 

    print (f"Para un rectangulo de base: {base:.2f} y altura: {altura:.2f}; su area es: {area:.2f} y su perimetro es: {perimetro:.2f}")

#rectangulo()

def circulo():
    radio = float(input("Ingrese el radio del circulo: "))

    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio 

    print (f"Para un circulo de radio: {radio:.2f}, su area es: {area:.2f} y su perimnetro es: {perimetro:.2f}")

#circulo()

#EJERCICIO 4: Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
#1. Entender el problema 
#Entrada: Celsius: float(input("Mensaje")
#Proceso: Fahrenheit: Celsius × 9/5 + 32.
#Salida: Mensaje con los grados en F

#2. Bosquejo a mano
#Celsius=  float(input("Mensaje")
#Fahrenheit= Celsius × 9/5 + 32
#print({Fahrenheit})

#3. Descubrir el patron 
# Simplemente se usa la formula para convertir grados celcius en fahrenheit 

#4. Escribir el codigo

def convertir_grados_CF():
    celsius = float(input("Ingrese la temperatura en °Celsius: "))
    fahrenheit = celsius * 1.8 + 32

    print(f"{celsius:.2f}°C equivale a {fahrenheit:.2f}°F")

#convertir_grados_CF()

#5. Prueba de escritorio 

#EJERCICIO 5: Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.

#1. Entender el problema 
#Entrada: total_segundos= int(input("Mensaje"))
#Proceso: Usar// (división entera) y % (residuo). El formato {n:02d} rellena con ceros a la izquierda hasta 2 dígitos.
#Salida: Mensaje con el formato 1:02:05

#2. Bosquejo a mano
#total_segundos= int(input("Mensaje"))
#horas = total_segundos//3600
#resto = total_segundos % 3600
#minutos = resto // 60
#segundos = resto % 60
#print("mensaje")

#3. Descubrir el patron 
#Se toman los segundos totales y se usa // 3600 para obtener la hora
#Despues se crea una variable extra para tomar los segundos sobrantes mediante % 3600
#Para calcular los minutos se usan los segundos sobrantes // 60
#Para obtener los segundos que en este caso ya es el sobrante final se usa % 60 
#Se muestra un mensaje 

#4. Escribir el codigo 
def trans_seg():
    total_segundos = int(input("Ingrese los segundos totales: "))
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    minutos = resto // 60
    segundos = resto % 60

    print (f"{total_segundos} equivale a: {horas}:{minutos:02d}:{segundos:02d}")

#trans_seg()

#5. Prueba de escritorio 

#EJERCICIO 6: Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.

#1. Entender el problema 
#Entrada: 2 variables (int)
#Proceso: Intercambio pythónico (a, b = b, a)
#Salida: Valores intercambiados 

#2. Bosquejo a mano
#a= int(input("Mensaje"))
#b= int(input("Mensaje"))
#a, b = b, a 
#print({a} {b})

#3. Descubrir el patron 
# Se reciben dos variables y se intercambian sus valores usando a, b = b, a

#4. Escribir el codigo 
def intercam_valores():
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))

    a, b = b, a

    print (f"a: {a}, b: {b}")

#intercam_valores()

#5. Prueba de escritorio
#EJERCICIO 7: Leer el precio de un producto sin IVA y mostrar el IVA y el precio final. El IVA en Ecuador es 15%.
#Añadir un descuento del 10% que se aplique antes del IVA. Muestra los tres valores: descuento, iva, total

#1. Entender el problema
#Entrada: Precio de un producto (float)
#Proceso: Aplicar primero el descuento y despues el iva correspondiente 
#Salida:  Muestra los tres valores: descuento, iva, total

#2. Bosquejo a mano
#precio=float(input("mensaje"))
#descuento= precio * 0.10
#precio_des= precio - descuento
#iva= precio_des + (precio_des * 0.15)
#mostrar mensaje mediante print 

#3. Descubrir el patron 
#se recibe un precio al cual se le calcula un descuento del 10% y al final se le agrega un iva del 15%

#4. Escribir codigo
def iva_descuento():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = precio * 0.10
    precio_des = precio - descuento
    iva = precio_des * 0.15
    total = precio_des + iva

    print(f"Valor inicial: ${precio:.2f}")
    print(f"Descuento del 10% aplicado: ${descuento:.2f}, por lo que el nuevo valor seria ${precio_des:.2f}")
    print(f"IVA del 15% aplicado: ${iva:.2f} ")
    print(f"Total a pagar ${total:.2f}")

iva_descuento()

#Prueba de escritorio








