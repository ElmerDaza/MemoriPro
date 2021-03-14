from gtts import gTTS
from playsound import playsound
import os


def archivo(text):
    with open("archivo.txt","w") as file:
        file.write(text)
        file.close()


def Hablar(text,idioma):
    i=0
    while i!= -1:

        try:

            archivo(text)
            with open("archivo.txt","r") as file:
                te=file.read()
            file = gTTS(text=te, lang=idioma)
            if(i!=0):
                nombre = ("archivo{}.mp3".format(i))
            else:
                nombre = "archivo.mp3"
            file.save(nombre)
            i=-1
            playsound(nombre)
            os.remove(nombre)
            os.remove("archivo.txt")
        except PermissionError as e:
            i=i+1
            if(e=="#"):
                print("i am sorry! can not understand!   ___"+e)
           
            

