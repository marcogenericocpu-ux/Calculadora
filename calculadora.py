print("=== CALCULADORA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Seleccione una opción: "))

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if opcion == 1:
    print("Resultado:", a + b)
elif opcion == 2:
    print("Resultado:", a - b)
elif opcion == 3:
    print("Resultado:", a * b)
elif opcion == 4:
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Opción no válida")