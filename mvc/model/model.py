import mysql.connector
from mysql.connector import errorcode

class Alumnos():
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_agenda', 
                password='Agenda_2020',
                host='127.0.0.1',
                port=3306,
                database='escuela')
            print("Conectado")
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print("Error connect: ", e)
    
    def select(self):
        try:
            self.connect()
            query=('SELECT * FROM alumnos;')
            self.cursor.execute(query)
            result=[]
            for row in self.cursor:
                r = {
                    'id_persona' : row[0],
                    'matricula' : row[1],
                    'nombre' : row[2],
                    'ap_paterno' : row[3],
                    'ap_materno' : row[4],
                    'edad' : row[5],
                    'fecha_nac' : row[6],
                    'genero' : row[7],
                    'estado' : row[8],
                    }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print("Error Select: ", e)
            result =[]
            return result

objeto=Alumnos()
objeto.connect()

for row in objeto.select():
    print(row)