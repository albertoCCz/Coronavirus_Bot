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
                             "\n——————————————————————"
                             "\nNº de casos: " + datos[0] +
                             "\nCasos últimas 24h: " + datos[1] +
                             "\nNº de recuperados: " + datos[2] +
                             "\nNº hospitalizados: " + datos[3] +
                             "\nNº de fallecidos: " + datos[4])


def acumulada(update, context):
    acum = getStats.graficas(getStats.driver)[0]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=acum)


def acumuladaCasos(update, context):
    acumCasos = getStats.graficas(getStats.driver)[1]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=acumCasos)


def tablaComunidades(update, context):
    head = getStats.datosCCAA(getStats.driver)[0]
    body = getStats.datosCCAA(getStats.driver)[1]



#programa principal
def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    #start handler
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)  # registramos el comando en el dispatcher

    #global handler
    stats_handler = CommandHandler("global", statsGlobal)
    dispatcher.add_handler(stats_handler)

    #acumulado handler
    acum_handler = CommandHandler("acumulado", acumulada)
    dispatcher.add_handler(acum_handler)

    #acumuladoCasos handler
    acumCasos_handler = CommandHandler("acumuladoCasos", acumuladaCasos)
    dispatcher.add_handler(acumCasos_handler)


    updater.start_polling()

if __name__ == '__main__':
    main()
