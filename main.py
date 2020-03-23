from telegram.ext import Updater, CommandHandler
import getStats

#nuestro token
token = '968373168:AAH0NErTU_0MdyUJDcjB9qm-D4ZtWP0lEo8'

#creamos todas las funciones que queramos
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Activo!")

def statsGlobal(update, context):
    datos = getStats.datosGlobales(getStats.driver)
    actualizacion = getStats.fechaActualizacion(getStats.driver)
    casos = datos[0]
    casos24 = datos[1]
    recuperados = datos[2]
    hospitalizados = casos[3]
    fallecidos = datos[4]
    fecha = actualizacion[0]
    hora = actualizacion[1]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="ACTUALIZACIÓN: " +
                             fecha + " a las " + hora +
                             "\n————————————————————————"
                             "\nNº de casos: " + casos +
                             "\nCasos últimas 24h: " + casos24 +
                             "\nNº de recuperados: " + recuperados +
                             "\nNº hospitalizados: " + hospitalizados +
                             "\nNº de fallecidos: " + fallecidos)


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
