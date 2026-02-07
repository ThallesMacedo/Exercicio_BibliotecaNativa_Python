import math

print("Vamos mostrar a raíz quadrada do seu número, mas primeiro preciso que você digite ele.")
number_usu = int(input("Qual número que você quer escolher: "))

square_number = math.isqrt(number_usu)
exponent_number = math.pow(number_usu,2)

print(square_number)
print(exponent_number)