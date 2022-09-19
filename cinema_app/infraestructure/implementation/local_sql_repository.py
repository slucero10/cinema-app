import sqlite3 as sl
from ...domain.models.local import Local
from ...domain.repositories.local_repository import LocalRepository


class LocalSQLRepository(LocalRepository):
    db_con = sl.connect("cinema.db")


    def get_branch_by_id(self, branch_id: int) -> Local:
        with self.db_con:
            data = self.db_con.execute("SELECT * FROM local WHERE id = ?", (branch_id,)).fetchone()
            if data is None:
                raise Exception(f"No se encontró el local con id = {branch_id} en la base de datos")
            return Local(data[0])