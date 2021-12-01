import pyautogui
import speech_recognition as sr
import pywhatkit
import pyttsx3
import subprocess
from datetime import datetime
import time
import os

engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

rutaz = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData\\Roaming\\Zoom\\bin\\') #Ruta del ZOOM cambiar si solo lo tiene instalado en otra ruta
setHora = "30/11/21 20:33" # Configuramos día y hora de la reunión
setHoraR = setHora.replace('30/11/21', '').strip() # utilizamos el strip para quitar la fecha y solo dejar la hora
talk(f"Zoom creara una reunión a las: " + setHoraR) # La computadora dira a la hora que se efectua la reunión solo en horas y minutos

def join(id, password):

    # Abrimos Zoom
    subprocess.call(f"{rutaz}Zoom.exe")
    print("Abriendo Zoom")
    
    while True:
        ingresoZoom = pyautogui.locateOnScreen("Crear1.png")
        if ingresoZoom != None: # verificando dos veces que ya se ha encontrado
            talk("Creando sala, porfavor espere...")
            pyautogui.click(ingresoZoom) # haciendo clic 
            break # detener el bucle para que pueda continuar
        else:
            # Si no encuentra entonces, le decimos que sigue buscando :))
            talk("Buscando sala...")
            time.sleep(2) # un poco de retraso para que no crashee
    
    # Find the ID input textbox
    talk(f"Bienvenido a la sala")
    time.sleep(3)
    pyautogui.hotkey('alt','u') #Abrimos el panel de participantes
    time.sleep(1)
    pyautogui.hotkey('alt','v') #Desconectamos el microfono
    pyautogui.hotkey('alt','a') #Desconectamos el video
    pyautogui.hotkey('alt','h') #Abrimos la pestaña del chat
    time.sleep(5)

    
# Ejecutando la función
while True:
    # Obtener la hora actual
    now = datetime.now()
    # Dar formato a la hora
    horaActual = (now.strftime("%d/%m/%y %H:%M"))
    # Verifique la hora
    if horaActual == setHora:
        # Ejecute la función y detenga el bucle
        join("ID", "CONTRASEÑA GENERADA")
        break
    else:
        # Retraso de 5 segundos antes de volver a comprobarlo
        time.sleep(5)
