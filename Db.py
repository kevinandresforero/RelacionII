import pymysql.cursors
conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="261120",
                           database="Prueba")
cursor = conexion.cursor()

try:
    print("Creando tablas Students y Materias...")
    Students = """CREATE TABLE Students(
                    IdE int NOT NULL,
                    NomE varchar(15) NOT NULL,
                    PRIMARY KEY(IdE)
    ) ;
    """

    Materias = """CREATE TABLE Materias(
                idM int NOT NULL,
                NomM varchar(15) NOT NULL,
                PRIMARY KEY(idM)
    ) ;
    """
    Codigo = int(input("Digite codigo del estudiante: "))
    Nombre = input("Digite nombre del estudiante: ")

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
except:
    print("Ya están creadas las tablas Materias Y Students")


TablaAlumnos = """INSERT INTO Students VALUES(idE," ""