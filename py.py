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

descuento()
#5. Prueba de escritorio 





