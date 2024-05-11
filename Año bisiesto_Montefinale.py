año = int(input("Ingresa un año y te diré si es bisiesto o no: "))
if año < 1:
    print("Por favor ingresa un año válido.")
elif (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")