#Funciones para el buen funcionamiento del programa
def imc(n, x):
    if n <= 0 or x <= 0:
        print("No pueden ser valores menores a 0.")
        return print("Vuelve a intentarlo.")
    else:
        return n / x ** 2

def altura_cm(n):
    if n <= 0:
        print("No se puede calcular una altura menor a 0 cm.")
        return print("Vuelve a intentarlo.")
    else:
        cm = n * 100
        return cm

def peso_grs(n):
    if n <= 0:
        print("No se puede calcular peso negativo.")
        return print("Vuelve a intentarlo.")
    else:
        grs = n * 1000
        return grs
if __name__ == "__main__": # Permite que otro archivo pueda invocar las funciones que se han creado en este y 
    # permite el funcionamiento de los mismos en la botonera grafica
    #Bucle del programa
    while True:
        print("***** Bienvenido a la calculadora de IMC *****")
        print("1- Calcular tu IMC.")
        print("2- Calcular altura en cm.")
        print("3- Calcular peso en gramos.")
        print("4- Salir.") 

        # Variable del bucle
        opt = input("Selecciona una opción: ")

        if opt == "1":
            try: # Comprueba que las variables de la función esten acorde a lo definido en el segmento declarado como imc
                peso = float(input("Ingresa tu peso en KG: "))
                altura = float(input("Ingresa tu altura en mts: "))

                total = imc(peso, altura) # Aquí el programa ejecuta la función definida

                if total is not None and total > 0: # is not None and permite que el programa pueda ejecutarse con números negativos.
                    print(f"Tu IMC es: {total}.\n") # Funcionamiento de la calculadora de IMC
            except ValueError:
                print("Error: Solo puedes ingresar números.\n")


        elif opt == "2":
            try:
                altura = float(input("Ingresa tu altura en mts: "))

                alturacm = altura_cm(altura)

                if alturacm is not None and alturacm > 0: # is not None and permite que el programa pueda ejecutarse con números negativos.
                    print(f"Tu altura en CM es: {alturacm} cm.\n")
            except ValueError:
                print("Error: Solo puedes ingresar números.\n")


        elif opt == "3":
            try:
                peso = float(input("Ingresa tu peso en KG: "))

                pgrs = peso_grs(peso)

                if pgrs is not None and pgrs > 0: # is not None and permite que el programa pueda ejecutarse con números negativos.
                    print(f"Tu peso en gramos es: {pgrs} grs.\n")
            except ValueError:
                print("Error: Solo puedes ingresar números.\n")


        elif opt == "4":
            print("Hasta pronto, gracias por usar nuestros servicios")
            break # Rompe el bucle de la calculadora y el programa en general

        else:
            print("ERROR: ELIGE OTRA OPCIÓN!!")