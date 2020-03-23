from telegram.ext import Updater, CommandHandler
import getStats

#nuestro token
token = open('BotToken.txt', 'r').readline()

#creamos todas las funciones que queramos
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Activo!")

def statsGlobal(update, context):
    datos = getStats.datosGlobales(getStats.driver)
    actualizacion = getStats.fechaActualizacion(getStats.driver)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="ACTUALIZACIÓN: " +
                             actualizacion[0] + " a las " + actualizacion[1] +
                             "\n————————————————————————"
                             "\nNº de casos: " + datos[0] +
                             "\nCasos últimas 24h: " + datos[1] +
                             "\nNº de recuperados: " + datos[2] +
                             "\nNº hospitalizados: " + datos[3] +
                             "\nNº de fallecidos: " + datos[4])


#programa principal
def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    #start handler
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)  # registramos el comando en el dispatcher

    #stats handler
    stats_handler = CommandHandler("global", statsGlobal)
    dispatcher.add_handler(stats_handler)


    updater.start_polling()

if __name__ == '__main__':
    main()
