valor_conta = float(input("qual o valor da conta?"))
qtd_pessoas = int(input("são quantas pessoas?"))
valor_indv = valor_conta/qtd_pessoas
print("cada pessoa deve pagar:", "{:.2f}".format(valor_indv))
