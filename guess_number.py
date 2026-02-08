#Importando a biblioteca para poder sortear um número aleatorio
import random

#Dando boas vindas e explicando como funciona o algoritmo e sorteando o número de 0 até 10
print("Bem vindo ao joguinho da adivinhação de número \nEu irei sortear um número de forma aleatória para que você tente, podemos começar?")
guess_number = random.randrange(11)
usu_number = int(input("Qual número que você acha que eu sortiei: "))

#Loop caso usuário digite número maior que 10
while usu_number >10:
    print("O jogo apenas sorteia um número de 0 a 10")
    usu_number = int(input("Tente novamente: "))

#Loop caso usuário digite número diferente do correto
while usu_number != guess_number:
    print("Errou")
    usu_number = int(input("Tente novamente: "))

#Condicional do usuário acertando o número sortiado
if usu_number == guess_number:
    print("Parabéns, voce acertou!")