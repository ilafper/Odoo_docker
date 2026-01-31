# comando para instalar las libreria de request                pip install python-telegram-bot requests 
# import de la librerias
from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler, MessageHandler, ContextTypes, filters
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
# el token que nos pasara el bot de telegram
#TOKEN = "8266994992:AAFIDAke9iL8Dj7_1baUQCRBWXdPXUEeSnM"
#la url de la api

#variables de entorno de la url de la api, de la mostrar todos y el token de telegram bot
API_URL=os.getenv("API_URL")

API_URL_TODOS_SOCIOS=os.getenv("API_URL_TODOS_SOCIOS")

TOKEN = os.getenv("TOKEN_TELEGRAM_BOT")

# API_URL = "http://localhost:9001/gestion/apirest/socio"
# API_URL_MOSTRAR_TODOS = "http://localhost:9001/gestion/socio"



mensaje_inicial="""
¡Hola! Bienvenido al bot.
"""







# funcion para las ordenes
async def ordenes_comandos_telegram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #leera el mensaje completo, por ejemplo: "Crear, nombre=”nombre”,apellidos=”apellidos”, num_socio=”numerosocio”"


    mensaje_que_le_mandamos = update.message.text

    try:
        # vamos a dividirlo en partes
        partes = mensaje_que_le_mandamos.split(",") # cuando le mandamos el mensaje seria como el formato que le mandamos arriba, loq ue haremos sera 
        #segmentarlo por las comas "," que daria algo asi : ["Crear", " nombre=Juan", "apellidos=Pérez", "num_socio=3"]

        # le indicamos que la orden es la posicion 0 osea la primera parte, usamos strip por si hay algun espacion para evitar problemas y pasarlo a minusculas
        orden = partes[0].strip().lower()

        # guardar los datos del usuarios, los campos y sus valores por ejemplo "nombre": "juan" y el resto si se lo mandasmos
        datos_orden = {}

        # recorrer cada parte del rsto de las instrucciones, pero empezamos a partir de la orden, se cogeria la parte de por ejemplo nombre= ivan y lo que siga
        for cada_parte in partes[1:]:

            tipo_orden, cada_campo = cada_parte.split("=")

            datos_orden[tipo_orden.strip()] = cada_campo.strip()

        # CREAR 
        if orden == "crear":
            print(datos_orden)
            datos_parseados=json.dumps(datos_orden)
            print("adasdjjffffufuf"+datos_parseados)
            # con la libreria de requests le indicamos el tipo de peticion que es(en este caso post), la parte de la url y los datos
            respuesta = requests.post(API_URL, datos_parseados)
            #mesajes para verlos en la terminal
            print(f"Se ha creado al usuario: {datos_orden}")
            
            # lo que te devuelve el bot de telegram con los que le hallas pasado
            await update.message.reply_text("se ha creado al socio correctamente: "+ respuesta.text)

        elif orden == 'todos':
            respuesta = requests.get(f"{API_URL_TODOS_SOCIOS}")
            print(f"Se muestran todos los usuarios OOKOKO: {respuesta}")
            await update.message.reply_text(respuesta.text)
                
        #Borrar
        elif orden =='borrar':

            datos_parseados=json.dumps(datos_orden)
            respuesta = requests.delete(f'{API_URL}?data={datos_parseados}')

            print(f"Se ha creado al usuario: {datos_orden}")

            await update.message.reply_text("se ha borrado al socio correctamente: "+respuesta.text)
        
        elif orden == 'put':
            datos_parseados=json.dumps(datos_orden)
            respuesta = requests.put(API_URL, datos_parseados)
            print(f"Se ha creado al usuario: {datos_orden}")

            await update.message.reply_text("se ha modificado al socio correctamente: "+ respuesta.text)

    except Exception as e:
        await update.message.reply_text("has puesto mal el formato de la orden, prueba de nuevo")





# comando /help 
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje_aiuda = """
    Lo que puedes hacer:

    • **Ver todos los socios**: todos
    • **Crear socio**: Crear, nombre=Juan, apellidos=fonso, num_socio=777 
    • **Borrar socio**: borrar, num_socio= [ numero del socio ]
    • **Modificar socio**: put ,num_socio=[ numero del socio para modificar ], [ campo a modificar]= valor a modificar
    """
    await update.message.reply_text(mensaje_aiuda)





def main():
    app = ApplicationBuilder().token(TOKEN).build()

    #cuando hacer /help llama a la funcion que mostrara el mensaje de ayuda, esto es gracias al commandhandler que son todos los mensajes  que empeicen por "/" mas el texto en nuestro caso es help y la fucnio
    app.add_handler(CommandHandler("help", ayuda))

    # para el resto de las ordenes que le ponemso 
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ordenes_comandos_telegram))
    #mesaje en la terminal del proyecto para ver si inicio correctamente
    print("Bot SISISI")
    
    app.run_polling()

if __name__ == "__main__":
    main()
