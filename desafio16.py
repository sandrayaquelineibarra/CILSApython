def calcular_area_triangulo(base, altura):
  
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos.")

    return (base * altura) / 2


try:
    
    print("Área con base=10 y altura=5:", calcular_area_triangulo(10, 5))  
    print("Área con base=7 y altura=3:", calcular_area_triangulo(7, 3))    
    print("Área con base=12 y altura=8:", calcular_area_triangulo(12, 8))  

   
    print("Área con base=-5 y altura=4:", calcular_area_triangulo(-5, 4))  
except ValueError as e:
    print("Error:", e)
