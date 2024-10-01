import random
import os



def titulo():
    os.system('cls')
    print('==================================')
    print('===========PAR OU IMPAR===========')
    print('==================================')
    print('')
    

def menu():
    print('[1] JOGAR')
    print('[2] VER REGRAS')
    print()
    resp = int(input('Digite a opção desejada: '))
    if resp == 1:
        jogar()
    if resp == 2:
        print('-'*30)
        print('Cada vitória concede 1 ponto')
        print('Cada derrota remove 1 ponto')
        print('Quantos pontos você consegue fazer?')
        print('-'*30)
        print()
        input('Aperte qualquer tecla para jogar ')
        jogar()


def jogar():
    os.system('cls')
    titulo()
    numero_jogador = int(input('Qual número quer jogar? '))
    palpite_jogador = str(input('PAR ou ÍMPAR? [P/I] ')).upper().strip()
    while palpite_jogador not in 'PI':
        print('Digite "P" para par ou "I" para ímpar!')
        palpite_jogador = str(input('PAR ou ÍMPAR? [P/I] ')).upper().strip()
    numero_computador = random.randint(1,10)
    soma = numero_computador + numero_jogador
    
    
    if soma % 2 == 0:
        print(f'Você jogou {numero_jogador} e o computador jogou {numero_computador}. Total de {soma}. DEU PAR!')
        if palpite_jogador == 'P':
            print('VOCÊ GANHOU!')
            somar_pontos()
        else:
            print(f'VOCÊ PERDEU!')
            remover_pontos()
            
    else:
        print(f'Você jogou {numero_jogador} e o computador jogou {numero_computador}. Total de {soma}. DEU ÍMPAR!')
        if palpite_jogador == 'I':
            print('VOCÊ GANHOU!')
            somar_pontos()
        else:
            print(f'VOCÊ PERDEU!')
            remover_pontos()
    jogar_novamente()

pontos = 0
def somar_pontos():
    global pontos
    pontos += 1

def remover_pontos():
    global pontos
    pontos -= 1

def jogar_novamente():
    print('-'*30)
    resp = str(input('Deseja jogar novamente? [S/N] ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Deseja jogar novamente? [S/N] ')).upper().strip()
    if resp == 'S':
        titulo()
        jogar()
    else:
        os.system('cls')
        titulo()
        print('FIM DE JOGO!'.center(30))
        print(f'VOCÊ FEZ {pontos} PONTOS!'.center(30))
        print('-'*30)