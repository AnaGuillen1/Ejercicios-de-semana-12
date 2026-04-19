a = float(input("Primer número: "))
b = float(input("Segundo número: "))
op = input("Operación (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: división entre cero")
else:
    print("Operación inválida")
