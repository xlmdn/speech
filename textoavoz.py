import tkinter as tk
from tkinter import messagebox
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="sk_9b045d4b91ed7ae44a49b6bb0f81093f64bf8b2c8442a0ad", 
)

def guardar_audio(texto):
    #texto = cuadro_texto.get("1.0", tk.END) 
    if texto.strip(): 
        voces = client.voices.get_all()
        audio = client.generate(
            text=texto,
            voice=("Arnold"),
            #voice=voces.voices[3], 
            model="eleven_multilingual_v2"
        )
        #save(audio, "audio.mp3")
        play(audio)
    else:
       messagebox.showinfo("Error","Por favor, ingresa texto antes de guardar el audio.")

