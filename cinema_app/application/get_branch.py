from ..domain.models.local import Local
from ..domain.repositories.local_repository import LocalRepository

class GetBranch:

    def __init__(self, local_repository: LocalRepository):
        self.local_repository = local_repository

    def run(self, branch_id: int) -> Local:
        branch = self.local_repository.get_branch_by_id(branch_id)
        return branch
