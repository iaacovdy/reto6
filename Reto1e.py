try:
    entrada=input("Escriba la lista de palabras, separadas por coma: ").split(",")
    ordenada=[]

    for i in range(0,len(entrada)):
        ordenada.append(sorted(entrada[i]))
    for i in ordenada:
        if ordenada.count(i)==1:
            entrada.pop(ordenada.index(i))

    print("Repetidos:")
    print(entrada)

except ValueError as error:
    print(f"Error: {error}, las palabras deben estar separadas por comas")