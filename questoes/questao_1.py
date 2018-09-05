## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario= float(input('Qual e o seu salário atual: ')) # pedir pro usuario por o salari atual.
    porcentagem= float(input('Quantos porcentos de aumento: ')) #pedir a prcentagem do aumento.
    por= (salario * porcentagem)/100 #calculo da porcentagem
    resutado= por + salario # culculo da soma do salario com a porcentagem
    print('O acrecimo foi de', por,'o seu salário vai ser', resutado,) #impressao na tela o resutado.
 

 


    


if __name__ == '__main__':
    main()
