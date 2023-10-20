#Construa um programa que calcule: Qual deve ser o bônus de um funcionário?
#Se ele vendeu mais de 1.000 unidades, o bônus tem que ser de R$250,
#caso contrário, o bônus tem que ser R$50.

#Declarando a constante vendas_funcionario recebendo o valor de 1.000  OBS: As constantes não podem ter valores mudados.
vendas_funcionario = 1.000
#Declarando a variável meta recebendo o valor de 1.000
meta = 1000
#Declarando a constante bonus_acima recebendo o valor de 250
bonus_acima = 250
#Declarando a constante bonus_abaixo recebendo o valor de 50
bonus_abaixo = 50

#Se vendas do funcionário for maior que a meta
if vendas_funcionario > meta:
#O Funcionário vai receber o bônus de 250
	bonus_funcionario = bonus_acima
else:  #Caso contrário
#O funcionário vai receber o bônus de 50
	bonus_funcionario = bonus_abaixo
#Exibindo o valor do bônus do Funcionário
print(f'O Bônus do Funcionário vai ser: R$ {bonus_funcionario}')

