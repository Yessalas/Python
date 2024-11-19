num1 = int(input("Digite um númro e tecle enter: "))
num2 = int(input("Digite outro número e tecle enter: "))
num3 = int(input("Digite mais um outro número: "))

if(num2 > num1 and num2 > num3):
    print(f"Maior número é {num2} ")
elif(num3 > num1 and num3 > num2):
    print(f"Maior número é {num3} ")
else:
    print(f"Maior número é {num1}")