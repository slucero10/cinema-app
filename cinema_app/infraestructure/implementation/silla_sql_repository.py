import sqlite3 as sl
import typing
from ...domain.models.silla import Silla
from ...domain.models.pasillo import Pasillo
from ...domain.repositories.silla_repository import SillaRepository


class SillaSQLRepository(SillaRepository):
    db_con = sl.connect("cinema.db")

    def get_seat(self, seat: Silla) -> Silla:
        with self.db_con:
            data = self.db_con.execute("SELECT * FROM silla WHERE sala_id = ? AND fila = ? AND columna = ?",
                                       (seat.sala_id, seat.fila, seat.columna)).fetchone()
            if data is None:
                raise Exception(f"No se encontró la silla {seat.fila}{seat.columna} en la sala {seat.sala_id}")
            return Silla(data[0], data[1], data[2], data[3], data[4])


    def get_adjacent_seats(self, seat: Silla, num_seats: int, hallways: typing.List[Pasillo]) -> \
            typing.List[typing.List[Silla]]:
        with self.db_con:
            data = self.db_con.execute("SELECT * FROM silla WHERE sala_id = ? AND fila = ?", (seat.sala_id, seat.fila))
            row_seats = [Silla(*row) for row in data]
            row_seats.sort(key=lambda x: x.columna)
            arranges = []
            for idx, s in enumerate(row_seats):
                arranges.append([])
                for n in range(num_seats):
                    if idx + n < len(row_seats):
                        if any(h.columna_izq == row_seats[idx + n].columna for h in hallways):
                            if n == num_seats - 1:
                                arranges[idx].append(row_seats[idx + n])
                            break
                        else:
                            arranges[idx].append(row_seats[idx + n])
                    else:
                        break
            result = []
            for arrange in arranges:
                if any(s.id == seat.id for s in arrange) and len(arrange) == num_seats:
                    result.append(arrange)

            return result