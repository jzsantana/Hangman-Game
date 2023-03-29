import random
from threading import Timer
import os


# Função para o jogador inserir uma nova palavra no jogo
def inserir():
    p = input('Digite uma nova palavra para o jogo: ')
    palavras.append(p)
    print(palavras)
    dica = input('Agora, digite uma dica para esta palavra: ')
    dicas.append(dica)
    print('-------------------------------------')
    print(dicas)


# Função para o usuário remover uma palavra e uma dica
def remover_palavra():
    palavra_removida = input('Digite a palavra que você deseja remover: ')
    if palavra_removida in palavras:
        index = palavras.index(palavra_removida)
        dica_removida = dicas[index]
        palavras.remove(palavra_removida)
        dicas.pop(index)
        print(f'A palavra removida foi {palavra_removida} e a dica removida foi {dica_removida}')


# Função para inserir palavras e dicas no modo café com leite
def modo_inserir():
    print('------------------ MENU -------------------')
    print('-> INSERIR NOVA PALAVRA E DICA      [ 1 ] <-')
    print('-> REMOVER PALAVRA E DICA           [ 2 ] <-')
    print('-> JOGAR                            [ 3 ] <-')
    print('-> SAIR DO JOGO                     [ 4 ] <-')

    menu = int(input('------- DIGITE UMA DAS OPÇÕES ACIMA: -------\n'))

    match menu:
        case 1:
            inserir()
        case 2:
            remover_palavra()
        case 3:
            print('SEU JOGO IRÁ COMEÇAR!')
        case 4:
            print('QUE PENA, VOCÊ SAIU DO JOGO! ATÉ A PROXIMA!')
            quit()


# Função de tempo
def tempo(texto="Que pena, seu tempo esgotou!"):
    print(f'Fim de jogo -- {texto}')
    pid = os.getpid()
    os.kill(pid, 0)


print('\n->->->->->->-> O JOGO COMEÇOU <-<-<-<-<-<-<-\n')
print('   BEM VINDO(A) AO CLÁSSICO JOGO DA FORCA\n')


palavras = ['artista', 'amor', 'pescador', 'livro', 'cadeira',
            'banana', 'internet', 'morango', 'bailarina', 'cadeado',
            'biscoito', 'pacote', 'shampoo', 'mercado'
            ]

dicas = ['aquele que cultiva as belas-artes', 'Forte afeição por outra pessoa', 'Profissão daquele que pesca',
         'Coleção de folhas de papel', 'Peça de mobília', 'Fruta amarela', 'Rede de conexões globais', 'Fruta vermelha',
         'Profissional de dança especifica', 'Fechadura portátil', 'Alimento assado no forno em pequenas porções',
         'Pequeno embrulho', 'Espécie de sabonete com fórmula específica para o cabelo', 'Local onde se compram coisas'
         ]

palavra_sorteada = random.choice(palavras).upper()


def nutella():
    vidas = 6
    letras_digitadas = []
    letras_atual = ['_'] * len(palavra_sorteada)

    while vidas != 0:

        letra = input('Digite uma letra: ').upper()
        letras_digitadas.append(letra)

        if letra in palavra_sorteada:
            print('VOCÊ ACERTOU UMA LETRA!')
            for item in range(len(palavra_sorteada)):
                if letra == palavra_sorteada[item]:
                    letras_atual[item] = letra

        else:
            print('ihh, você errou!')
            vidas -= 1
            if vidas == 5:
                palavra_index = palavras.index(palavra_sorteada.lower())
                dica = dicas[palavra_index]
                print(f'Aqui vai uma dica:\n {dica}')
            elif vidas == 2:
                palavra_index = palavras.index(palavra_sorteada.lower())
                dica = dicas[palavra_index]
                print(f'Aqui vai uma dica:\n {dica}')
        if '_' not in letras_atual:
            print('PARABÉNS, VOCÊ GANHOU!')
            break

        print(' '.join(letras_atual))

        print('Tentativas: ', letras_digitadas)


def cafecomleite():

    modo_inserir()

    vidas = 6
    letras_digitadas = []
    letras_atual = ['_'] * len(palavra_sorteada)

    while vidas != 0:
        temporizador = Timer(30, tempo)
        temporizador.start()
        letra = input('Digite uma letra: ').upper()
        letras_digitadas.append(letra)

        if letra in palavra_sorteada:
            print('VOCÊ ACERTOU UMA LETRA!')
            for item in range(len(palavra_sorteada)):
                if letra == palavra_sorteada[item]:
                    letras_atual[item] = letra

        else:
            print('Ihh, você errou!')
            vidas -= 1
            if vidas == 4:
                palavra_index = palavras.index(palavra_sorteada.lower())
                dica = dicas[palavra_index]
                print('Aqui vai uma dica: ')
                print(dica)
        if '_' not in letras_atual:
            print('PARABÉNS, VOCÊ GANHOU!')
            break

        print(' '.join(letras_atual))
        print('Tentativas: ', letras_digitadas)

        if temporizador == 0:
            print('FIM DE JOGO')
            quit()
        elif vidas == 0:
            temporizador.cancel()
            print('Ihhh, suas vidas acabaram. Perdeu fracote!')
            quit()


def raiz():
    vidas = 6
    letras_digitadas = []
    letras_atual = ['_'] * len(palavra_sorteada)

    print('SEJA BEM VINDO(A) AO MODO RAIZ')
    while vidas != 0:
        temporizador = Timer(10, tempo)
        temporizador.start()
        letra = input('Digite uma letra: ').upper()
        letras_digitadas.append(letra)

        if letra in palavra_sorteada:
            print('VOCÊ ACERTOU UMA LETRA!')
            for item in range(len(palavra_sorteada)):
                if letra == palavra_sorteada[item]:
                    letras_atual[item] = letra

        else:
            print('Ihh, você errou!')
            vidas -= 1
            if vidas == 1:
                palavra_index = palavras.index(palavra_sorteada.lower())
                dica = dicas[palavra_index]
                print('Aqui vai uma dica: ')
                print(dica)
        if '_' not in letras_atual:
            print('PARABÉNS, VOCÊ GANHOU!')
            break

        print(' '.join(letras_atual))
        print('Tentativas: ', letras_digitadas)

        if temporizador == 0:
            print('FIM DE JOGO')
            quit()
        elif vidas == 0:
            temporizador.cancel()
            print('Ihhh, suas vidas acabaram. Perdeu fracote!')
            quit()


print('>------------- MODOS DE JOGO --------------<')
print('->                NUTELLA                 <-')
print('->                 CAFÉ                   <-')
print('->                 RAIZ                   <-')
print('->             SAIR DO JOGO               <-')
print('>------------------------------------------<\n')


modo = input('ESCOLHA UM DOS MODOS DE JOGO ACIMA: \n').upper()

match modo:
    case "NUTELLA":
        nutella()

    case "CAFÉ":
        cafecomleite()

    case "RAIZ":
        raiz()

    case "SAIR":
        print('QUE PENA, VOCÊ CLICOU EM SAIR DO JOGO! ATÉ A PROXIMA!')

