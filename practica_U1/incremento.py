def incremento():
    cont=0
    n=int(input("Ingrese un numero: "))
    cont+=4
    m=0
    cont+=1
    for i in range(n):
        for j in range(n):
            m=m+1
            cont+=2
    print("Resultado",m)
    cont+=3
    cont+=(2*n*n+2*n)+(2*n+2) #aqui aplico las unidades de tiempo del for
    print(f"El numero de unidades de tiempo es: {cont} ut")

if __name__ == "__main__":
        incremento()