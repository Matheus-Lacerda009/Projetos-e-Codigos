print("Este programa calculará os zeros e resolverá com o valor escolhido uma função quadrática.")
print("-----------------------------------------------------------------------------------------")

#Entrada do valor de a da função

a = float(input("Digite aqui o valor de A:\n"))
print("-----------------------------------------------------------------------------------------")

#Verificador para checar se a é igual à 0. Se sim, exibir mensagem de erro

if(a==0):
    print("Erro, A não pode ser igual à zero.")
    print("-----------------------------------------------------------------------------------------")

#Entrada do valor de b da função

b = float(input("Digite aqui o valor de B:\n"))
print("-----------------------------------------------------------------------------------------")

#Entrada do valor de c da função

c = float(input("Digite aqui o valor de C:\n"))
print("-----------------------------------------------------------------------------------------")

#Utilizando da fórmula da Bhaskára, iremos calcular o zero1 e zero2

zero1 = (-b+(((b**2)-4*a*c)**0.5))/(a*2)
zero2 = (-b-(((b**2)-4*a*c)**0.5))/(a*2)

#Se as duas variáveis (zero1 e zero2) forem iguais, exiba mensagem mostrando tal fato. Caso o contrário, exiba o valor dos dois separademente.

if(zero1==zero2):
    print("O valor dos dois zeros são iguais, sendo ele:",zero1)
else:
    print("O valor do zero 1 é:",zero1)
    print("-----------------------------------------------------------------------------------------")
    print("O valor do zero 2 é:",zero2)
print("-----------------------------------------------------------------------------------------")

#Entrada do valor x da função

val = float(input("Insira aqui o valor escolhido (x) para a resolução da função:\n"))
print("-----------------------------------------------------------------------------------------")

#Resolução da função com os valores dados anteriormente e o resultado exibido

fun = (a*(val**2))+(b*val)+c
print("O valor de Y/F é de:",fun)