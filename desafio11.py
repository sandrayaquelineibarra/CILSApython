
lista_dnis = [12345678, 87654321, 11111111, 22222222]

while True:
    try:
        
        entrada = input("Ingrese un número de DNI o escriba 'salir' para terminar: ")

        if entrada.lower() == "salir":
            print("Gracias por utilizar nuestro sistema.")
            break

        
        dni = int(entrada)

        
        if dni in lista_dnis:
            print(f"El DNI {dni} se encuentra registrado en nuestro sistema.")
        else:
            print(f"El DNI {dni} no está registrado en nuestro sistema.")

    except ValueError:
       
        print(f"Lo lamento, '{entrada}' no es un número.")

else:
    print("¡El programa se ejecutó perfectamente!")
