import pyttsx3

def textoavoz(texto):
    engine= pyttsx3.init()
    engine.say(texto)  
    engine.runAndWait()

texto=input("Ingrese el texto que desea convertir a voz: ")
textoavoz(texto)