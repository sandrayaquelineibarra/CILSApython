vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

palabras = ["Hola", "Mundo", "Python", "áéíóúAEIOU", 123, None, ""]

print("Resultados de las pruebas:")
for palabra in palabras:
    if isinstance(palabra, str):  
        contador = 0
        for letra in palabra:  
            if letra in vocales:
                contador += 1
        print(f"La palabra '{palabra}' contiene {contador} vocales.")
    else:
        print(f"'{palabra}' no es una palabra válida.")