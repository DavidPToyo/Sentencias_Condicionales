import sys
import math

peso = float(input("Ingrese el peso en Kg: "))
altura_cm = float(input("Ingrese la altura en cm: "))
altura_m = altura_cm / 100
imc = peso / (altura_m**2)

print(f"El imc es de: {imc:.1f}")

if imc < 18.5:
    print("Bajo Peso")
elif 18.5 <= imc < 25:
    print("Adecuado")
elif 25<= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidad Grado 1")
elif 35 <= imc < 40:
    print("Obesidad Grado 2")
else:
    print("Obesidad Grado 3")