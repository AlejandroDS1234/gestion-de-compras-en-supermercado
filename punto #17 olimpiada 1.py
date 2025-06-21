print("Convertidor de nota numerica a letra")
nota=int(input("Ingrese una nota de 0 a 5 para convertirlo a una calificacion de F a A"))
if nota<=3 and nota>0:
    print("Su nota equivale a una F")
elif nota<3.5:
    print("Su nota equivale a una D")
elif nota<4:
    print("Su nota equivale a una C")
elif nota<4.5:
    print("Su nota equivale a una B")
elif nota<=5:
    print("Su nota equivale a una A")
else:
    print("Nota no valida")