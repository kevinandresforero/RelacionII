import pymysql.cursors

contraseña = "261120"
Db = "Prueba"

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="261120",
                           database="Prueba")
cursor = conexion.cursor()

while op != 9:
    print("1. Crear Base de datos")
    print("2. Crear Tabla Students")
    print("3. Crear Tabla Materias")
    print("4. Crear Tabla Relaciones")
    print("5. Llenar tabla Students")
    print("6. Llenar tabla Materias")
    print("7. Llenar Relaciones")
    print("8. Mostrar Tablas")
    print("9. Borrar Tabla")
    op = int(input("Digite opcion: "))

    if op == 1:         # Crear Db
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
        )
        cursor = conexion.cursor()
        cursor.execute("SHOW DATABASES;")
        print("Conectado Ome")
        try:
            print("Creando...")
            cursor.execute("CREATE DATABASE Prueba;")
            print("Se creo satisfactoriamente la DB Prueba")
        except:
            print("Ya Fue Creada En Otra Ocación la DB Prueba")
        cursor.close()

    if op == 2:         #Crear tabla Estudiantes
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
        )
        cursor = conexion.cursor()

        try:
            print("Creando tablas Students...")
            Students = """CREATE TABLE Students(
                            IdE int NOT NULL,
                            NomE varchar(15) NOT NULL,
                            PRIMARY KEY(IdE)
            ) ;
            """

            print(" Tabla Studiants  craeada satisfactoriamente")
        except:
            print("Tabla Studiants ya existe")
        cursor.close()
        conexion.close()

    if op == 3:         #Crear tabla Materias
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
        )
        cursor = conexion.cursor()

        try:
            print("Creando tabla Materias...")

            Materias = """CREATE TABLE Materias(
                        idM int NOT NULL,
                        NomM varchar(15) NOT NULL,
                        PRIMARY KEY(idM)
            ) ;
            """
            print(" Tabla Materias  craeada satisfactoriamente")
        except:
            print("Tabla Materias ya existe")
        cursor.close()
        conexion.close()

    if op == 4:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
        )
        cursor = conexion.cursor()

        try:

            InsertarRegistro = """insert into Students(IdE, NomE) values
                                    (%s,%s)"""
            cursor.execute(InsertarRegistro, (Codigo, Nombre))

            Relaciones = """CREATE TABLE Relaciones(
                            idE_foran int NOT NULL,
                            idM_foran int NOT NULL,
                            FOREIGN KEY (idE_foran) REFERENCES Students(IdE),
                            FOREIGN KEY (idM_foran) REFERENCES Materias(idM)
                            );"""
            cursor.execute(Students)
            cursor.execute(Materias)
            conexion.commit()
            print("Creando tabla Relaciones ")
        except:
            print("Ya está creada las tabla Relaciones")

    Codigo = int(input("Digite codigo del estudiante: "))
    Nombre = input("Digite nombre del estudiante: ")
    TablaAlumnos = """"insert into Students() values
            (%s,%s,%s,%s,%s,%s)"""