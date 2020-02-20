import pymysql.cursors

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="261120",
                           database="Prueba")

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

Relaciones = """CREATE TABLE Relaciones(idE_foran int, idM_foran int,
FOREING KEY (idA_foran) REFERENCES Estudiantes(idE),
FOREING KEY (idM_foran) REFERENCES Materias(idM)
);
"""

cursor = conexion.cursor()
cursor.execute(Relaciones)
cursor.execute(Estudiantes)
cursor.execute(Materias)
cursor.close()


conexion.commit()
conexion.close()

