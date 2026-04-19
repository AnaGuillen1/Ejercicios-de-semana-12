monto = float(input("Monto de compra: "))

if monto > 100:
    total = monto * 0.8
elif 50 <= monto <= 100:
    total = monto * 0.9
else:
    total = monto

print("Total a pagar:", total)
