import tkinter as tk
import textoavoz as tv
import vozatexto as vt

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("SPEECH")
ventana.geometry("800x300")
ventana.resizable(False, False)
#titulo1
etiqueta_tv= tk.Label(ventana, text="Texto a Voz")
etiqueta_tv.place(x=10, y=10,width=380, height=20)

# Área de texto
texto_area = tk.Text(ventana)
texto_area.place(x=10, y=40, width=385, height=200)

# Botón "Generate Speech"
boton_generar = tk.Button(ventana, text="Generar voz", 
                          command=lambda: tv.guardar_audio(texto_area.get("1.0", tk.END)))
boton_generar.place(x=170, y=250)

#titulo2
etiqueta_vt= tk.Label(ventana, text="Voz a Texto")
etiqueta_vt.place(x=410, y=10,width=380, height=20)

# Crear la etiqueta con un tamaño de fuente más grande y estilo
etiqueta = tk.Label(ventana, text="", bg="gray",wraplength=380)
etiqueta.place(x=410, y=40, width=385, height=200)


# Crear el botón con un tamaño más grande y estilo
boton = tk.Button(ventana, text="Iniciar Reconocimiento de Voz", 
                  command=lambda:vt.iniciar_reconocimiento_voz(etiqueta)
                  )
boton.place(x=500, y=250)



ventana.mainloop()