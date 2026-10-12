
# Funciones de la calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


# Pedimos los números y la operación
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
    print("Error: Debes ingresar números válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
