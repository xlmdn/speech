import whisper
import tkinter as tk
import sounddevice as sd
import scipy.io.wavfile as wav
import threading
import speech_recognition as sr

def iniciar_grabacion():
    global grabacion  
    etiqueta.config(text="Grabando...")
    fs = 44100  
    grabacion = sd.rec(int(fs * 5), samplerate=fs, channels=1)

def detener_grabacion_y_procesar():
    global grabacion
    sd.stop()
    etiqueta.config(text="Grabación detenida")
    wav.write("grabacion.mp3", 44100, grabacion) 
    procesar_audio("grabacion.mp3")

def procesar_audio(archivo_audio):
    model = whisper.load_model("base")
    result = model.transcribe(archivo_audio)
    etiqueta.config(text=result["text"])
    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Grabar y Procesar Audio")

# Crear la etiqueta para mostrar el texto
etiqueta = tk.Label(ventana, text="Presiona 'Iniciar' para comenzar")
etiqueta.pack()

# Crear los botones
boton_iniciar = tk.Button(ventana, text="Iniciar", command=lambda: threading.Thread(target=iniciar_grabacion).start())
boton_iniciar.pack()

boton_detener = tk.Button(ventana, text="Detener y Procesar", command=detener_grabacion_y_procesar)
boton_detener.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()








model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])