import sqlite3 as sl
from ...domain.models.sala import Sala
from ...domain.repositories.sala_repository import SalaRepository


class SalaSQLRepository(SalaRepository):
    db_con = sl.connect("cinema.db")


    def get_room_by_branch_and_id(self, room: Sala) -> Sala:
        with self.db_con:
            data = self.db_con.execute("SELECT * FROM sala WHERE id = ? AND local_id = ?", (room.id, room.local_id))\
                .fetchone()
            if data is None:
                raise Exception(f"No se encontró el local con id = {room.id} y local_id = {room.local_id} "
                                f"en la base de datos")
            return Sala(data[0], data[1])