
### DEFINIÇÃO

def print_hi(name):
    print(f'Oi, {name}') # a partir do Python 3


#como fazia no python antes da versão 3
def exibir_dia_da_semana_if(numero):
    if numero == 1:
        print('O dia é segunda')
    elif numero == 2:
        print('O dia é terça')
    elif numero == 3:
        print('O dia é quarta')
    elif numero == 4:
        print('O dia é quinta')
    elif numero == 5:
        print('O dia é sexta')
    elif numero == 6:
        print('O dia é sábado')
    elif numero == 7:
        print('O dia é domingo')
    else:
        print('Número do dia inválido. Digite de 1 a 7')



### EXECUÇÃO DE SCRIPT

#print do nome helloworld
print_hi('Karol')

#exemplo de dia da semana com if - elif (else if) - else
exibir_dia_da_semana_if(0)