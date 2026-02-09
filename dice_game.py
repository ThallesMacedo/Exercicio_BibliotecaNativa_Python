#Importando bilbioteca para gerar número aleatório
import random

#Mensagem de inicio do programa e função para gerar número
print("Bem vindo ao dado númerico\nVou sortear um número de 1 a 6\nE te dizer se sou par ou ímpar")
number = random.randrange(1,7)

#Condicional para verificar se é par ou ímpar, mostra na tela o resultado ao usuário
if number % 2 ==0:
    print(f"O número sorteado foi : {number} e ele é par")
else:
    print(f"O número sorteado foi : {number} e ele é ímpar")
