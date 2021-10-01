todo_list = ["Hacer la cama", "Barrer el patio", "Comer menos azucar"]

#podemos eliminar elementos de listas con el metodo remove()
#todo_list.remove("Hacer la cama")
#print(todo_list)
#Podemos eliminar elementos por su indice con el metodo pop(indice)
#todo_list.pop(1)
#print(todo_list)
#si llamamos al metodo pop() sin argumento. se eliminan el ultimo elemento

todo_list.pop()

print(todo_list)

#tambien tenemos el metodo especial "del",metodo especial no tan frecuente

del todo_list
print(todo_list)

todo_list = ["Hacer la cama", "Barrer el patio", "Comer menos azucar"]
 todo_list.clear()