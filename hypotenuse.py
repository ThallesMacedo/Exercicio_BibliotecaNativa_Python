#Importando a Biblioteca de funções matematicas
import math

#Recebendo os numeros referente aos catetos
print("Bem vindo ao algoritimo de cálculo de hipotenusa \nVamos começar?")

number_a = float(input("Qual é o primeiro número do cateto (cm): "))
number_b = float(input("Qual é o segundo número do cateto: (cm)"))

#Fazendo o calculo por parte, primeiro realizo a soma dos catetos ao quadrado e o resultado eu retiro a raíz quadrada
exponent_number = math.pow(number_a,2) + math.pow(number_b,2)
hypotenuse = math.sqrt(exponent_number)

#Devolvo para o usuário o resultado da hipotenusa
print(f"A hipotenusa calculada com os catetos inseridos é de: {hypotenuse:.2f} cm")