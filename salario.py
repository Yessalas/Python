salario = float(input("Digite o seu salarío atual e tecle enter para saber o seu reajuste: "))

if salario <= 280:
    aumento = 0.20
    reajuste = salario * aumento
    atual= salario + reajuste
    print (f"O valor do seu salario atual é {salario}, e você teve um percentual de aumento aplicado {aumento}, e o valor do aumento foi {reajuste}, e seu salario atual é {atual}")


elif salario <= 700:
    aumento = 0.15
    reajuste = salario * aumento
    atual= salario + reajuste
    print (f"O valor do seu salario atual é {salario}, e você teve um percentual de aumento aplicado {aumento}, e o valor do aumento foi {reajuste}, e seu salario atual é {atual}")


elif salario <= 1500 :
    aumento = 0.1
    reajuste = salario * aumento
    atual= salario + reajuste
    print (f"O valor do seu salario atual é {salario}, e você teve um percentual de aumento aplicado {aumento}, e o valor do aumento foi {reajuste}, e seu salario atual é {atual}")

else :
    aumento = 0.05
    reajuste = salario * aumento
    atual= salario + reajuste
    print (f"O valor do seu salario atual é {salario}, e você teve um percentual de aumento aplicado {aumento}, e o valor do aumento foi {reajuste}, e seu salario atual é {atual}")
