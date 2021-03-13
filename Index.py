import speech_recognition as sr

import mysql.connector

#enconding: utf-8

DB_HOST = 'localhost'
DB_USER='root'
DB_PASS=''
DB_NAME='memori'

# Connect to server on localhost



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="memori"
)
#_______________________________________
def Consulta(query): 
    mycursor = mydb.cursor()

    sql = "SELECT * FROM palabras WHERE palabra ='"+query+"'"

    mycursor.execute(sql)

    data = mycursor.fetchall()
    for x in data:
        print(x)






#__________________________
r = sr.Recognizer()
with sr.Microphone() as source:
  print("te escucho--")
  audio = r.listen(source)
  try:
    text = r.recognize_google(audio, language='es-ES')
    print("Creo que lo que dijiste fue: {}".format(text))
    string_ = format(text)
    string_ =string_.lower()
    if(string_ == "guárdame una palabra" or string_ == "crea una palabra" or string_ == "nueva palabra" or string_ == "crea una nueva palabra"):
      print("Que bien amigo____Dime que Palabra guardaremos")
      audio = r.listen(source)
      text = r.recognize_google(audio, language='es-ES')
      palabra = format(text)
      print("--------------------------------------------------------")
      print("Listo. que significa _"+palabra)
      print("--------------------------------------------------------")
      audio = r.listen(source)
      text = r.recognize_google(audio, language='es-ES')
      consepto = format(text).lower()
      print("--------------------------------------------------------")
      print("Listo.  ya estoy guardando lo que significa _"+palabra)
      print("--------------------------------------------------------")
      mycursor = mydb.cursor()
      sql = "INSERT INTO palabras (ID, palabra,comsepto) VALUES (%s, %s,%s)"
      val = (0, palabra, consepto)
      mycursor.execute(sql, val)

      mydb.commit()
      
      
      
      
      
      
    elif(string_ == "quiero crear una tabla"):
        print("--------------------------------------------------------")
        print("Bueno Dime Como se va A llamar la tabla")
        print("--------------------------------------------------------")
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        palabra = format(text)
        print("--------------------------------------------------------")
        print("Bueno le pondre _"+palabra)
        print("Dime como se llama la primera columna")
        print("--------------------------------------------------------")
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        Colum = format(text)
        print("--------------------------------------------------------")
        print("Bueno le pondre _"+Colum)
        print("Quieres añadir otra columna?_")
        print("--------------------------------------------------------")
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        Resp = format(text)
        Resp =Resp.lower()
        if(Resp=="si" or Resp == "sí"):
            print("--------------------------------------------------------")
            print("Dime como se llama la siguiente columna")
            print("--------------------------------------------------------")
            audio = r.listen(source)
            text = r.recognize_google(audio, language='es-ES')
            Colum2 = format(text)
            Colum2 = Colum2.lower()
            print("--------------------------------------------------------")
            print("ok sigo trabajando en la tabla.....")
            print("--------------------------------------------------------")
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE `memori`.`"+palabra+"` ( `id` INT(50) NOT NULL AUTO_INCREMENT , `"+Colum+"` TEXT NOT NULL , `"+Colum2+"` TEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB COMMENT = 'un comentario'")
            print("ya cree la tabla _"+palabra+" con las columnas _"+Colum+" _"+Colum2)
            
        else:
            print("--------------------------------------------------------")
            print("ok sigo trabajando en la tabla.....")
            print("--------------------------------------------------------")
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE `memori`.`"+palabra+"` ( `id` INT(50) NOT NULL AUTO_INCREMENT , `"+Colum+"` TEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB COMMENT = 'un comentario'")
            print("ya cree la tabla _"+palabra+" con las columnas _"+Colum)

            
            
    elif(string_ == "quiero una palabra" or string_ == "quiero saber una palabra" or string_== "dime una palabra" or string_ =="busco una palabra"):
        print("--------------------------------------------------------")
        print("Bueno.  Dime Cual Palabra__")
        print("--------------------------------------------------------")
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        palabra = format(text)
        Consulta(palabra)
                
    
  except Exception as e:
    print("i am sorry! can not understand!   ___"+e)


