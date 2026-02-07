#importando biblioteca nativa do python math — Funções matemáticas
import math

#Entrada de um número escolhido pelo usuário
print("Vamos mostrar a raíz quadrada do seu número, mas primeiro preciso que você digite ele.")
number_usu = float(input("Qual número que você quer escolher: "))

#funções matematicas para dar uma saída no meu programa
square_number_int = math.isqrt(number_usu)
exponent_number = math.pow(number_usu,2)
square_number_float = round(math.sqrt(number_usu),2)

#saída com a resposta para meu usuário
print(f"A raíz quadrada do seu número de forma inteira e sem casas decimais: {square_number_int} \nSeu número com raíz quadrada de forma inteira e duas casas decimais (se houver):{square_number_float} \nSeu número ao quadrado: {exponent_number}")
