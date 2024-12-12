def esta_dentro_intervalo(valor, limite_inferior, limite_superior):


  return limite_inferior <= valor <= limite_superior

if __name__ == "__main__":
  limite_inferior = int(input("Ingrese el límite inferior del intervalo: "))
  limite_superior = int(input("Ingrese el límite superior del intervalo: "))
  valor_a_verificar = int(input("Ingrese el valor a verificar: "))

  if esta_dentro_intervalo(valor_a_verificar, limite_inferior, limite_superior):
    print(f"El valor {valor_a_verificar} está dentro del intervalo [{limite_inferior}, {limite_superior}]")
  else:
    print(f"El valor {valor_a_verificar} no está dentro del intervalo [{limite_inferior}, {limite_superior}]")