#programa para ensamblar tu propia malteada y que te dice el precio 



print("tipo de vaso?")
print("para chico 65$ 1, para mediano 75$ 2 para grande 95$ 3")

vaso=input()

if (vaso == "1"):
    precio = 65
    
elif(vaso == "2"):
    precio = 75
    
elif(vaso == "3"):
    precio = 95
    


print("selecciona tu sabor")
print(" fresa 5$ 1, vainilla 5$ 2, chocolate 5$ 3, oreo 15$ 4, ferrero 25$ 5")

sabor=input()

if(sabor == "1"):
    precio = precio + 5
    
elif(sabor == "2"):
    precio = precio + 5

elif(sabor == "3"):
    precio = precio + 5

elif(sabor == "4"):
    precio = precio + 15

elif(sabor == "5"):
    precio = precio + 25



print(precio)