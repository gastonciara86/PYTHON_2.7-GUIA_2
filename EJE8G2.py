c=0
cars=raw_input("Ingrese auto:")
precio=int(raw_input("Precio:"))
while precio<1000000 :
    cars=raw_input("Ingrese auto:")
    precio=int(raw_input("Precio:"))
    if precio in range (95000,125000):
        c=c+1
print "Cantidad de autos entre $95mil y $125mil son:",c
