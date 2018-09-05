## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

def main():
    km= int(input('Quantos qulimetros voce percorreu: '))#pedir que o usuario coloque a quantidade de km pecorridos.
    dias=int(input('Quantos dias voce utilizou o carro: '))#pedir a o usuario a quantidade de dias com o carro.
    resu1= 60 * dias#calculo dos dias 
    resu2= 0.15 * km#calculo dos quilometros
    resutado= resu1 + resu2# a soma dos dois resutados
    print(' O valor a ser pago é R$', resutado)# impressao do valor que o usuario irar pagar.




    
if __name__ == '__main__':
    main()
