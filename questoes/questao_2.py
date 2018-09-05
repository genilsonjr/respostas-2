## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    C= int(input('qual e a temperatura em celsius: ')) #pedindo que o usuario coloque o valor de celsius.
    F= C * (9/5) +32 #calculo de conversao de celsius para fahrenheit.
    print('De celsius que e',C,'para fahrenheit e:' ,F) #comando de imprssao da conversao.    
  



if __name__ == '__main__':
    main()
