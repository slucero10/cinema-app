import abc

from ..models.sala import Sala


class SalaRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_room_by_branch_and_id(self, room: Sala) -> Sala:
        raise NotImplementedError
