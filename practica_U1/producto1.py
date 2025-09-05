def producto():
    cont=0
    m=0
    cont+=1
    n=int(input("Ingrese un numero: "))
    cont+=4
    m=n*n
    cont+=2
    print("El producto es: ",m)
    cont+=3
    print(f"El numero de unidades de tiempo es: {cont} ut")

if __name__ == "__main__":
    producto()