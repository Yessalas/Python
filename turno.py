nome = input("Digite o seu nome e tecle enter:")
turno = input("Digite o turno que voçê estuda, M-matituno, V-vesperino, N-noturno: ")
if (turno == 'M' or turno == 'm'):
        print(f"Bom Diaa, {nome} ! ")
    
elif (turno == 'V' or turno == 'v'):
        print (f"Boa Tarde, {nome} !")
elif (turno == 'N' or turno == 'n'):
        print (f"Boa Noite, {nome} !")
    
else:
        print ("Turno invalido !")
    