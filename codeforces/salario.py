#primeira valor determina o nome do funcionario
#segundo valor determina a quantidade de horas trabalhadas
#terceiro valor determina o valor a ser pago por hora ao funcionario
n= input()
h= int(input())
v= float(input())
p = float(h*v)
print(n)
print("R$","{:.2f}".format(p))

