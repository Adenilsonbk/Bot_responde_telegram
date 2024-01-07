import telebot
import wikipedia
from colorama import Fore, Back, Style

bot = telebot.TeleBot('6005195174:AAFMDKEgiEqL-Jpb7QaPYQkhAvRfHbxzA0c')

texto_usuario = " "

wikipedia.set_lang("pt")



@bot.message_handler(commands=["start"])
def start(message):
    
    nome = message.from_user.username
    
    bot.send_message(message.chat.id, "Ola " + nome + "," + " diga algo")

@bot.message_handler(func=lambda message: True)
def texto(message):
    nome = message.from_user.username
    
    global texto_usuario
    texto_usuario = message.text
    print("_______________________________")
    print(Fore.MAGENTA +  "_________BOT  LUNNA__________")
    print(Style.RESET_ALL) #Volta a cor padrão
    print("USUARIO:  " + nome)
    print("MENSAGEM: "+ texto_usuario)

    
    # FAZER A PESQUISA
    
    buscar = wikipedia.search(texto_usuario)
    
    if buscar:
        pesquisa = wikipedia.page(buscar[0])
        resumo = wikipedia.summary(pesquisa.title, sentences=2)  # Obtendo o resumo do artigo
        bot.send_message(message.chat.id, resumo)
        
        print("______Resposta entregue_______")
        print("    ")
        
    else:
        bot.send_message(message.chat.id, "Não encontrei nada sobre ("+texto_usuario+") no meu banco de dados")
        print("__________Não Achei____________")
   
print(Fore.GREEN + " 😀 SEU BOT ESTA ONLINE 😁")

#print("RESPOSTA: " + resumo                  )
bot.polling()