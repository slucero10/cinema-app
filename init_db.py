import sqlite3 as sl


def connect_to_db(db_name):
    return sl.connect(db_name)


def create_tables(con):
    with con:
        con.executescript("""
            CREATE TABLE IF NOT EXISTS local (
               id int NOT NULL CONSTRAINT local_pk PRIMARY KEY
            );
            CREATE TABLE IF NOT EXISTS sala (
               id int NOT NULL CONSTRAINT sala_pk PRIMARY KEY,
               local_id int NOT NULL,
               FOREIGN KEY (local_id) REFERENCES local (id)
            );
            CREATE TABLE IF NOT EXISTS silla (
               id int NOT NULL CONSTRAINT silla_pk PRIMARY KEY,
               sala_id int NOT NULL,
               fila char(1) NOT NULL,
               columna int NOT NULL,
               estado varchar(16) NOT NULL,
               FOREIGN KEY (sala_id) REFERENCES sala (id)
            );
            CREATE TABLE IF NOT EXISTS pasillo (
               id int NOT NULL CONSTRAINT pasillo_pk PRIMARY KEY,
               sala_id int NOT NULL,
               columna_izq int,
               columna_der int,
               FOREIGN KEY (sala_id) REFERENCES sala (id)
            );
            CREATE TABLE IF NOT EXISTS pelicula (
               id int NOT NULL CONSTRAINT pelicula_pk PRIMARY KEY,
               titulo_distribucion varchar(64) NOT NULL,
               titulo_original varchar(64) NOT NULL,
               genero varchar(16) NOT NULL,
               idioma_original varchar(16) NOT NULL,
               pais_origen varchar(16) NOT NULL,
               fecha_produccion date NOT NULL,
               duracion time NOT NULL,
               clasificacion varchar(8) NOT NULL,
               resumen varchar(255) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS horario (
               id int NOT NULL CONSTRAINT horario_pk PRIMARY KEY,
               sala_id int NOT NULL,
               pelicula_id int NOT NULL,
               fecha timestamp NOT NULL,
               FOREIGN KEY (sala_id) REFERENCES sala (id),
               FOREIGN KEY (pelicula_id) REFERENCES pelicula (id)
            );
            CREATE TABLE IF NOT EXISTS persona (
               id int NOT NULL CONSTRAINT persona_pk PRIMARY KEY,
               nombre int NOT NULL
            );
            CREATE TABLE IF NOT EXISTS reparto (
               id int NOT NULL CONSTRAINT reparto_pk PRIMARY KEY,
               pelicula_id int NOT NULL,
               persona_id int NOT NULL,
               personaje int NOT NULL,
               FOREIGN KEY (pelicula_id) REFERENCES pelicula (id),
               FOREIGN KEY (persona_id) REFERENCES persona (id)
            );
            CREATE TABLE IF NOT EXISTS director (
               id int NOT NULL CONSTRAINT director_pk PRIMARY KEY,
               pelicula_id int NOT NULL,
               persona_id int NOT NULL,
               rol int NOT NULL,
               FOREIGN KEY (pelicula_id) REFERENCES pelicula (id),
               FOREIGN KEY (persona_id) REFERENCES persona (id)
            );
        """,)


def insert_values(con):
    with con:
        con.executescript("""
            INSERT INTO "local" (id)
                VALUES (1);
            INSERT INTO "local" (id)
                VALUES (2);
            INSERT INTO "local" (id)
                VALUES (3);
            
            INSERT INTO sala (id,local_id)
                VALUES (1,1);
            INSERT INTO sala (id,local_id)
                VALUES (2,1);
            INSERT INTO sala (id,local_id)
                VALUES (3,2);
            INSERT INTO sala (id,local_id)
                VALUES (4,2);
            INSERT INTO sala (id,local_id)
                VALUES (5,3);
                
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(1, 1, 'a', 1, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(2, 1, 'a', 2, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(3, 1, 'a', 3, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(4, 1, 'a', 4, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(5, 1, 'a', 5, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(6, 1, 'a', 6, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(7, 1, 'a', 7, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(8, 1, 'b', 1, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(9, 1, 'b', 2, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(10, 1, 'b', 3, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(11, 1, 'b', 4, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(12, 1, 'b', 5, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(13, 1, 'b', 6, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(14, 1, 'b', 7, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(15, 2, 'a', 1, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(16, 2, 'a', 2, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(17, 2, 'a', 3, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(18, 2, 'a', 4, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(19, 2, 'a', 5, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(20, 2, 'b', 1, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(21, 2, 'b', 2, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(22, 2, 'b', 3, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(23, 2, 'b', 4, 'DISPONIBLE');
            INSERT INTO silla
                (id, sala_id, fila, columna, estado)
                VALUES(24, 2, 'b', 5, 'DISPONIBLE');
            INSERT INTO pasillo (id,sala_id,columna_izq,columna_der)
                VALUES (1,1,2,3);
            INSERT INTO pasillo (id,sala_id,columna_izq,columna_der)
                VALUES (2,1,5,6);
            INSERT INTO pasillo (id,sala_id,columna_der)
                VALUES (3,2,1);
            INSERT INTO pasillo (id,sala_id,columna_izq)
                VALUES (4,2,5);

        """,)

if __name__ == "__main__":
    db_con = connect_to_db("cinema.db")
    create_tables(db_con)
    insert_values(db_con)

