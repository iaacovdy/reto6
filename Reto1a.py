entrada=input("Escriba dos números y el operador, separados por coma: ").split(",")
def operar(a,b,c):
    match c:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            try:
                return a/b
            except ZeroDivisionError as error:
                print(f"Error: {error}, el divisor no puede ser cero")
print(entrada)
print(operar(int(entrada[0]),int(entrada[1]),entrada[2]))