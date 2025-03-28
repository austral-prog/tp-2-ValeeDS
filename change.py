def change():
    expense = 23.75
    money = 100

    gasto = money - expense

    pesos = int(gasto)
    centavos = int((gasto - pesos)*100)

    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{centavos}")