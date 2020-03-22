from telegram.ext import Updater, CommandHandler
import getStats

#creamos todas las funciones que queramos
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Activo!")

def stats(update, context):
    datos = getStats.datos(getStats.driver)
    casos = datos[0]
    fallecidos = datos[1]
    recuperados = datos[2]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Número de casos: " + casos +
                             "\nNúmero de fallecidos: " + fallecidos +
                             "\nNúmero de recuperados: " + recuperados)


#programa principal
def main():
    updater = Updater(token='968373168:AAH0NErTU_0MdyUJDcjB9qm-D4ZtWP0lEo8', use_context=True)
    dispatcher = updater.dispatcher

    #start handler
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)  # registramos el comando en el dispatcher

    #stats handler
    stats_handler = CommandHandler("coronavirus", stats)
    dispatcher.add_handler(stats_handler)


    updater.start_polling()

if __name__ == '__main__':
    main()
