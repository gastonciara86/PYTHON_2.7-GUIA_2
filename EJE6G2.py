suma=0
preg=int(raw_input("Cuantas Personas Desea Cargar:"))
for x in range (preg):
    name=raw_input("Ingrese Nombre:")
    age=int(raw_input("Edad:"))
    suma=suma+age
    promedio=suma/preg
print "El promedio de edades es:",promedio
