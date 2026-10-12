
# Funciones de la calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


# Programa principal
def calculadora():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        operacion = input("Ingresa la operación (+, -, *, /): ")

        if operacion == "+":
            resultado = sumar(num1, num2)
        elif operacion == "-":
            resultado = restar(num1, num2)
        elif operacion == "*":
            resultado = multiplicar(num1, num2)
        elif operacion == "/":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operación inválida"

        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Error: Datos inválidos o división por cero.")


# Ejecutamos la calculadora
if __name__ == "__main__":
    calculadora()
