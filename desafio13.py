
personas = {}


for i in range(3):
    print(f"Ingrese los datos para la persona #{i + 1}:")
    
   
    nombre = input("Nombre: ")
    
   
    apellido = input("Apellido: ")
    
  
    while True:
        try:
            dni = int(input("DNI: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número válido para el DNI.")

  
    persona = {"nombre": nombre, "apellido": apellido, "dni": dni}

 
    personas[i + 1] = persona


print("\nDatos de las personas ingresadas:")
for key, persona in personas.items():
    print(f"Persona #{key}:")
    print(f"  Nombre: {persona['nombre']}")
    print(f"  Apellido: {persona['apellido']}")
    print(f"  DNI: {persona['dni']}")

