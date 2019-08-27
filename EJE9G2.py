max=-30000000
r="si"
while r=="si" :
    valor = float (raw_input("Ingrese Valor:"))
    if valor>max :
        max=valor
    r=raw_input("Hay mas datos:")
print max, "el mayor es:"