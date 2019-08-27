datos=raw_input ("hay datos para ingresar:")
while datos=="si" :
    N=raw_input ("Ingrese Nro:")
    N=int(N)
    if N>0 :
        print N, "Es positivo"
    else:
        print N, "Es negativo"
    datos=raw_input ("hay datos para ingresar:")
print "fin"