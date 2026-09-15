estudiantes = []

for i in range(3):
    notas = []

    print("Estudiante", i + 1)

    for j in range(3):
        nota = float(input("Ingrese la nota: "))
        notas.append(nota)

    estudiantes.append(notas)

print("Notas de los estudiantes:")
print(estudiantes)