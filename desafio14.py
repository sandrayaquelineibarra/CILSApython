personas = {}

for i in range(3):
    print(f"Ingrese los datos de la persona {i + 1}:")
    
    nombre = input("Nombre: ")
    
    apellido = input("Apellido: ")
    
    dni = input("DNI: ")
    
    persona = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }
    personas[i + 1] = persona

print("\nDatos de las personas ingresadas:")
for clave, persona in personas.items():
    print(f"\nPersona #{clave}:")
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"DNI: {persona['dni']}")