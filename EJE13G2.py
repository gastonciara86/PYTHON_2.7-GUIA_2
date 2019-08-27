totalLL=0
sinLL=0
for x in range(7):
    p=raw_input("LLovio?:si o no:")
    if p=="no":
        sinLL=sinLL+1
    else:
        mm=int(raw_input("Cuanto LLovio?:"))
        totalLL=totalLL+mm
print "No llovio:",sinLL
print "Total de lluvia:", totalLL
