#funciones calculadora
import funciones as fn 

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero."

#funcion de lista ordena 
def ordenar_de_menor(list1): 
 stop= True
list1_ord=[]
list_temp=list1.copy()
while stop:
  val_max=list_temp[0]
  for i in range(len(list_temp)):
     x=list_temp[i]

     if (x>val_max):
       val_max=x 

  list1_ord.append(val_max)
  list_temp.remove(val_max)
  if len(list_temp)==0:
     stop= False

 # demayor a menor 
def ordenar_de_mayor(list2):
    stop = True
    list2_ord=[]
    list_temp=list2.copy()
    while stop:
        val_min=list_temp[0]
        for i in range(len(list_temp)):
            x=list_temp[i]

            if (x<val_min):
                val_min=x

        list2_ord.append(val_min)
        list_temp.remove(val_min)
        if len(list_temp)==0:
            stop= False
    return  list2_ord
        
# orden alfabetico
def ordenar_a (list3):
 stop = True
 list3_ord=[]
 list_temp=list3.copy()
 while stop:
  val_alto=list_temp[0]
  for i in range(len(list_temp)):
     x=list_temp[i]

     if (x<val_alto):
       val_alto=x

  list3_ord.append(val_alto)
  list_temp.remove(val_alto)
  if len(list_temp)==0:
     stop= False