print("PROGRAMA DE EVALUACION DE NOTAS")
nota_alumno=int(input("Ingrese un valor: "))

def evaluación (nota):
    valoracion = "Aprobado"
    if nota<5:
        valoracion="Reprobado"
    return valoracion

print(evaluación(nota_alumno))