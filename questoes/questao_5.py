## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    cigarros= int(input(' Quantos cigarros voce fuma por dia: '))#a quantidade de cigarros que o usuario fuma por dias.
    anos=int(input('Quantos anos voce ja fumou: '))#pedindo que o usuario informe quantos anos e ja fomou.
    totalciga= (anos * 365)*cigarros#calculo dos cigarros fumados em todos os anos.
    fumados= (totalciga * 10)/24#e o acrecimo pra saber quanto tempo de vida o usuario perdeu.
    print('Dias perdidos', fumados)#impressao dos dias perdidos.


    


    
if __name__ == '__main__':
    main()
