##No se encontraron casos en los que el programa termine en error
entrada=input("Escriba la palabra a verificar: ").lower()
i: int=0
pal: bool=True
largo: int=len(entrada)-1
while (i<len(entrada)):
    if entrada[i]==entrada[largo-i]:
        i+=1
        continue
    else:
        pal=False
        break

print(entrada+" es palíndromo? "+str(pal))