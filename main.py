import funciones as fn

while True:
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación: ")

    if opcion == '5':
        print("calculadora cerrada.")
        break

    num1 = int(input("Ingrese el primer número: "))
    num2 = int (input("Ingrese el segundo número: "))

    if opcion == '1':
        print("El resultado de la suma es:", fn.suma(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es:", fn.resta(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es:", fn.multiplicacion( num1, num2))
    elif opcion == '4':
        print("El resultado de la división es:", fn.division(num1, num2))
    else:
        print("Opción no válida, seleccione otra opcion.")

#////////////////////////////////////////////////////////////////////////////////////////

list1 = [1,5,9,8,2,65,45,78,95,32,111,55,8,-5]
lista_ordenada= fn.ordenar_de_menor(list1)
print("lista ordenada",lista_ordenada)
print("lista original",list1)

#//////////////////////////////////////////////////////////////////////////////////////

list2 = [51,18,89,65,4,2,3,5,96,85,74,14,25,36,32,65,98,87,45,12]
list2_ord = fn.ordenar_de_mayor(list2)
print("lista ordenada",list2_ord)
print("lista original",list2)

#/////////////////////////////////////////////////////////////////////////////////////////
list3 = ["Bruno","Joaquin","Martin","Gonzalo","Franco","Matias","Quimy","Marti"]
list3_ord = fn.ordenar_a(list3)
print("lista ordenada",list3_ord)
print("lista original",list3)
