from DoblePila import DoblePila

if __name__ == "__main__":
    unaDoblePila = DoblePila(10, int)
    opcion = -1
    while opcion != "0":
        print("Ingrese la opcion deseada")
        print("[0] Salir")
        print("[1] Insertar elemento en pila1")
        print("[2] Insertar elemento en pila2")
        print("[3] Desapilar elemento en pila1")
        print("[4] Desapilar elemento en pila2")
        opcion = input("--> ")
        if opcion == "1":
            elemento = int(input("Ingrese el elemento a insertar en la pila1: "))
            unaDoblePila.apilarPila1(elemento)
        
        elif opcion == "2":
            elemento = int(input("Ingrese el elemento a insertar en la pila2: "))
            unaDoblePila.apilarPila2(elemento)
        
        elif opcion == "3":
            elemento = unaDoblePila.desapilarPila1()
            print(elemento)
        
        elif opcion == "4":
            elemento = unaDoblePila.desapilarPila2()
            print(elemento)
    
    print("Salio del programa")