carreras: tuple[str, ...] = ("Ingeniería de Software", "Contabilidad", "Derecho")



personas: list[tuple[str, str, int, int]] = ["Omar","de jesus","19 años", "0", "Elier ", "poueriet","5 años", "2", "Margot", "De Espiritusanto", "17 años", "1", "Felix", "Garcia", "28 años","1" "Elizabeth", "de Poueriet" ,"38 años","2",
    # nombre, apellido, edad, carrera
]
 
estudiantes: list[dict[str, str | int]] = [
    {"nombre": "Omar", "apellido": "de jesus", "edad": 19, "carrera": Ingenieria de Software},
    {"nombre": "Elizabeth", "apellido": "de Poueriet", "edad": 38, "carrera": Derecho},
    {"nombre": "Margot", "apellido": "De Espiritusanto", "edad": 17, "carrera": Contabilidad},
    {"nombre": "Elier", "apellido": "Poueriet", "edad": 5, "carrera": Derecho},
    {"nombre": "Felix", "apellido": "Garcia", "edad": 28, "carrera": Contabilidad}
]
for _ in range(5):
    # Solicita los datos aquí
    print
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} {estudiante['apellido']} tiene {estudiante['edad']} años y estudia {estudiante['carrera']}")