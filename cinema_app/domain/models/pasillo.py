from dataclasses import dataclass


@dataclass
class Pasillo:
    id: int
    sala_id: int
    columna_izq: int
    columna_der: int
