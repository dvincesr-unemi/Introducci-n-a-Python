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

        # Validación: evita dividir para cero si no hay notas.
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


obj = Calificador()

print(obj.cargar_notas(80, 95, 70, 120, -5, 100))

print(f"Promedio: {obj.promedio()}")