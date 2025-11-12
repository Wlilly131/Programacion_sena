#print("1. Suma de dos números: Pide dos números y muestra su suma.")

#numero_1 = int(input("Ingrese el pimero número que desea sumar: "))
#numero_2 = int(input("Ingrese el pimero segundo que desea sumar: "))
#print("La suma de los numeros es de: ",numero_1+numero_2)

#print("3. Área del triángulo: Calcula el área de un triángulo con base y altura ingresadas por el usuario.")

#base = int(input("Ingrese la base del triangulo: "))
#altura = int(input("Ingrese la altura del triangulo: "))
#print("El area del triangulo es:",((base * altura)/2))

#print("5. Potencia: Calcula xyx^yxy usando el operador **.")

#num1 = int(input("Ingrese el numero al que desea sacar la potencia:"))
#num2 = int(input("Ingrese el numero al que desea elevar el numero:"))
#print("La potencia del numero del numero es: ",num1**num2)

#print("7. Verificar edad: Pide la edad y muestra si la persona es mayor de edad (≥18).")

#edad = int(input("Ingrese su edad: "))
#if edad>=18:
#    print("Usted es mayor de edad")
#else:
#    print("Usted es menor de edad")

#print("9. Comparar cadenas: Pide dos cadenas y verifica si son iguales.")

#cadena_1 = input("Ingrese la cadena que quiere comparar:")
#cadena_2 = input("Ingrese la otra cadena que quiere comparar:")
#if cadena_1==cadena_2:
    #print("Las cadenas son iguales")
#else:
    #print("Las cadenas no son iguales")

#print("11. Acceso permitido: Solicita usuario y contraseña y valida si ambos son correctos usando and.")
#usuario="William131"
#contraseña=1000254610
#acc_user = input("Ingrese su nombre de usuario: ")
#acc_pss = int(input("Ingrese su contraseña de usuario: "))
#if usuario==acc_user and contraseña == acc_pss:
    #print("Correcto")
#else:
    #print("Incorrecto")

#print("13. Verificación múltiple: Pide tres valores booleanos e
# imprime si al menos uno es True (usa or).")
#booleano2 = input("Ingrese un numero de 6 a 10: ")
#booleano3 = input("Ingrese un numero de 11 a 15: ")

edad = 18
estudiante = False
adulto = True
def ingreso():
    edad_1 = int(input("Ingrese su edad"))
    if edad_1 >= 18 or estudiante == False or adulto == True:
        print("Puede pasar")
    else:
        print("No puede ingresar")
    ingreso

# def loquesea():
#     booleano1 = (input("Ingrese un numero de 1 a 5: "))
#     if booleano1 in range(1,5+1):
#         return True
#     else:
#         return False
    
# def loquesea2():
#     booleano2 = int(input("Ingrese un numero de 6 a 10: "))
#     if booleano2 in range(6,10+1):
#         return True
#     else:
#         return False
# def loquesea3():
#     booleano3 = int(input("Ingrese un numero de 11 a 15: "))
#     if booleano3 in range(11,15+1):
#         return True
#     else:
#         return False
# def prueba():
#     if loquesea()+loquesea2() >= 1 :
#         return True
#     else:
#         return False
# def prueba2():
#     if prueba()+loquesea3() >=1:
#         return True
#     else:
#         return False
# print(prueba2)