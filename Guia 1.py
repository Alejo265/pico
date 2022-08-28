
numero = "" 
baseActual = 0 
base10 = 0
a=[] 


print("Ingresa el número a convertir ")
numero = input() 
print("Ingresa la base actual")
baseActual = int(input()) 



tam = len(numero) 


for k in range(len(numero)): 
   a.append(numero[k]) 


cont = tam - 1 

temporal = 0
for i in range(tam):
    temporal = int(a[i]) * pow(baseActual, cont) 
    cont = cont - 1
    base10 = base10 + temporal 


  
Menu=int(input("Menu:\n 1- convetir a binario \n 2- Convertir a octal\n 3- convertir a decimal \n 4- convertir a hexagecimal \n 5-salir \n"))
numero1 = base10
while Menu !=5:
   if Menu == 1:
    print(bin(numero1))
    break
   elif Menu== 2:
    print(oct(numero1))
    break
   elif Menu==3:
    print(base10)
    break
   elif Menu== 4:
    print(hex(numero1))
    break
bin(base10)
b=chr(base10) 
print ("En codigo Ascii corresponde a:"+b)
    