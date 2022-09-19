from .. import application
from . import implementation
from ..domain import models


if __name__ == "__main__":
    try:
        branch_id = input("Introduzca el identificador del local: ")
        branch_id = int(branch_id)
        local_rep = implementation.LocalSQLRepository()
        get_branch_use_case = application.GetBranch(local_rep)
        branch = get_branch_use_case.run(branch_id)
        print(f"Local {branch.id} encontrado")

        room_id = input("\nIntroduzca el identificador de la sala: ")
        room_id = int(room_id)
        room_obj = models.sala.Sala(room_id, branch.id)
        sala_rep = implementation.SalaSQLRepository()
        get_room_use_case = application.GetRoom(sala_rep)
        room = get_room_use_case.run(room_obj)
        print(f"Sala {room.id} en Local {room.local_id} encontrada")

        seat_info = input("\nIntroduzca la posición de la silla (ejemplo -> a1): ")
        seat_obj = models.silla.Silla(0, room.id, seat_info[0], int(seat_info[1]), "")
        silla_rep = implementation.SillaSQLRepository()
        get_seat_use_case = application.GetSeat(silla_rep)
        seat = get_seat_use_case.run(seat_obj)
        print(f"Silla {seat.fila}{seat.columna} en Sala {seat.sala_id} encontrada")

        num_seats = input("\nIntroduzca el número de sillas contiguas a buscar: ")
        get_adjacent_seats_use_case = application.GetCloseSeats(silla_rep)
        seats = get_adjacent_seats_use_case.run(seat, int(num_seats))

        print("\nResultado: ")
        if len(seats) == 0:
            print("No se encontraron sillas disponibles con las características solicitadas")
        else:
            for idx, arrange in enumerate(seats):
                opt_arr = [s.fila + str(s.columna) for s in arrange]
                print(f"Opción {idx + 1}: ", opt_arr)

    except Exception as e:
        print("Ocurrió un error: ", str(e))