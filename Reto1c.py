try:
    entrada=[int(i) for i in input("Escriba la lista de números, separados por coma: ").split(",")]
except ValueError as error:
    print(f"Error: {error}, los valores deben estar separados por comas")
primos = []

def primo(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

try:
    for i in entrada:
        if primo(i):
            primos.append(i)
    print("los números primos son: ")
    print(primos)
except NameError as error:
    print(f"Error:{error}, no hay valores a evaluar")

