from gestion_proyectos.equipos.equipo import Equipo
from gestion_proyectos.proyectos.proyecto import Proyecto
from gestion_proyectos.tareas.tarea import Tarea

def main():
    # Creacion de equipos
    # id, nombre, objetivo, jefe
    equipo1 = Equipo("1", "EQUIPO1", "Desarrolladores Font end","PEPE")
    equipo2 = Equipo("2", "EQUIPO2", "Desarrolladores Backend","JUAN")
    
    # Creacion de proyectos
    # id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin , id_equipo
    proyecto1 = Proyecto("1", "PROYECTO1", "DESC PROYECTO1","2023-01-01", "2024-03-30","1" ) 
    proyecto2 = Proyecto("2", "PROYECTO2", "DESC PROYECTO2","2023-01-01", "2024-03-30","2" ) 

    # crear tareas
    # nombre, descripcion, fecha_limite, id_proyecto
    tarea1 = Tarea("TAR1","DESC TAREA 1", "2024-01-10","2024-04-08","1")
    tarea2 = Tarea("TAR2","DESC TAREA 2", "2024-01-10","2024-04-08","2")

    # Mostrar detalles de las transacciones
    print("\n****************************************")
    
    print("Proyectos del Equipo 1:")
    print("\n****************EQUIPO1***********************")
    print(equipo1)
    print("\n****************PROYECTO1***********************")
    print(proyecto1)
    print("\n****************TAREA1***********************")
    print("Tarea:", tarea1)

    print("\n****************************************")

    print("\nProyectos del Equipo 2:")
    print("\n****************EQUIPO2***********************")
    print(equipo2)
    print("\n****************PROYECTO2***********************")
    print(proyecto2)
    print("\n****************TAREA2***********************")
    print("Tarea:", tarea2)

if __name__ == "__main__":
    main()