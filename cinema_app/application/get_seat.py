from ..domain.models.silla import Silla
from ..domain.repositories.silla_repository import SillaRepository

class GetSeat:

    def __init__(self, silla_repository: SillaRepository):
        self.silla_repository = silla_repository

    def run(self, seat: Silla) -> Silla:
        selected_seat = self.silla_repository.get_seat(seat)
        return selected_seat
