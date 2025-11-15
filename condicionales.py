print("PROGRAMA DE EVALUACION DE NOTAS")
nota_alumno=int(input("Ingrese un valor: "))

def evaluación (nota):
    valoracion = "Aprobado"
    if nota<5: 
        valoracion="Reprobado" #La variable *Valoracion* solo está disponible dentro del ambito, es decir que no se puede acceder fuera del concional IF que sería su ambito 
    return valoracion
#si quiero acceder a la variable valoración no podré acceder porque está fuera de su ambito (IF)
print(evaluación(nota_alumno))