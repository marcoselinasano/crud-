from typing import Any
import cx_Oracle

class conexionBD():
    usuario  ="INACAP_C2"
    password = "inacap"
    dsn      ="localhost/xe"
    
    def __init__(self):
            try:
                self.conexion = cx_Oracle.connect(    user=self.usuario,
                                password=self.password,
                                    dsn = self.dsn 
                                                 )
                print("la conexion ha sido todo un exito ")
            except cx_Oracle.DatabaseError as e:
                print(f"error al conectarse al la base de datos{e}")
conexion= conexionBD()

        