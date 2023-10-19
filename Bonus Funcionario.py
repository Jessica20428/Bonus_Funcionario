#Construa um programa que calcule: Qual deve ser o bônus de um funcionário?
#Se ele vendeu mais de 1.000 unidades, o bônus tem que ser de R$250,
#caso contrário, o bônus tem que ser R$50.

vendas_funcionario = 1000
meta = 1000
bonus_acima = 250
bonus_abaixo = 50

if vendas_funcionario > 1000:
	bonus_funcionario = bonus_acima
else:
	bonus_funcionario = bonus_abaixo
print(f'O Bônus do Funcionário vai ser: R$ {bonus_funcionario}')

