suma=0
preg=raw_input ("Tiene Datos para Ingresar (SI o NO):")
while preg=="SI":
    sueldo=int(raw_input("Ingrese Sueldo:"))
    suma=suma+sueldo
    preg=raw_input("Tiene Datos para Ingresar (SI o NO):")
print "El Total Es:",suma,"pesos"


