try:
    entrada=[int(i) for i in input("Escriba la lista de números, separados por coma: ").split(",")]

    print(entrada)

    mayor=0
    for i in range(0,len(entrada)-1):
        sumar=entrada[i]+entrada[i+1]
        if (sumar>mayor):
            mayor=sumar
        
    print ("La suma mayor es: ")
    print (mayor)

except ValueError as error:
    print(f"Error: {error}, los valores deben estar separados por comas")