todo_list = ["Sacar la basura","Barrer la entrada","Pasear al boby","Regar las plantas"]
#para agregar elementos usamos la funcion insert () que viene
#en todas las listas.el primer parametro es el indice que ocupara el nuevo elemento
todo_list.insert(2, "Dejar la cocacola")

print(todo_list)

#mezclar listas
movies = ["Matrix", "Star Wars", "El viejo de las argollas"]
books = ["Poemas de Baldor", "Chistes de Proschle, Horoscopo Xino"]
#el metodo extend incorpora al arreglo lo que esta extendiendo
movies.extend(books)

print(movies)
print(books)
