import logging
from threading import Thread
import time
import telegram
from telegram.ext import ApplicationBuilder,Updater, MessageHandler, filters
import asyncio

from config import TOKEN, CHAT_ID, LOG_FILENAME

# Crea una instancia de la clase `Bot` de python-telegram-bot
bot = telegram.Bot(token=TOKEN)

# Configura el registro de eventos para el bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Función para enviar la notificación
async def send_notification():
    message = "¡Pendejo Recuerda hacer tu daily notes!"
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Función para guardar los mensajes en un archivo de texto
async def log_message(update, context):
    chat_id = update.message.chat_id

    if str(chat_id) == CHAT_ID:
        user_id = update.message.from_user.id
        user_name = update.message.from_user.username
        message_text = update.message.text
        timestamp = update.message.date.strftime("%Y-%m-%d")
        
        try:
            with open(LOG_FILENAME, 'a') as log_file:
                log_file.write(f"{timestamp} - User ID: {user_id}, Username: @{user_name}, Message: {message_text}\n")
            with open('done', 'a') as done_file:
                done_file.write("Done")
            await update.message.reply_text("Mensaje guardado. \nGracias por tu responsabilidad.")
        except Exception as e:
            logger.error(f"Error al guardar el mensaje: {e}")
            await update.message.reply_text("Error al guardar el mensaje.")
    else:
        await update.message.reply_text("No tienes permiso para usar este bot.")

    


# Crea una instancia de la clase `Updater` de python-telegram-bot
# bot = telegram.Bot(token=TOKEN)

# updater = Updater(bot=bot, )
# dispatcher = updater.dispatcher

# # Agrega un manejador para registrar los mensajes en el archivo de texto
# message_handler = MessageHandler(filters.Text & ~filters.COMMAND, log_message)
# dispatcher.add_handler(message_handler)
async def main():
    await bot.send_message(chat_id=CHAT_ID, text="¡Pendejo Recuerda hacer tu daily note!")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

    app = ApplicationBuilder().token(TOKEN).build()
    message_handler = MessageHandler(filters.ALL, log_message)
    app.add_handler(message_handler)
    
    # start the bot 
    # app.bot.send_message(chat_id=CHAT_ID, text="¡Recuerda hacer tus daily notes pendejo!")
    loop.create_task(app.run_polling())
    

    