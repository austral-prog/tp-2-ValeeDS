def change():
    expense = 23.75
    money = 100

    gasto = money - expense

    pesos = int(gasto)
    centavos = int( (gasto - pesos) *100)

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
