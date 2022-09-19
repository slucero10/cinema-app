import abc

from ..models.local import Local


class LocalRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_branch_by_id(self, branch_id: int) -> Local:
        raise NotImplementedError
