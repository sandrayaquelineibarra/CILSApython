
notas = [3, 5, 6, 8, 10, 4, 9, 7]
  
notas_validas = []

for nota in notas:
    if 6 <= nota <= 10:
        notas_validas.append(nota)

print("Notas válidas entre 6 y 10:")
for nota in notas_validas:
    print(nota)