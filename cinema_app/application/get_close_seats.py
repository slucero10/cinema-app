import typing

from .get_hallways import GetHallways
from ..domain.models.silla import Silla
from ..domain.repositories.silla_repository import SillaRepository
from ..infraestructure.implementation.pasillo_sql_repository import PasilloSQLRepository

class GetCloseSeats:

    def __init__(self, silla_repository: SillaRepository):
        self.silla_repository = silla_repository
        self.pasillo_repository = PasilloSQLRepository()

    def run(self, seat: Silla, num_seats: int) -> typing.List[Silla]:
        get_hallways_use_case = GetHallways(self.pasillo_repository)
        hallways = get_hallways_use_case.run(seat.sala_id)
        close_seats = self.silla_repository.get_adjacent_seats(seat, num_seats, hallways)
        return close_seats
