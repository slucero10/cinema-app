import abc
import typing

from ..models.silla import Silla
from ..models.pasillo import Pasillo


class SillaRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_seat(self, seat: Silla) -> Silla:
        raise NotImplementedError

    @abc.abstractmethod
    def get_adjacent_seats(self, seat: Silla, num_seats: int, hallways: typing.List[Pasillo]) -> \
            typing.List[typing.List[Silla]]:
        raise NotImplementedError
