def change():
    expense = 23.75
    money = 100

    pesos = money - expense
    centavos = int((pesos - int(pesos))*100)

    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{centavos}")

change()