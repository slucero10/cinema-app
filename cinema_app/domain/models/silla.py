from dataclasses import  dataclass


@dataclass
class Silla:
    id: int
    sala_id: int
    fila: str
    columna: int
    estado: str
