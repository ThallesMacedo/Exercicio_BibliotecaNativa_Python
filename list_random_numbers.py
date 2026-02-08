#Importando biblioteca nativa para geraçõa de números aleatórios
import random

#Mensagem de explicação e lista vazia criada
print("Gerando uma lista com 5 números aleatórios de 0 a 1000")
list_number = []

#Criado loop para geração de números até a quantidade de 5 dentro da lista
while len(list_number) <=5:
    number = random.randrange(1001)
    list_number.append(number)

#Extraindo o máximo e o mínimo dentro da lista
bigger = max(list_number)
smaller = min(list_number)

#Apresentando o resultado na tela
print(f"A lista gerada foi: {list_number}\nSeu maior número foi: {bigger}\nSeu menor número foi: {smaller}")
