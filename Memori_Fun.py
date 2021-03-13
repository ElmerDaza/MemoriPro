import mysql.connector

def Conectar():
    DB_HOST = 'localhost'
    DB_USER='root'
    DB_PASS=''
    DB_NAME='memori'
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
    BD = Conectar()
    mycursor = BD.cursor()
    mycursor.execute(
        "CREATE TABLE `memori`.`"
        +tablaNAME+
        "` ( `id` INT(50) NOT NULL AUTO_INCREMENT , `"
        +Colum+"` TEXT NOT NULL , `"
        +Colum2
        +"` TEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB COMMENT = 'un comentario'"
        )
    print("ya cree la tabla _"+palabra+" con las columnas _"+Colum+" _"+Colum2)
            
    
















    
