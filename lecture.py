#EJERCISIO DE DECISIONES DE PHYTON

#queremos crear un script que deletree una palabra dada por el usuario, en este caso va a ser “Pollo” con el ciclo for podemos conseguirlo de la siguiente manera:

palabra = "Pollo"

for letra in palabra:
	print(letra)  



   #La variable o iterador letra en cada recorrido lo que hará es moverse por la palabra en cada iteración y tomará cada una de las letras que haya en “pollo”.   


#¿Cómo romper un bucle for?

#A veces no es necesario que el ciclo se cumpla dependiendo de la cantidad de elementos que tenga el dato iterable y para eso podemos establecer que termine según una condición específica, esto se logra a través de la sentencia break.

palabra = "Pollo"

for letra in palabra:
	if letra == "l":
		break 
	print(letra)   

 #Ahora cuando llegue a la primera letra “l” se va a terminar el ciclo.     