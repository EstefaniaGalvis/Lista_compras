lista_compras = []

while True: 
    productos = input("Ingrese el nombre del producto (o 'terminar' para finalizar): ")

    if productos == "terminar":
        break
    else:
        lista_compras.append(productos)

print("Lista de compras: ")
for productos in lista_compras:
    print(productos)

        

