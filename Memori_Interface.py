import Memori_Fun as me
import Memori_RecorderVoice


while True:
    
    try:
        print("*****************************************")
        print("Estoy iniciando___")
        print("*****************************************")
        string_ = Memori_RecorderVoice.escuchar()
        if(string_ == "guárdame una palabra"
           or string_ == "crea una palabra"
           or string_ == "nueva palabra"
           or string_ == "crea una nueva palabra"
           or string_ == "crea una palabra nueva"
           or string_ == "quiero guardar una palabra"
           or string_ == "una palabra nueva"):
            print("Que bien amigo____Dime que Palabra guardaremos")
            r = Memori_RecorderVoice.escuchar()
            if(r != ""):
                res=r
                print("--------------------------------------------------------")
                print("Listo. dime un significado de  _"+res)
                print("--------------------------------------------------------")
            else:
                
                definicion = Memori_RecorderVoice.escuchar()
                me.Registrar(res,definicion,"palabras")
                print("--------------------------------------------------------")
                print("Ya se guardo la nueva Palabra ")
                print("--------------------------------------------------------")

            
        elif(
            string_ == "quiero crear una tabla" 
            or string_ == "créame una tabla" 
            or string_ == "quiero una tabla"
            or string_ == "guárdame una tabla"
            or string_ == "crea una tabla"
            or string_ == "nueva tabla"
            or string_ == "crea una nueva tabla"
            or string_ == "crea una tabla nueva"):
            print("--------------------------------------------------------")
            print("Bueno Dime Como se va A llamar la tabla")
            print("--------------------------------------------------------")
            res = Memori_RecorderVoice.escuchar()
            print("--------------------------------------------------------")
            print("Bueno le pondre _"+res)
            print("Dime como se llama la primera columna")
            print("--------------------------------------------------------")
            colum = [None]
            colum[0]=Memori_RecorderVoice.escuchar()
            print("--------------------------------------------------------")
            print("Bueno le pondre _"+colum[0])
            print("Quieres añadir otra columna?_")
            print("--------------------------------------------------------")
            m_ = Memori_RecorderVoice.escuchar()
            if (m_ == "si" or m_ =="sí"):
                i=0
                while (i<10):

                    if(i != 0):
                        print("--------------------------------------------------------")
                        print("Quieres añadir otra columna?_")
                        print("--------------------------------------------------------")
                        e_ =Memori_RecorderVoice.escuchar()
                        if(e_=="si" or e_=="sí"):
                            print("--------------------------------------------------------")
                            print("Dime como se llama la siguiente columna")
                            print("--------------------------------------------------------")
                            colum[i]=Memori_RecorderVoice.escuchar()
                            i=i+1
                        else:
                            i=12
                    else:
                        print("--------------------------------------------------------")
                        print("Dime como se llama la siguiente columna")
                        print("--------------------------------------------------------")
                        colum[i]=Memori_RecorderVoice.escuchar()
                        i = i+1
            else:
                me.TablaNueva(colum,res)
                print("--------------------------------------------------------")
                print("Listo. se creo la tabla")
                print("--------------------------------------------------------")
            if(i==12):
                me.TablaNueva(colum,res)
                

        
    except ValueError :
        print("--------------------------------------------------------")
        print("parece que hay un problema grave en el codigo':('")
        print("¿QUIERES VERLO?")
        print("--------------------------------------------------------")
        

