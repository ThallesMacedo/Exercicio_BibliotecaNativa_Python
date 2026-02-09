#Importando biblioteca para uso de datas
import datetime

#Recebo o dado do usuário em qual ano ele nasceu e puxo uma função para saber a data atual transformando o ano atual em inteiro
year_usu = int(input("Qual ano que você nasceu? "))
today_and_hour = datetime.datetime.now()
year_today = int(today_and_hour.strftime("%Y"))

#Faço a fórmula do ano atual menos o ano inserido pelo usuário
years = year_today - year_usu

#Apresentando o resultado
print(f"Sua idade aproximada é de: {years} anos")
