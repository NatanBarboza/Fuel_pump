from fuel_pump import FuelPump

fp1 = FuelPump("Gasolina", 5.65)

print(fp1.type_fuel)
print(fp1.value)
print(fp1.fuel_quantity)

print(fp1.to_fuel(50))
print(fp1.fuel_quantity)
print(fp1.fuel_per_l(5))
print(fp1.fuel_quantity)