from Estudiante import estudiante
from Lista import lista_enlazada

    
e1=estudiante(202010245,"Esteban Valdez",20,"siquinala",54645138,"esteban@gmail.com","ingenieria en sistemas","programador jr")
e2=estudiante(202010254,"Cristan Oxlaj",20,"masagua",546454486,"@gmail.com","ingenieria en sistemas","programador jr")
e3=estudiante(202010033,"Jose Rodolfo",20,"santa rosa",5467826486,"rodolfo@gmail.com","ingenieria en sistemas","programador jr") 


lista_e=lista_enlazada()
lista_e.insertar(e1)
lista_e.insertar(e2)
lista_e.insertar(e3)


lista_e.recorrer()
lista_e.generar_graphviz("Lista Estudiantes.dot")



# lista_e.eliminar(202010245)
# lista_e.eliminar(202010033)
# lista_e.recorrer()