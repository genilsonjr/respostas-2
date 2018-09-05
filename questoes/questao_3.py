## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    Pi= 3.14 #valor de pi.
    r= int(input('Coloque o valor do raio: '))# pedindo para que o usuario coloque o valor do raio da circunferencia.
    area= Pi * r **2 #calculo da area do circulo.
    diametro= 2 * r #calculo do diametro da circunferencia.
    comprimento= 2 * Pi * r #calculo do comprimento da circunferencia.
    print('Meu amigo a area do seu circulo é', area,'o diametro da sua circunferencia é', diametro,'e o comprimento é', comprimento)#impressao do valor 


    
if __name__ == '__main__':
    main()
