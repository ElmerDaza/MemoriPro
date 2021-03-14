import Memori_Fun as me
import Memori_RecorderVoice
import Memori_Hablar


while True:
    i=1
    try:
        print("*****************************************")
        print("Estoy iniciando___")
        print("*****************************************")
        string_ = Memori_RecorderVoice.escuchar()
        if(string_ == "guárdame una palabra"
           or string_ == "crea una palabra"
           or string_ == "guárdame otra palabra"
           or string_ == "nueva palabra"
           or string_ == "crea una nueva palabra"
           or string_ == "crea una palabra nueva"
           or string_ == "quiero guardar una palabra"
           or string_ == "una palabra nueva"):
            print("Que bien amigo____Dime que Palabra guardaremos")
            r = Memori_RecorderVoice.escuchar()
            if(r != ""):
                res=r
                print("|")
                print("|")
                print("|")
                print("|")
                print("--------------------------------------------------------")
                print("Listo. dime un significado de  _"+res)
                print("--------------------------------------------------------")
                definicion = Memori_RecorderVoice.escuchar()
                me.Registrar(res,definicion,"palabras")
                print("|")
                print("|")
                print("|")
                print("|")
                print("--------------------------------------------------------")
                print("Ya se guardo la nueva Palabra ")
                print("--------------------------------------------------------")

            
                
                

            
        elif(string_ == "quiero crear una tabla" 
            or string_ == "créame una tabla" 
            or string_ == "quiero una tabla"
            or string_ == "guárdame una tabla"
            or string_ == "crea una tabla"
            or string_ == "nueva tabla"
            or string_ == "tabla"
            or string_ == "crear una tabla"
            or string_ == "crear tabla"
            or string_ == "tabla nueva"
            or string_ == "crea una nueva tabla"
            or string_ == "crea una tabla nueva"):
            print("|")
            print("|")
            print("|")
            print("|")
            print("--------------------------------------------------------")
            print("Bueno Dime Como se va A llamar la tabla")
            print("--------------------------------------------------------")
            res = Memori_RecorderVoice.escuchar()
            print("|")
            print("|")
            print("|")
            print("|")
            print("--------------------------------------------------------")
            print("Bueno le pondre _"+res)
            print("Dime como se llama la primera columna")
            print("--------------------------------------------------------")
            colum = [""]*10
            colum[0]=Memori_RecorderVoice.escuchar()
            print("|")
            print("|")
            print("|")
            print("|")
            print("--------------------------------------------------------")
            print("Bueno le pondre _"+colum[0])
            print("Quieres añadir otra columna?_")
            print("--------------------------------------------------------")
            m_ = Memori_RecorderVoice.escuchar()
            if (m_ == "si" or m_ =="sí"):
                
                while (i<10):

                    if(i != 1):
                        print("|")
                        print("|")
                        print("|")
                        print("|")
                        print("--------------------------------------------------------")
                        print("Quieres añadir otra columna?_")
                        print("--------------------------------------------------------")
                        e_ =Memori_RecorderVoice.escuchar()
                        if(e_=="si" or e_=="sí"):
                            print("|")
                            print("|")
                            print("|")
                            print("|")
                            print("--------------------------------------------------------")
                            print("Dime como se llama la siguiente columna")
                            print("--------------------------------------------------------")
                            colum[i]=Memori_RecorderVoice.escuchar()
                            i=i+1
                        else:
                            i=12
                    else:
                        print("|")
                        print("|")
                        print("|")
                        print("|")
                        print("--------------------------------------------------------")
                        print("Dime como se llama la siguiente columna")
                        print("--------------------------------------------------------")
                        colum[i]=Memori_RecorderVoice.escuchar()
                        i = i+1
            else:
                print("|")
                print("|")
                print("|")
                print("|")
                print("--------------------------------------------------------")
                print("SE CREARA NUEVA TABLA NE NOMBRE _"+res+" EJECUTO LA ORDEN:_")
                print("--------------------------------------------------------")
                r_= Memori_RecorderVoice.escuchar()
                
                if(r_=="si" or r_=="sí"):
                    me.TablaNueva(colum,res)
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("--------------------------------------------------------")
                    print("Listo. se creo la tabla")
                    print("--------------------------------------------------------")
                elif(r_=="no" or r_=="nó"):
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("--------------------------------------------------------")
                    print("bueno_")
                    print("--------------------------------------------------------")
                elif(r_=="error---" ):
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("--------------------------------------------------------")
                    print("no escuche nada queres volver a intentarlo")
                    print("--------------------------------------------------------")
                    inh=input("escriba y para afirmativo__")
                    if(inh=="y"):
                        me.TablaNueva(colum,res)
                        print("|")
                        print("|")
                        print("|")
                        print("|")
                        print("--------------------------------------------------------")
                        print("Listo. se creo la tabla")
                        print("--------------------------------------------------------")
                
            if(i==12):
                print("|")
                print("|")
                print("|")
                print("|")
                print("--------------------------------------------------------")
                print("SE CREARA NUEVA TABLA NE NOMBRE _"
                +res+" \n\nEJECUTO LA ORDEN?:_  ******************************")
                print("--------------------------------------------------------")
                r_= Memori_RecorderVoice.escuchar()
                
                if(r_=="si" or r_=="sí"):
                    me.TablaNueva(colum,res)
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("--------------------------------------------------------")
                    print("Listo. se creo la tabla")
                    print("--------------------------------------------------------")
                elif(r_=="no" or r_=="nó"):
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("--------------------------------------------------------")
                    print("bueno_")
                    print("--------------------------------------------------------")
                elif(r_=="error---" ):
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("--------------------------------------------------------")
                    print("no escuche nada queres volver a intentarlo")
                    print("--------------------------------------------------------")
                    inh=input("escriba y para afirmativo__")
                    if(inh=="y"):
                        me.TablaNueva(colum,res)
                        print("|")
                        print("|")
                        print("|")
                        print("|")
                        print("--------------------------------------------------------")
                        print("Listo. se creo la tabla")
                        print("--------------------------------------------------------")

        elif(string_ == "dime una palabra"
        or string_ == "palabra"
        or string_ == "dame palabra"
        or string_ == "abre una palabra"
        or string_ == "abre palabra"
        or string_ == "dime una palabra"
        or string_ == "que es"
        or string_ == "qué es"
        or string_ == "que significa esta palabra palabra"
        or string_ == "que significa"):

            print("|")
            print("|")
            print("|")
            print("|")
            print("--------------------------------------------------------")
            print("OK.... dime que palabra has guardado.")
            print("--------------------------------------------------------")
            res = Memori_RecorderVoice.escuchar()
            co = me.Consulta(res,"palabras")
            if(len(co) != 0):
                print("|")
                print("|")
                print("|")
                print("|")
                print("--------------------------------------------------------")
                print("Esto fue lo que encontré._\n\n\n"+co[0][2]+"\n\n\nQuieres REPRODUCIR?._")
                print("--------------------------------------------------------")
                res1 = Memori_RecorderVoice.escuchar()
                if(res1=="si" or res1=="sí"):
                    Memori_Hablar.Hablar(co[0][2],"es-ES")

            else:
                print("|")
                print("|")
                print("|")
                print("|")
                print("--------------------------------------------------------")
                print("esa palabra NO ESTA GUARDADA\n\nQUIERES GUARDAR ESTA PALABRA.  _"+res)
                print("--------------------------------------------------------")
                res1 = Memori_RecorderVoice.escuchar()
                if(res1 == "si" or res1 == "sí"):
                    print("------")
              
        elif(string_ == "apagate" 
        or string_ =="apagar"
        or string_ =="detente"
        or string_ =="deten el programa"):
            exit(0)
        
    except ValueError :
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------------------------------------------------------")
        print("parece que hay un problema grave en el codigo':('")
        print("¿QUIERES VERLO?")
        print("--------------------------------------------------------")
        

