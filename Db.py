import pymysql.cursors

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="261120",
                           database="Prueba")
cursor = conexion.cursor()
try:
    Estudiantes = """CREATE TABLE Students(
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
    cursor.execute(Estudiantes)
    cursor.execute(Materias)
    conexion.commit()
except:
    print("Ya estan creadas las tablas Estudiantes y Materias")

try:
    Relaciones = """CREATE TABLE Relaciones(idE_foran int, idM_foran int,
    FOREING KEY (idA_foran) REFERENCES Estudiantes(idE),
    FOREING KEY (idM_foran) REFERENCES Materias(idM)
    );
    """
    cursor.execute(Relaciones)
    conexion.commit()
except:
    print("No se pudo crear la tabla relaciones ... Paila Socio")
cursor.close()
conexion.close()

