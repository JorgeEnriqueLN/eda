def suma():
    cont=0
    cont2=0
    n=int(input("Ingrese un numero: "))
    cont+=4
    m=0
    cont+=1
    for i in range(n):
        m=m+n
        cont+=2 
    print("Resultado",m)
    cont+=3
    cont+=(2*n+2) #aqui aplico las unidades de tiempo del for. No lo hago dentro del for porque se contaria n veces.
    print(f"El numero de unidades de tiempo es: {cont} ut")

if __name__ == "__main__":
    suma()