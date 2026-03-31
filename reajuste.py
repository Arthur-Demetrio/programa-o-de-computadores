salario = float(input("qual o valor do salário?"))
percent = int(input("qual o percentual de reajuste?"))
novo_salario = salario*(1+(percent/100))
print("o novo salario é R$", novo_salario)