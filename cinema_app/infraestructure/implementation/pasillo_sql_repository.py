import sqlite3 as sl
import typing

from ...domain.models.pasillo import Pasillo
from ...domain.repositories.pasillo_repository import PasilloRepository


class PasilloSQLRepository(PasilloRepository):
    db_con = sl.connect("cinema.db")


    def get_hallways_by_room(self, room_id: int) -> typing.List[Pasillo]:
        with self.db_con:
            data = self.db_con.execute("SELECT * FROM pasillo WHERE sala_id = ?", (room_id,))
            hallways = [Pasillo(*row) for row in data]
            return hallways