import mysql.connector

def Conectar():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="memori"
        )
    return mydb

#_______________________________________
def Consulta(query, tabla):
    BD = Conectar()
    mycursor = BD.cursor()

    sql = "SELECT * FROM "+tabla+" WHERE palabra ='"+query+"'"

    mycursor.execute(sql)

    data = mycursor.fetchall()
    return data

#_______________________________________
def Registrar(palabra,consepto,tabla):
    BD = Conectar()
    mycursor = BD.cursor()
    sql = "INSERT INTO "+tabla+" (ID, palabra,comsepto) VALUES (%s, %s,%s)"
    val = (0, palabra, consepto)
    mycursor.execute(sql, val)
    BD.commit()

#_________________________________________
def TablaNueva(columnasNAME,tablaNAME):
    dec =""
    BD = Conectar()
    mycursor = BD.cursor()
    le=columnasNAME.__len__()
    for i in range (0,le):
        dec +="`"+format(columnasNAME[i])+"` TEXT NOT NULL ,"

    mycursor.execute(
        "CREATE TABLE `memori`.`"
        +tablaNAME+
        "` ( `id` INT(50) NOT NULL AUTO_INCREMENT , "
        +dec+" PRIMARY KEY (`id`)) ENGINE = InnoDB COMMENT = 'un comentario'"
        )
    print("ya cree la tabla _"+tablaNAME+" con las columnas _")
            
    
















    
