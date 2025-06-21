print("Comparador de cifras de un numero de dos cifras")
cfr=str(input("Ingrese un numero de dos cifras: "))
cfr1=int(cfr[0])
cfr2=int(cfr[-1])
if cfr1>cfr2:
    print(f"{cfr1} es mayor")
elif cfr1<cfr2:
    print(f"{cfr2} es mayor")
else:
    print("Doble")