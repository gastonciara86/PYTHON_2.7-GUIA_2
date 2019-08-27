menor= 100000
r="si"
while r=="si" :
    nombre=raw_input ("Ingrese Nombre:")
    sueldo=float (raw_input ("ingrese Sueldo:"))
    if sueldo<menor :
        menor=sueldo
        pobre=nombre
    r=raw_input ("Hay mas datos:")
print "el sueldo mas bajo es de",pobre,"=",menor