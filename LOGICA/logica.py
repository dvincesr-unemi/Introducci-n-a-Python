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
#iva = precio_des * 0.15
#total = precio_des + iva
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

#iva_descuento()

#5. Prueba de escritorio

#EJERCICIO 8: Leer un número entero y determinar si es par o impar
#Modifícalo para que además diga si es múltiplo de 3, de 5, o de ambos.

#1. Entender el problema
#Entrada: Variable (int)
#Proceso: Usar valor % (int) para aplicar las condiciones 
#Salida: Mostrar si es par o impar, mutiplo de 3 o de 5 mediante un print 

#2. Bosquejo a mano
#numero=int(input("Mensaje"))
#if numero % 2 ==0: es par
#else: es impar 
#if numero % 3 == 0 and numero % 5 == 0
#elif numero %3 == 0: es mutiplo de 3
#elif numero % 5 == 0: es mutiplo de 5
#else: no es mutiplo ni de 3 ni de 5 

#3. Descubrir el patron 
#Smplemente de usan condiciones en este caso aplicando % ya que para que sea par o mutiplo al aplicar % debe ser 0

#4. Escribir codigo 
def par_impar_muti():
    numero = int(input("Ingrese un numero para saber si es par, impar, mutiplo de 3, de 5 o de ambos: "))

    if numero % 2 == 0:
        print("El numero es par.")
    else: 
        print ("El numerp es impar.")

    if numero % 3 == 0 and numero % 5 == 0:
        print ("El mutiplo de 3 y de 5 a la vez.")
    elif numero % 3 == 0:
         print ("Es multiplo de 3")
    elif numero % 5 == 0: 
         print ("Es mutiplo de 5")
    else:
         print("No es multiplo ni de 3 ni de 5. ")

#par_impar_muti()

#5: Prueba de escritorio

#EJERCICIO 9: Leer hh:mm:ss y convertir a segundos totales. 

#1.Entender el problema 
#Entrada: Tiempo en el formato 1:02:04
#Proceso: Uso de split() para convertir el tiempo en una lista por posiciones (Horas, minutos, segundos)
#Salida: Mostrar los segundos totales mediante print 

#2. Bosquejo a mano
#tiempo = input("Mensaje")
#horas, minutos, segundos = tiempo.split(":")
# total_segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)
#Mensaje mediante print

#3. Descubrir el patron
#Se recibe el tiempo total el formato h:min:seg, se debe transformar a segundos totales, mediante un solo input el usuario ingresa el tiempo
#Se usa Split() para separar horas, minutos y segundos en una lista 
#Se realizan los calculos correspondientes 

#4. Escribir codigo 

def tiempot_seg():
    tiempo = input("Ingrese la hora (hh:mm:ss): ")
    horas, minutos, segundos = tiempo.split(":")
    total_segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)

    print(f"Total de segundos: {total_segundos}")

#tiempot_seg()

 #5. Prueba de escritorio 

#EJERCICIO 10: Un cajero solo tiene billetes de $50 $20, $10, $5 y $1. Dado un monto, mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
#Después probar con monedas de $0.25, $0.10, $0.05 y $0.01 (necesitas trabajar con centavos).

#1.Entender el problema
#Entrada: monto (int)
#Proceso: Dividir sucesivamente de mayor a menor usando // y %
#Salida: Cantidad de billetes de cada tipo

#2. Bosquejo a mano
#monto = int(input("Mensaje"))
#b50 = monto // 50
#monto = monto % 50
#b20 = monto // 20
#monto = monto % 20
#b10 = monto // 10
#monto = monto % 10
#b5 = monto // 5
#monto = monto % 5
#b1 = monto // 1

#3. Descubrir el patron 
#En cada paso agarras la mayor denominación que quepa. Trabajamos siempre con el resto, no con el monto original.

#4. Escribir codigo
def billetes():
    monto = int(input("Ingrese el monto total: "))

    b50 = monto // 50 
    monto = monto % 50

    b20 = monto // 20
    monto = monto % 20

    b10 = monto // 10
    monto = monto % 10

    b5 = monto // 5
    monto = monto % 5

    b1 = monto // 1

    print(f"$50 × {b50}")
    print(f"$20 × {b20}")
    print(f"$10 × {b10}")
    print(f"$5  × {b5}")
    print(f"$1  × {b1}")

#billetes()

#5. Prueba de escritorio

#Con monedas es casi igual, pero usaremos centavos = round(monto * 100) para mayor precision con los decimales 
#Escribir codigo:

def monedas ():
    monto = float(input("Ingrese el monto total en dolares: "))
    centavos = round(monto * 100)

    m25 = centavos // 25
    centavos = centavos % 25

    m10 = centavos // 10
    centavos = centavos % 10

    m5 = centavos // 5
    centavos = centavos % 5

    m1 = centavos

    print("\nCantidad de monedas:")
    print(f"25¢: {m25}")
    print(f"10¢: {m10}")
    print(f"5¢ : {m5}")
    print(f"1¢ : {m1}")

#monedas()
#Prueba de escritorio 

#EJERCICIO 11: Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo: 435 → 4+3+5 = 12.
#1.Entender el problema
#Misma logica del problema anterior, que en esta ocasion se debe sumar  suma = centenas + decenas + unidades 

#2. Bosquejo a mano 
#Misma logica del problema anterior, que en esta ocasion se debe sumar  suma = centenas + decenas + unidades 

#3. Descubrir el patron 
##Misma logica del problema anterior, que en esta ocasion se debe sumar  suma = centenas + decenas + unidades 

#4. Escribir codigo

def suma_digitos():
    numero = int(input("Ingrese un numero de 3 cifras: "))

    centenas = numero // 100 
    numero = numero % 100

    decenas = numero // 10
    numero = numero % 10

    unidades = numero

    suma = centenas + decenas + unidades 

    print (f"Suma: {suma}")

#suma_digitos()

#5. Prueba de escritorio 
                 
#EJERCICIO 12: Lee una cantidad de minutos y muéstrala como «X horas Y minutos». Ejemplo: 135 → «2 horas 15 minutos».
#1.Entender el problema
#Misma logica del problema anterior

#2. Bosquejo a mano 
#Misma logica del problema anterior

#3. Descubrir el patron 
##Misma logica del problema anterior 

#4. Escribir codigo
def minutos_horasm():
    minutos_totales = int(input("Ingrese el tiempo total en minutos: "))

    horas = minutos_totales // 60
    minutos = minutos_totales % 60

    print(f"{horas} horas {minutos} minutos")

#minutos_horasm()

#5. Prueba de escritorio 

#EJERCICIO 13: Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: IMC = peso / estatura². Muestra el IMC con 2 decimales.

#1. Entender el problema
#Entrada: Se lee peso (float) y estatura (float)
#Proceso: Se aplica el calculo para IMC (IMC = peso / estatura² )
#Salida: Se usa print para mostrar el resultado en este caso su IMC redondeado a dos decimales 

#2. Bosquejo a mano 
#peso(float)
#estatura(float)
#imc = peso / estatura ** 2
#print( {imc})

#3. Descubrir el patron 
#Se reciben dos variables (float) y se le aplica el calculo correspondiente en este caso para calcular el IMC

#4. Escribir codigo 

def imc():
    peso = float(input("Ingrese su peso (kg): "))
    estatura = float(input("Ingrese su estatura (m): "))

    imc_v = peso / (estatura ** 2 )

    print (f"Su Indice de Masa Corporal es: {imc_v:.2f}")

#imc()
#5. Prueba de escritorio 


#EJERCICIO 14: Lee un número decimal y una cantidad de decimales, y muéstralo redondeado. Ejemplo: 3.14159 con 2 decimales → 3.14.
#1. Entender el problema 
#Entrada: decimal(float), redondeo(int)
#Proceso: resultado = round(decimal, redondeo)
#Salida: Mensaje con el numero redondeado

#2. Bosquejo a mano
#decimal(float), redondeo(int)
#resultado =  round(decimal, redondeo)
#print({resultado})

#3. Descubrir el patron 
#Se recibe un numero decimal, segun lo que el usuario desee se redondeara usando round(decimal, redondeo)

#4. Escribir codigo
def decimal_redondeo():
    decimal = float(input("Ingrese el numero decimal: "))
    redondeo = int(input("¿A cuantas cifras desea redondearlo?: "))

    resultado = round (decimal, redondeo)

    print(resultado)

#redondeo()

#5. Prueba de escritorio 

#EJERCICIO 15: Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si compras entre 5 y 9 te dan 5%. Calcula el total.

#1. Entender el problema 
#Entrada: Se tiene un precio inicial de 12 y se le solicita al usuario que ingrese cuantos productos compro a ese precio 
#Proceso: Se usan condiciones (if, else)
#Salida: Se muestra el total a pagar 

#2. Bosquejo a mano
##Entrada:
# cantidad = int(input("Mensaje"))

#Proceso:
# Si cantidad >= 10 → descuento = 15%
# Si cantidad >= 5 → descuento = 5%
# Caso contrario → descuento = 0%
# Calcular subtotal
# Calcular descuento
# Calcular total
#Salida: Mostrar subtotal, descuento y total a pagar

#3. Descubrir el patron
#Simplemente se usan condiciones para establecer el descuento 

#4. Escribir codigo 

def descuento():
    PRECIO = 12 
    cantidad = int(input("Cantidad: "))

    if cantidad >= 10:
        descuento = 0.15
    elif cantidad >= 5:
        descuento = 0.05
    else:
        descuento = 0

    precio_inicial = PRECIO * cantidad
    valor_descueto = precio_inicial * descuento
    total = precio_inicial - valor_descueto

    print(f"Precio unitario: {PRECIO}")
    print(f"Cantidad a comprar: {cantidad}")
    print(f"Total inicial a pagar: {precio_inicial:.2f}")
    print(f"Descuento aplicado en %: {int(descuento * 100)}%")
    print(f"Descuento aplicado en $: {valor_descueto:.2f}")
    print(f"Total final a pagar: {total:.2f}")

#descuento()
#5. Prueba de escritorio 

#EJERCICIO 16: Leer un número N y mostrar los números del 1 al N.
#1. Entender el problema
#Entrada: Se ingresa un numero (sera N segun el problema )
#Proceso: Se usa un proceso repetitivo (for) para mostrar los numeros de 1 a N
#Salida: Se incluye el print dentro del ciclo para mostrar los numeros del 1 a N

#2. Bosquejo a mano
#Es necesario usar un ciclo for para mostrar los numeros del 1 a N, en este caso se usara range(1, n + 1)
#Si fuera a mano sin for se deberia hacer print(1), print(2), print(3).... hasta llegar a N, pero esto no es eficiente

#3. Descubrir el patron
#Se usa un ciclo for para mostrar los numeros del 1 a N, en este caso se usara range(1, n + 1)

#4. Escribir codigo
def primerfor(n):
    for i in range (1, n + 1):
        print(i)
#primerfor(10)

#Tambien se puede hacer que vaya al reves, es decir de N a 1, para esto se usa range(n, 0, -1)
def primerfor_reves(n):
    for i in range( n, 0, -1):
        print(i)
#primerfor_reves(10)

#5. Prueba de escritorio

#EJERCICIO 17: Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
#1. Entender el problema
#Entrada: Se ingresa un numero (sera N segun el problema )
#Proceso: Se usa un proceso repetitivo (for) para sumar los numeros de 1 a N
#Salida: Se incluye el print fuera del ciclo para mostrar la suma de los numeros del 1 a N

#2. Bosquejo a mano
#Es necesario usar un ciclo for para sumar los numeros del 1 a N, en este caso se usara range(1, n + 1)
# Leer N
# suma = 0
# Repetir desde 1 hasta N
# Sumar el número actual a la variable suma
# Mostrar la suma

#3. Descubrir el patron
#Se usa un ciclo for para sumar los numeros del 1 a N, en este caso se usara range(1, n + 1)

#4. Escribir codigo
def suma_numeros(n):
    suma = 0 
    for i in range (1, n +1):
        suma += i
    return suma
#print(suma_numeros(10))

#Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).
def suma_pares(n):
    suma = 0 
    for i in range (2, n +1, 2):
        suma += i
    return suma
#print(suma_pares(100))

#5. Prueba de escritorio

#EJERCICIO 18: Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.
#1. Entender el problema
#Entrada: Se ingresa un numero (sera N segun el problema )
#Proceso: Se usa un proceso repetitivo (for) para multiplicar los numeros de 1 a N
#Salida: Se incluye el print fuera del ciclo para mostrar el factorial de los numeros del 1 a N

#2. Bosquejo a mano
#Es necesario usar un ciclo for para multiplicar los numeros del 1 a N, en este caso se usara range(1, n + 1)
# Leer N
# factorial = 1
# Repetir desde 1 hasta N
# Multiplicar el número actual a la variable factorial
# Mostrar el factorial  

#3. Descubrir el patron
#Se usa un ciclo for para multiplicar los numeros del 1 a N, en este caso se usara range(1, n + 1)

#4. Escribir codigo
def factorial(n): 
    factorial = 1
    for i in range (1, n + 1):
        factorial *= i
    return factorial
#print(factorial(5))

#¿Qué pasa con N muy grande (100!)? Python maneja enteros infinitos, pruébalo. En JS con enteros normales explotaría.
#print(factorial(100))

#5. Prueba de escritorio

#EJERCICIO 19: Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 70).
#1. Entender el problema
#Entrada: Se ingresa un numero (sera N segun el problema ) y luego se ingresan las notas de los estudiantes (una por una)
#Proceso: Se usa un proceso repetitivo (for) para contar cuantas notas son mayores o iguales a 70
#Salida: Se muestra el conteo de estudiantes que aprobaron

#2. Bosquejo a mano
#Es necesario usar un ciclo for para contar cuantas notas son mayores o iguales a 70        
# Leer N
# contador_aprobados = 0    
# Repetir N veces
# Leer nota 
# Si nota >= 70, incrementar contador_aprobados
# Mostrar contador_aprobados

#3. Descubrir el patron
#Se usa un ciclo for para contar cuantas notas son mayores o iguales a 70   

#4. Escribir codigo

def contar_aprobados(n):
    contador_aprobados = 0
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota >= 70:
            contador_aprobados += 1
    return contador_aprobados
#print(f"Cantidad de estudiantes aprobados: {contar_aprobados(5)}") 

#Añade un contador para reprobados y muestra el porcentaje de aprobación.

def contar_aprobados_reprobados(n):
    contador_aprobados = 0
    contador_reprobados = 0 
    for i in range (1, n+1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota >= 70:
            contador_aprobados += 1
        else:
            contador_reprobados += 1
    porcentaje_aprobados = (contador_aprobados / n) * 100
    porcentaje_reprobados = (contador_reprobados / n) * 100
    return contador_aprobados, contador_reprobados, porcentaje_aprobados, porcentaje_reprobados
#resultado = contar_aprobados_reprobados(5)

#print(f"Cantidad de estudiantes aprobados: {resultado[0]}")
#print(f"Cantidad de estudiantes reprobados: {resultado[1]}")
#print(f"Porcentaje de estudiantes aprobados: {resultado[2]}%")
#print(f"Porcentaje de estudiantes reprobados: {resultado[3]}%")

#5. Prueba de escritorio

#EJERCICIO 20: Leer las notas de N estudiantes y mostrar la nota más alta.
#1. Entender el problema
#Entrada: Se ingresa un numero (sera N segun el problema ) y luego se ingresan las notas de los estudiantes (una por una)
#Proceso: Se usa un proceso repetitivo (for) para comparar las notas y obtener la nota mas alta
#Salida: Se muestra la nota mas alta                                                                                

#2. Bosquejo a mano
#Es necesario usar un ciclo for para comparar las notas y obtener la nota mas alta
# Leer N

#4. Escribir codigo
def nota_mas_alta(n):
    nota_maxima = float('-inf')  
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota > nota_maxima:
            nota_maxima = nota
    return nota_maxima

#Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.
def nota_mas_baja(n):
    nota_minima = float('inf')
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota < nota_minima:
            nota_minima = nota
    return nota_minima

#5. Prueba de escritorio

#EJERCICIO 21: Leer un número y determinar si es primo (solo divisible entre 1 y él mismo), CON BANDERAS Y BREAK. Ejemplo: 7 es primo, 8 no es primo.
#1. Entender el problema
#Entrada: Se ingresa un numero (sera N segun el problema )
#Proceso: Se usa un proceso repetitivo (for) para verificar si el numero es divisible entre algun numero entre 2 y n-1
#Salida: Se muestra si el numero es primo o no

#2. Bosquejo a mano
#Es necesario usar un ciclo for para verificar si el numero es divisible entre algun numero entre 2 y n-1
# Leer N
# bandera = False
# for i in range(2, N):
#     if N % i == 0:
#         bandera = True
#         break
# if not bandera:
#     print("El número es primo")
# else:
#     print("El número no es primo")

#3. Descubrir el patron
#Se usa un ciclo for para verificar si el numero es divisible entre algun numero entre 2 y n-1, si es divisible se cambia la bandera a True y se rompe el ciclo con break

#4. Escribir codigo
def es_primo(n):
    if n <= 1:
        return False
    divisor_extra = False
    for i in range(2, n):
        if n % i == 0:
            divisor_extra = True
            break
    return not divisor_extra
#Genera una lista de todos los primos entre 2 y 100.
#primos = [i for i in range(2, 101) if es_primo(i)]
#print("Números primos entre 2 y 100:", primos)

#5. Prueba de escritorio

#EJERCICIO 22: Lee un número N y muestra su tabla de multiplicar (del 1 al 12).

#1. Entender el problema
#Entrada: Se ingresa un número (N).
#Proceso: Se utiliza un ciclo for para recorrer los números del 2 al 12 y multiplicarlos por N.
#Salida: Se muestra la tabla de multiplicar del número ingresado.

#2. Bosquejo a mano
# Leer N
# Repetir desde 2 hasta 12
#     Multiplicar N por el número actual
#     Mostrar la operación y el resultado

#3. Descubrir el patrón
# Se usa un ciclo for para recorrer los números del 2 al 12.
# En cada iteración se multiplica el número ingresado por el valor actual del ciclo y se muestra el resultado.

#4. Escribir código
def tabla_multiplicar(n):
    for i in range(1, 13):
        print(f"{n} × {i} = {n * i}")

#tabla_multiplicar(9)

#5. Prueba de escritorio

#EJERCICIO 23: Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).

#1. Entender el problema
#Entrada: Se ingresa un número entero (positivo, negativo o cero).
#Proceso: Se obtiene el valor absoluto del número y se elimina un dígito en cada iteración mediante división entera entre 10, contando cuántas veces se realiza este proceso.
#Salida: Se muestra la cantidad de dígitos del número.

#2. Bosquejo a mano
# Leer número
# Obtener su valor absoluto
# Si el número es 0
#     La cantidad de dígitos es 1
# Si no
#     Mientras el número sea diferente de 0
#         Aumentar el contador
#         Dividir el número entre 10 usando división entera
# Mostrar la cantidad de dígitos

#3. Descubrir el patrón
# En cada iteración se elimina el último dígito del número utilizando la división entera (// 10).
# El proceso se repite hasta que el número llegue a 0, mientras un contador registra cuántos dígitos tenía originalmente.

#4. Escribir código

def digitos(num):
    n = abs(num)
    contador = 0

    if n == 0:
        contador = 1
    else:
        while n != 0:
            contador += 1
            n = n // 10

    return contador

#print(digitos(108972))

#5. Prueba de escritorio

#EJERCICIO 24: Leer N números y mostrar la suma de los números pares y la suma de los números impares.

#1. Entender el problema
#Entrada: Se ingresa un número N que representa la cantidad de valores a leer. Luego se ingresan los N números.
#Proceso: Se utiliza un ciclo for para recorrer los números ingresados. Si un número es par se suma al acumulador de pares; de lo contrario, se suma al acumulador de impares.
#Salida: Se muestra la suma de los números pares y la suma de los números impares.

#2. Bosquejo a mano
# Leer N
# Inicializar suma_pares = 0
# Inicializar suma_impares = 0
# Repetir desde 1 hasta N
#     Leer número
#     Si el número es par
#         Sumarlo a suma_pares
#     Si no
#         Sumarlo a suma_impares
# Mostrar la suma de los pares
# Mostrar la suma de los impares

#3. Descubrir el patrón
# Se usan dos acumuladores para guardar las sumas.
# En cada iteración se determina si el número es par o impar mediante el operador módulo (%) y se acumula en la variable correspondiente.

#4. Escribir código

def suma_pares_impares(n):
    suma_pares = 0
    suma_impares = 0

    for i in range(1, n + 1):
        numero = int(input(f"Ingrese el valor #{i}: "))

        if numero % 2 == 0:
            suma_pares += numero
        else:
            suma_impares += numero

    return suma_pares, suma_impares

#resultado = suma_pares_impares(4)

#print(f"La suma de los pares es: {resultado[0]}")
#print(f"La suma de los impares es: {resultado[1]}")

#5. Prueba de escritorio

#EJERCICIO 25: Pedir una edad y validar que esté entre 0 y 120. Si es inválida, volver a solicitarla.

#1. Entender el problema
#Entrada: Se ingresa una edad (int).
#Proceso: Se crea una función que valida si la edad está entre 0 y 120. Si no cumple la condición, se vuelve a pedir mediante un ciclo while.
#Salida: Se muestra la edad válida ingresada por el usuario.

#2. Bosquejo a mano
# Crear una función validar_edad(edad)
#     Verificar si la edad está entre 0 y 120
#     Devolver True si es válida o False si no lo es
#
# Repetir indefinidamente
#     Leer una edad
#     Si la función devuelve True
#         Salir del ciclo
#     Si no
#         Mostrar mensaje de error
#
# Mostrar la edad válida

#3. Descubrir el patrón
# Se utiliza una función para validar una condición y devolver un valor booleano (True o False).
# El ciclo while True repite la solicitud de datos hasta que la función indique que la edad es válida mediante un break.

#4. Escribir código

def validar_edad(edad):
    return 0 <= edad <= 120

def principal():
    while True:
        edad = int(input("Edad (0-120): "))

        if validar_edad(edad):
            break

        print("Inválida, intenta de nuevo")

    print(f"Edad válida: {edad}")

# principal()

#5. Prueba de escritorio

#EJERCICIO 26: Adivinar un número aleatorio entre 1 y 100.

#1. Entender el problema
#Entrada: El usuario ingresa números enteros del 1 al 100.
#Proceso: Se genera un número aleatorio. Mediante un ciclo while se comparan los intentos del usuario con el número secreto. Si el número es menor o mayor, se muestra una pista. El ciclo termina cuando el usuario acierta.
#Salida: Se muestra un mensaje indicando que acertó y la cantidad de intentos realizados.

#2. Bosquejo a mano
# Generar un número aleatorio
# Inicializar el contador de intentos en 0
# Repetir hasta adivinar el número
#     Leer un intento
#     Aumentar el contador
#     Si el intento es igual al número secreto
#         Mostrar mensaje y terminar
#     Si el intento es menor
#         Mostrar "Es mayor"
#     Si no
#         Mostrar "Es menor"

#3. Descubrir el patrón
# Se utiliza un ciclo while True porque no se sabe cuántos intentos necesitará el usuario.
# En cada repetición se compara el número ingresado con el número secreto.
# Cuando el usuario acierta, se utiliza break para salir del ciclo.

#4. Escribir código

import random

def adivinar_numero(secreto):

    intentos = 0

    while True:
        intento = int(input("Adivina el numero del 1 al 100: "))
        intentos += 1

        if intento == secreto:
            print(f"Felicidades lo adivinaste en {intentos} intentos")
            break

        elif intento < secreto:
            print("Es mayor")

        else:
            print("Es menor")

numero = random.randint(1,100)

#adivinar_numero(numero)

#5. Prueba de escritorio

#EJERCICIO 27: Mostrar los primeros N números de la serie de Fibonacci.

#1. Entender el problema
#Entrada: Se ingresa un número N, que representa la cantidad de términos de la serie.
#Proceso: Se inicializan los dos primeros términos (0 y 1). Mediante un ciclo for se muestran los términos y en cada iteración se actualizan para obtener el siguiente número de la serie.
#Salida: Se muestran los primeros N números de la serie de Fibonacci.

#2. Bosquejo a mano
# Leer N
# Inicializar los dos primeros números de la serie (0 y 1)
# Repetir N veces
#     Mostrar el primer número
#     Actualizar ambos números para obtener el siguiente término
# Al finalizar, hacer un salto de línea

#3. Descubrir el patrón
# Se utilizan dos variables para almacenar los dos últimos términos de la serie.
# En cada repetición se imprime el primer término y luego ambos valores se actualizan simultáneamente para avanzar al siguiente par de números.

#4. Escribir código

def fibonacci(n):

    a, b = 0, 1

    for _ in range(n):

        print(a, end=" ")

        a, b = b, a + b

    print()

fibonacci(10)

#5. Prueba de escritorio

#EJERCICIO: Escribir una función calcular_iva(precio) que reciba un precio y retorne el IVA (15%). Luego crear una función calcular_total(precio) que retorne el precio más el IVA utilizando la función anterior.

#1. Entender el problema
#Entrada: Se ingresa un precio.
#Proceso: Se crea una función que calcula el IVA (15%) y otra función que utiliza la primera para calcular el precio total.
#Salida: Se muestra el valor del IVA y el total a pagar.

#2. Bosquejo a mano
# Leer el precio
# Crear una función para calcular el IVA
#     Multiplicar el precio por 15%
#     Retornar el IVA
# Crear una función para calcular el total
#     Llamar a la función que calcula el IVA
#     Sumar el precio y el IVA
#     Retornar el total
# Mostrar el IVA
# Mostrar el total

#3. Descubrir el patrón
# Se divide el problema en dos funciones con responsabilidades diferentes.
# Una función puede llamar a otra para reutilizar código y evitar repetir operaciones.

#4. Escribir código

def calcular_iva(precio):

    iva = precio * 0.15

    return iva


def calcular_total(precio):

    total = precio + calcular_iva(precio)

    return total


#precio = float(input("Ingrese el precio: "))

#print(f"IVA: ${calcular_iva(precio):.2f}")
#print(f"Total: ${calcular_total(precio):.2f}")

#5. Prueba de escritorio

#EJERCICIO 29: Escribir una función que reciba un número y retorne True si es primo, False si no.
#Luego escribir una función contar_primos(a, b) que cuente cuántos números primos hay entre a y b.

#1. Entender el problema
#Entrada: Se ingresan dos números (a y b) que representan el inicio y el fin de un intervalo.
#Proceso: Se crea una función para determinar si un número es primo. Luego se crea otra función que recorra todos los números entre a y b, utilizando la función anterior para contar cuántos son primos.
#Salida: Se muestra la cantidad de números primos encontrados entre a y b.

#2. Bosquejo a mano
# Leer el número inicial y el número final
# Crear una función para verificar si un número es primo
#     Si el número es menor o igual a 1, retornar False
#     Buscar divisores entre 2 y el número menos uno
#     Si encuentra un divisor, retornar False
#     Si no encuentra divisores, retornar True
# Crear una función para contar los primos
#     Inicializar un contador en 0
#     Recorrer todos los números entre a y b
#     Si el número es primo
#         Aumentar el contador
#     Retornar el contador
# Mostrar la cantidad de números primos

#3. Descubrir el patrón
# Se reutiliza una función dentro de otra.
# La función es_primo() resuelve un problema específico y contar_primos() la utiliza para recorrer un intervalo y contar los valores que cumplen la condición.

#4. Escribir código
#En la linea 768 ya tengo una funcion que busca numeros primos, simplemento voy a hacer la que los cuenta
def contar_primos(a, b):

    contador = 0

    for i in range(a, b + 1):

        if es_primo(i):
            contador += 1

    return contador


print(contar_primos(1, 20))

#5. Prueba de escritorio
    
#EJERCICIO 30: Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.
#1. Entender el problema
#Entrada: Se ingresa un número entero.
#Proceso: Se reutiliza la función digitos() para obtener la cantidad de dígitos del número. Luego, mediante un ciclo while, se recorre el número dígito por dígito, elevando cada uno a la cantidad de dígitos y acumulando la suma. Finalmente se compara la suma obtenida con el número original.
#Salida: Se muestra True si el número es narcisista y False si no lo es.

#2. Bosquejo a mano
#Es necesario reutilizar la función digitos() para conocer la cantidad de dígitos del número.
#Luego se utiliza un ciclo while para recorrer cada dígito del número.
#En cada iteración se obtiene el último dígito, se eleva al número de dígitos y se acumula en una variable suma.
#Al finalizar el recorrido se compara la suma con el número original.

#3. Prueba de escritorio
#Ejemplo: n = 153
#
#Cantidad de dígitos = 3
#
#Iteración 1:
#digito = 3
#suma = 3³ = 27
#numero = 15
#
#Iteración 2:
#digito = 5
#suma = 27 + 5³ = 152
#numero = 1
#
#Iteración 3:
#digito = 1
#suma = 152 + 1³ = 153
#numero = 0
#
#Comparación final:
#153 == 153 → True

#4. Escribir código
#Se llama la funcion de mas arriba llamada digitos(), linea 833

def es_narcisista(n):

    cantidad = digitos(n)
    numero = abs(n)
    suma = 0

    while numero != 0:

        digito = numero % 10
        suma += digito ** cantidad
        numero = numero // 10

    return suma == abs(n)


print(es_narcisista(153))

#5. Prueba de escritorio

#EJERCICIO 31: Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
#Añade una función calcular() que pida dos números y muestre suma, resta, multiplicación y división. Nueva opción del menú.

#1. Entender el problema
#Entrada: El usuario selecciona una opción del menú. Si elige la opción "Calcular", ingresa dos números.
#Proceso: Se crean funciones independientes para cada opción del menú (saludar, despedir, calcular y mostrar_menu). El programa permanece en un ciclo while hasta que el usuario seleccione la opción de salir. La función calcular() realiza las cuatro operaciones básicas y verifica que el segundo número sea diferente de cero antes de dividir.
#Salida: Se muestra el saludo, la despedida, los resultados de las operaciones matemáticas o un mensaje de despedida al salir.

#2. Bosquejo a mano
# Crear una función saludar()
# Crear una función despedir()
# Crear una función calcular()
#     Pedir dos números
#     Mostrar suma
#     Mostrar resta
#     Mostrar multiplicación
#     Si el segundo número es diferente de cero
#         Mostrar división
#     Caso contrario
#         Mostrar mensaje de error
# Crear una función mostrar_menu()
# Crear un ciclo while para mostrar el menú continuamente
# Leer la opción elegida
# Según la opción, llamar a la función correspondiente
# Si el usuario elige salir
#     Romper el ciclo con break

#3. Descubrir el patrón
# Se divide el programa en varias funciones, donde cada una realiza una tarea específica.
# El programa principal solo controla el menú y llama a la función correspondiente según la opción elegida por el usuario.
# Se utiliza un ciclo while True junto con break para mantener el menú activo hasta que el usuario decida salir.

#4. Escribir código

def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

def calcular():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")

    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("No se puede dividir para cero.")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Calcular")
    print("4. Salir")

while True:
    mostrar_menu()

    opcion = input("Opción: ")

    if opcion == "1":
        saludar()

    elif opcion == "2":
        despedir()

    elif opcion == "3":
        calcular()

    elif opcion == "4":
        print("Adiós")
        break

    else:
        print("Opción inválida")

#5. Prueba de escritorio

#EJERCICIO 32: Función area_rectangulo(base, altura) que retorne el área.

#1. Entender el problema
#Entrada: Se ingresan la base y la altura de un rectángulo.
#Proceso: Se crea una función area_rectangulo(base, altura) que recibe ambos valores, calcula el área multiplicando la base por la altura y retorna el resultado.
#Salida: Se muestra el área del rectángulo.

#2. Bosquejo a mano
# Crear la función area_rectangulo(base, altura)
# Multiplicar la base por la altura
# Retornar el área
# Pedir la base y la altura al usuario
# Llamar a la función
# Mostrar el resultado

#3. Descubrir el patrón
# Se utiliza una función que recibe parámetros, realiza un cálculo y retorna el resultado.
# El programa principal únicamente obtiene los datos, llama a la función y muestra el valor retornado.

#4. Escribir código

def area_rectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

resultado = area_rectangulo(base, altura)

print(f"El área del rectángulo es: {resultado}")

def area_rectangulo_validacion(base, altura):

    if base <= 0 or altura <= 0:
        return None

    return base * altura


base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

resultado = area_rectangulo_validacion(base, altura)

if resultado is None:
    print("La base y la altura deben ser mayores que cero.")
else:
    print(f"El área del rectángulo es: {resultado}")

print(f"El área del rectángulo es: {resultado}")

#5. Prueba de escritorio

#EJERCICIO 33: Función maximo(a, b, c) que retorne el mayor de tres números.

#1. Entender el problema
#Entrada: Se ingresan tres números.
#Proceso: Se crea una función maximo(a, b, c) que compara los tres números para determinar cuál es el mayor y lo retorna.
#Salida: Se muestra el número mayor.

#2. Bosquejo a mano
# Crear la función maximo(a, b, c)
# Comparar el primer número con el segundo y el tercero
# Si el primero es el mayor, retornarlo
# En caso contrario, comparar el segundo con el tercero
# Si el segundo es el mayor, retornarlo
# De lo contrario, retornar el tercero
# Pedir los tres números al usuario
# Llamar a la función
# Mostrar el resultado

#3. Descubrir el patrón
# Se utiliza una función con parámetros que compara varios valores y retorna uno de ellos.
# El programa principal únicamente obtiene los datos, llama a la función y muestra el valor retornado.

#4. Escribir código

def maximo(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = maximo(num1, num2, num3)

print(f"El número mayor es: {resultado}")

def maximo_iguales(a, b, c):

    if a == b == c:
        return "Los tres números son iguales"

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    return c

#5. Prueba de escritorio

#EJERCICIO 34: Escribir una función es_bisiesto(anio) que retorne True si un año es bisiesto y False en caso contrario.

#1. Entender el problema
#Entrada: Se ingresa un año.
#Proceso: Se crea una función es_bisiesto(anio) que verifica si el año cumple las reglas de un año bisiesto: debe ser divisible entre 4 y no entre 100, o ser divisible entre 400.
#Salida: Se muestra True si el año es bisiesto y False si no lo es.

#2. Bosquejo a mano
# Crear la función es_bisiesto(anio)
# Verificar si el año es divisible entre 4 y no entre 100
# O verificar si el año es divisible entre 400
# Si cumple alguna de las condiciones
#     Retornar True
# En caso contrario
#     Retornar False
# Pedir el año al usuario
# Llamar a la función
# Mostrar el resultado

#3. Descubrir el patrón
# Se utiliza una función que evalúa una condición lógica compuesta usando operadores and y or.
# La función retorna un valor booleano (True o False) según el resultado de la condición.

#4. Escribir código

def es_bisiesto(anio):

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True

    return False


anio = int(input("Ingrese un año: "))

print(es_bisiesto(anio))

def bisiesto(anio):

    if anio <= 0:
        return None

    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


anio = int(input("Ingrese un año: "))

resultado = bisiesto(anio)

if resultado is None:
    print("Ingrese un año válido.")
else:
    print(resultado)
#5. Prueba de escritorio

#EJERCICIO 35: Escribir una función factorial(n) y luego una función
#combinatoria(n, k) = n! / (k! · (n-k)!).

#1. Entender el problema
#Entrada: Se ingresan dos números enteros n y k.
#Proceso: Se crea una función factorial(n) para calcular el factorial de un número.
#Luego se crea una función combinatoria(n, k) que reutiliza la función factorial()
#para calcular la cantidad de combinaciones posibles.
#Salida: Se muestra el resultado de la combinatoria.

#2. Bosquejo a mano
# Crear la función factorial(n)
# Inicializar una variable resultado en 1
# Recorrer los números desde 1 hasta n
# Multiplicar el resultado por cada número
# Retornar el factorial
#
# Crear la función combinatoria(n, k)
# Utilizar la función factorial() para calcular:
#     n!
#     k!
#     (n-k)!
# Aplicar la fórmula de la combinatoria
# Retornar el resultado
#
# Pedir n y k
# Llamar a la función combinatoria()
# Mostrar el resultado

#3. Descubrir el patrón
# Se reutiliza una función dentro de otra.
# La función factorial() resuelve un problema específico y combinatoria()
# la utiliza tres veces para aplicar la fórmula matemática.
# También se reutiliza el concepto de acumulador visto anteriormente.

#4. Escribir código

def factorial(n):

    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


def combinatoria(n, k):

    # CAMBIO: Se valida que k no sea mayor que n ni negativo.
    # Si ocurre, la combinatoria no existe y se retorna None.

    if k < 0 or k > n:
        return None

    return factorial(n) / (factorial(k) * factorial(n - k))


n = int(input("Ingrese n: "))
k = int(input("Ingrese k: "))

resultado = combinatoria(n, k)

if resultado is None:
    print("Valores inválidos. Debe cumplirse 0 ≤ k ≤ n.")
else:
    print(f"La combinatoria es: {resultado}")

#5. Prueba de escritorio

#EJERCICIO 36: Programa que use funciones separadas para cada operación
#(sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.

#1. Entender el problema
#Entrada: El usuario selecciona una opción del menú e ingresa dos números.
#Proceso: Se crean funciones independientes para sumar, restar, multiplicar y dividir.
#Según la opción elegida, el programa llama a la función correspondiente.
#Salida: Se muestra el resultado de la operación seleccionada.

#2. Bosquejo a mano
# Crear la función sumar(a, b)
# Crear la función restar(a, b)
# Crear la función multiplicar(a, b)
# Crear la función dividir(a, b)
# Crear una función mostrar_menu()
# Mostrar el menú
# Leer la opción elegida
# Pedir los dos números
# Llamar a la función correspondiente
# Mostrar el resultado
# Repetir hasta que el usuario decida salir

#3. Descubrir el patrón
# Se divide el problema en varias funciones, donde cada una realiza una operación específica.
# El programa principal únicamente controla el menú y llama a la función adecuada.
# Se reutiliza el uso de parámetros, valores de retorno y un ciclo while con break.

#4. Escribir código

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):

    # CAMBIO: Se valida que el divisor no sea cero antes de realizar la división.

    if b == 0:
        return None

    return a / b


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Programa finalizado.")
        break

    if opcion in ("1", "2", "3", "4"):

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print(f"Resultado: {sumar(num1, num2)}")

        elif opcion == "2":
            print(f"Resultado: {restar(num1, num2)}")

        elif opcion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")

        elif opcion == "4":

            resultado = dividir(num1, num2)

            if resultado is None:
                print("No es posible dividir para cero.")
            else:
                print(f"Resultado: {resultado}")

    else:
        print("Opción inválida.")

#5. Prueba de escritorio

