#Importando biblioteca de datas
import datetime 

#Puxando as funções de data e hora atual
today_and_hour = datetime.datetime.now()
year = today_and_hour.strftime("%Y")

#Mostrando na tela de forma organizada
print(f"A data e horário atual é: {today_and_hour}\nE o ano é: {year}")
