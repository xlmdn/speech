import speech_recognition as sr

def iniciar_reconocimiento_voz(etiqueta):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language='es-MX')
        etiqueta.config(text= texto)
    except sr.UnknownValueError:
        etiqueta.config(text="No se pudo entender el audio")
    except sr.RequestError as e:
        etiqueta.config(text=f"Error al solicitar resultados; {e}")