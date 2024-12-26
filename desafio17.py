def crear_diccionario_persona():
    persona = {}
    persona['nombre'] = input("Ingrese el nombre: ")
    persona['apellido'] = input("Ingrese el apellido: ")
    persona['edad'] = int(input("Ingrese la edad: "))
    persona['email'] = input("Ingrese el email: ")
    return persona

def escribir_dato_txt(lista_diccionarios, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("nombre,apellido,edad,email\n") 
        for persona in lista_diccionarios:
            linea = f"{persona['nombre']},{persona['apellido']},{persona['edad']},{persona['email']}\n"
            archivo.write(linea)

personas = []

num_personas = int(input("¿Cuántas personas desea ingresar? "))

for _ in range(num_personas):
    persona = crear_diccionario_persona()
    personas.append(persona)

escribir_dato_txt(personas, 'dato_persona.txt')

print("Los datos se han guardado en el archivo dato_persona.txt")