print("Olá! Este programa faz qualquer operação básica entre dois números!")
print("\n-------------------------------------------------------------------\n")

#Entrada da operação desejada

print("Primeiro, insira a operação desejada com a primeira letra em maiúsculo\n(Soma, Subtração, Divisão e Multiplicação)")
op = str(input("\n-------------------------------------------------------------------\n"))

#Entrada do primeiro número

print("Agora, insira o primeiro número do cálculo")
pri = float(input("\n----------------------------------------\n"))

#Entrada do segundo número

print("Por fim, insira o segundo número do cálculo")
sec = float(input("\n-----------------------------------------\n"))

#Verificação de operação. Caso seja soma, some o primeiro número com o segundo

if(op=="Soma"):
    print("O resultado é:",pri+sec)

#Verificação de operação. Caso seja subtração, subtraia o segundo número do primeiro

elif(op=="Subtração"):
    print("O resultado é:",pri-sec)

#Verificação de operação. Caso seja divisão, divida o primeiro número pelo segundo

elif(op=="Divisão"):
    print("O resultado é:",pri/sec)

#Verificação de operação. Caso seja multiplicação, multiplique o primeiro número pelo segundo

elif(op=="Multiplicação"):
    print("O resultado é:",pri*sec)

#Verificação de operação. Se nenhuma operação válida for encontrada, mostre mensagem de erro

elif(op!="Soma"or"Subtração"or"Divisão"or"Multiplicação"):
     print("Operação Inválida!\nVerifique a escrita e tente novamente")

#Verificação de operação. Caso nenhuma das verificações se aplique, mostre mensagem de erro

else:
    print("ERRO\nVerifique as informações e tente novamente")