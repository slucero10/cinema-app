from ..domain.models.sala import Sala
from ..domain.repositories.sala_repository import SalaRepository

class GetRoom:

    def __init__(self, sala_repository: SalaRepository):
        self.sala_repository = sala_repository

    def run(self, room: Sala) -> Sala:
        selected_room = self.sala_repository.get_room_by_branch_and_id(room)
        return selected_room
