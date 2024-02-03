import speech_recognition as sr
from random import randint
import subprocess as sub
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import os
from pygame import mixer
from tkinter import *
from PIL import ImageTk, Image
import threading as tr


ventana = Tk()
ventana.title("Asistente Virtual")
ventana.geometry("800x400")
ventana.resizable(0, 0)
ventana.configure(bg="blue")


comandos = '''


    Comandos que puedes usar:
    - Play...(repoduce una cancion)
    - Busca...(Busca en internet)
    - Abre...(Pagina web)
    - Alarma...(Confugura una alarma)
    - Escribe...(Escribe lo que digas)
    - Chiste...(Cuenta un chiste)
    - Termina...(Cierra el programa)
'''

label = Label(ventana, text="IA", bg="blue",
              fg="black", font=('Arial', 30, 'bold'))
label.pack(pady=10)

canvas_comandos = Canvas(bg='#2193b0', height=130, width=255)
canvas_comandos.place(x=0, y=0)
canvas_comandos.create_text(90, 50, text=comandos,
                            fill='black', font='Arial 10')

text_info = Text(ventana, bg='#2193b0', fg='black')
text_info.place(x=0, y=135, height=280, width=260)

foto = ImageTk.PhotoImage(Image.open("images.jpg"))
foto_window = Label(ventana, image=foto)
foto_window.pack(pady=5)


name = "assistant"
listener = sr.Recognizer()
engine = pyttsx3.init()

chistes = ["Que le dijo, un fideo a otro....... Oye, mi cuerpo pide salsa", "Sabes cual es el colmo de un calvo......... Tener ideas descabelladas",
           "Que le dice, un sapo a otro........... A que te doy un sopapo", "Que le dice, un cero a otro cero........... No somos nada",
           "Cual es el colmo, de un vampiro............ Ninguno, los vampiros, no tienen colmo, tienen colmillos, jajaja equis de",
           "Cual es el colmo, de un gallo........... Que se le ponga, la piel de gallina", "Que le dice, una naranja a otra............ Todavia, no he encontrado, a mi media naranja",
           "Que le dijo, el zapato al otro zapato............  Que vida mas arrastrada llevas, jajajaja", "Que le dijo, un piojo a un calvo.............. No te agaches que me resvalo",
           "Que le dice, un semáforo a otro............... No me mires, que me estoy cambiando",
           "Que le dijo, el enchufe al cable............... Sigeme la corriente"]

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sitios = {
    'google': 'google.com',
    'youtube': 'youtube.com',
    'facebook': 'facebook.com',
    'whatsapp': 'web.whatsapp.com',
    'gmail': 'accounts.google.com'
}


def talk(text):
    engine.say(text)
    engine.runAndWait()


def ReadAndTalk():
    text = text_info.get('1.0', 'end')
    talk(text)


def write_text(text):
    text_info.insert(INSERT, text)


def Listen():
    try:
        with sr.Microphone() as source:
            talk("Te escucho")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec


def clock(rec):
    num = rec.replace('alarma', '')
    num = num.strip()
    talk("Alarma activada a las " + num + " horas")
    if num[0] != '0' and len(num) < 5:
        num = '0' + num
    while True:
        if datetime.datetime.now().strftime('%H:%M') == num:
            print("DESPIERTA!!!!")
            mixer.init()
            mixer.music.load("alarma.mp3")
            mixer.music.play()
        else:
            continue
        if keyboard.read_key() == 's':
            mixer.music.stop()
            break


def run_AI():
    while True:
        rec = Listen()

        if 'play' in rec:
            music = rec.replace('play', '')
            print("Reproduciendo "+music)
            talk("Reproduciendo "+music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            buscar = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(buscar, 1)
            write_text(buscar+": " + wiki)
            talk(wiki)
            break

        elif 'alarma' in rec:
            t = tr.Thread(target=clock, args=(rec,))
            t.start()

        elif 'abre' in rec:
            for site in sitios:
                if site in rec:
                    sub.call(f'start msedge.exe  {sitios[site]}', shell=True)
                    print(f"Abriendo {site}")
                    talk(f"Abriendo {site}")

        elif 'chiste' in rec:
            ran = randint(0, 10)
            talk(chistes[ran])

        elif 'escribe' in rec:
            try:
                with open("nota.txt", "a") as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", "w")
                write(file)

        elif 'termina' in rec:
            talk("Adios")
            break


def write(f):
    talk("Que quieres que escriba")
    rec_write = Listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo puedes revisarlo")
    sub.Popen("nota.txt", shell=True)


def VozEspañol():
    Change_Voice(0)


def VozIngles():
    Change_Voice(1)


def Change_Voice(id):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)


boton_voz_Es = Button(ventana, text="Voz Español", fg="white", bg="red", font=(
    'Arial', 14, 'bold'), command=VozEspañol)
boton_voz_Es.place(x=600, y=80, width=120, height=30)

boton_voz_EU = Button(ventana, text="Voz Ingles", fg="white",
                      bg="red", font=('Arial', 14, 'bold'), command=VozIngles)
boton_voz_EU.place(x=600, y=150, width=120, height=30)

boton_listen = Button(ventana, text="Escuchar", fg="white",
                      bg="red", font=('Arial', 22, 'bold'), command=run_AI)
boton_listen.pack(pady=25)

boton_speak = Button(ventana, text="Hablar", fg="white",
                     bg="red", font=('Arial', 14, 'bold'), command=ReadAndTalk)
boton_speak.place(x=600, y=220, width=120, height=30)


ventana.mainloop()
