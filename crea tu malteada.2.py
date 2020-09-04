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
    
    
    
print("algun extra para su maltiada c/u 5$")
print("para añadir una extra precione 1 y despues el numero del producto")
print("chispas de chocolate 1, leche de almendras 2, leche de coco 3, chochos de colores 4")


quiero= input()
extra=input()

while(quiero == "1"):
    if(extra == "1"):
        precio = precio + 5
    if(extra == "2"):
        precio = precio + 5
    if(extra == "3"):
        precio = precio + 5
    if(extra == "4"):
        precio = precio + 5
    print("algun otro sabor")
    quiero= input()
    extra=input()

print(precio)