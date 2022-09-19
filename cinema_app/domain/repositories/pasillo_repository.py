import abc
import typing

from ..models.pasillo import Pasillo


class PasilloRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_hallways_by_room(self, room_id: int) -> typing.List[Pasillo]:
        raise NotImplementedError
