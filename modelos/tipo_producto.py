from oracleConexion import conexionBD

class  tipoProducto:

    def __init__(self) -> None:
        self.conexion= conexionBD

    def ObeterTodos(self):
       cursor = self.conexion.cursor()#creo el objeto que usare para interactuar con el sql cursor
       SQL= '''
            SELECT * FROM TipoProducto
            '''
       cursor.executer(SQL)#executer ejecuta la consulta
       row =cursor.fetchall()#y fetchall mustra TODOS los ficheros

       for i in row:
          print(f"Id:{row[0]}, nombre:{row[1]}")
       
    def  insertar(self,nombre):
        
        cursor = self.conexion()

        cursor.execute("SELECT COUNT(*) FROM TipoProducto WHERE nombre = :nombre", [nombre])
        if cursor.fetchone()[0]>0:
             print(f"el tipo de produto '{nombre}' ya existe.")
            
            
        else:
            SQL = '''
                    INSERT INTO TipoProducto(nombre) Values(:nombre)
                  '''
            cursor.execute(SQL[2])
            self.conexion.commit()
            print("el Tipo de producto ha sido insertado con exito")
    def actualizar():
        None
    def eliminar(self):
        pass