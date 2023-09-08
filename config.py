# Load config from yaml file
from decouple import config


# Configura el token de tu bot de Telegram
TOKEN = config("API_TOKEN") 

# ID del chat al que quieres enviar las notificaciones
CHAT_ID = config("CHAT_ID")

# Nombre del archivo en el que se guardarán los mensajes
LOG_FILENAME = config("LOG_FILENAME")