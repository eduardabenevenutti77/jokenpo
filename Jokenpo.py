#crie um programa para jogar jokenpo com vc
from random import randint
print('\n\t Vamos jogar Jokênpo!')

Opcao = ['Pedra','Papel','Tesoura']
computador = randint(0,2)

Jogar = str(input('\n Deseja Jogar? => ')).upper()

if Jogar=='S' or Jogar=='SIM':
    print('''\n Escolha entre: 
    [0] Pedra
    [1] Papel
    [2] Tesoura''')

    UsuarioOpcao = int(input('\n Escolha a sua jogada => '))

    print('----------------------------------------------------------------')
    print(' O computador jogou {}'.format(Opcao[computador]))
    print(' O jogador jogou {}'.format(Opcao[UsuarioOpcao]))
    print('----------------------------------------------------------------')
    if computador==0: #pedra
        if UsuarioOpcao==0:
            print('\n Empate')
        elif UsuarioOpcao==1:
            print('\n O Jogador venceu')
        elif UsuarioOpcao==2:
            print('\n O Computador venceu')
        else:
            print('\n Jogada Inválida')

    elif computador==1: #papel
        if UsuarioOpcao==0:
            print('\n O Computador venceu')
        elif UsuarioOpcao==1:
            print('\n Empate')
        elif UsuarioOpcao==2:
            print('\n O Jogador venceu')
        else:
            print('\n Jogada Inválida')

    elif computador==2: #tesoura
        if UsuarioOpcao==0:
            print('\n O jogador venceu')
        elif UsuarioOpcao==1:
            print('\n O computador venceu')
        elif UsuarioOpcao==2:
            print('\n Empate')
        else:
            print('\n Jogada Inválida')

else:
    print('\n Que pena, nós veremos novamente na próxima vez!')
