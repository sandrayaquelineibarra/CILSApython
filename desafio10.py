try:
  
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

  
    resultado = num1 / num2

except ValueError:
  
    print("Error: Los datos ingresados no son números válidos.")

except ZeroDivisionError:
   
    print("Error: No se puede dividir entre cero.")

else:

    print(f"El resultado de la división es: {resultado}")