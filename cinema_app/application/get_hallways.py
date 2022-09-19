import typing

from ..domain.models.pasillo import Pasillo
from ..domain.repositories.pasillo_repository import PasilloRepository

class GetHallways:

    def __init__(self, pasillo_repository: PasilloRepository):
        self.pasillo_repository = pasillo_repository

    def run(self, local_id: int) -> typing.List[Pasillo]:
        hallways = self.pasillo_repository.get_hallways_by_room(local_id)
        return hallways
