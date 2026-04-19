anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Bisiesto")
else:
    print("No bisiesto")
