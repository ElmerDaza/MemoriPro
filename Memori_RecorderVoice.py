import speech_recognition as sr

def escucrhar():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
        print("te escucho--")
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        print("Creo que lo que dijiste fue: {}".format(text))
        string_ = format(text)
        string_ =string_.lower()
        return string_
