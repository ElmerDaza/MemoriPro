import speech_recognition as sr

def escuchar():
    string_ = ""
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            print("te escucho--")
            audio = r.listen(source)
            text = r.recognize_google(audio, language='es-ES')
            print("Creo que lo que dijiste fue: {}".format(text))
            string_ = format(text)
            string_ = string_.lower()
    except Exception as e:
        print("|")
        print("|")
        print("|")
        print("|")
        print("Quizas no haya INTERNET ")
        print("Quieres ver el error error ")
        string_ = "error---"
        cn = input("escribe 'y' si es afirmativo _")

        if(cn=="y"):
            print("i am sorry! can not understand!   ___"+e)
           
        else:
           print("listo terminé")
    return string_