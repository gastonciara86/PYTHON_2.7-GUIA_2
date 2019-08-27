c=0
preg="si"
name0=" "
while preg=="si":
    name=raw_input("Ingrese Nombre:")
    sexo=raw_input("Sexo (m o f):")
    if sexo=="f":
        c=c+1
        name0=name0+name+" "
    preg=raw_input("Tiene mas datos?(si o no):")
print "Total de Mujeres:",c,"Nombres:",name0