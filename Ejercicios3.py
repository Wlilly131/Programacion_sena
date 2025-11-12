"""
Nivel Básico 1  7

1. Declaración simple: Crea tres variables (nombre, edad, altura) y asígnales valores adecuados.
Imprime sus valores.

2. Identificar tipo: Declara variables de tipo entero, flotante, cadena y booleano. Usa type() para
mostrar su tipo.
3. Concatenación: Declara dos variables de texto con tu nombre y apellido. Combínalas en una
sola variable e imprímela.
4. Operaciones numéricas: Declara dos variables numéricas y muestra la suma, resta,
multiplicación y división.
5. Booleanos: Crea dos variables booleanas y usa operadores
"""

print("------------------ejercicio 1------------------")

nombre = "William" #VARIABLE TIPO TEXTO "STR"
edad = 24 #VARIABLE TIPO ENTERO "INT", NUMERO SIN DECIMALES
altura = 1.75 #vARIABLE TIPO FLOTANTE "FLOAT", NUMERO CON DECIMALES
print("Mi nombre es:",nombre, "Tengo ", edad, "años de edad","y mido", altura,"m")

print("------------------ejercicio 2------------------")

entero = 5 #VARIABLE TIPO ENTERO "INT"
flotante = 6.9 #VARIABLE TIPO FLOTANTE "FLOAR"
cadena = "William Ricardo" #VARIABLE TIPO TEXTO "STR"
viernes = True #VARIABLE TIPO BOOLEANO
sabado  = False #VARIABLE TIPO BOOLEANO
print("El numero",entero,"es un entero y su tipo es:", type(entero))
print("El numero",flotante,"es un flotante y su tipo es:", type(flotante))
print("La cadena de texto es:",cadena,"y su tipo es:", type(cadena))
print("¿ El dia de hoy es viernes ?:", viernes,"y su tipo es:", type(viernes))
print("¿ El dia de hoy es viernes ?:", sabado, "y su tipo es:", type(sabado))

print("------------------ejercicio 3------------------")

nombre_1 = "William"
apellido = "Sierra"
nombre_completo = nombre_1+" "+apellido
print("Mi nombre es: "+nombre_completo)

print("------------------ejercicio 4------------------")

x = 10
y = 3
suma = x+y
resta = x-y
multiplicacion = x*y
division = x/y
print("La suma de X + Y es igual a:",suma)
print("La resta de X + Y es igual a:", resta)
print("La multiplicaion de X + Y es igual a:",multiplicacion)
print("La division de X + Y es igual a:", float(division),"Y con decimales es:",int(division))

print("------------------ejercicio 5------------------")

mayor_edad = True
licencia_conduccion = False
print("AND: ", mayor_edad and licencia_conduccion)
print("OR: ", mayor_edad or licencia_conduccion)
print("NOT: ",not mayor_edad)



    print("Selccione un número de 1 a 5")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. División")
    print("5. Salir")
    opcion = input("Digite un número del 1 al 5 según la opción que se quiera ejecutar: ")
    return(opcion)
    if opcion >=1:
        valor_1 = input("Ingrese el primer valor a sumar: ")
        valor_2 = input("Ingrese el segundo valor a sumar: ")
    return(valor_1)
calculadora()