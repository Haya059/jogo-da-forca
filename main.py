import random

def definir_palavra():
    palavras_possiveis = ['python', 'hayashida', 'programar', 'computador']
    return random.choice(palavras_possiveis)

def exibir_palavra(palavra, acertos):
    exibicao = ''
    for letra in palavra:
        if letra in acertos:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def jogo_da_forca():
    palavra = definir_palavra()
    tentativas = 6
    acertos = set()
    erros = set()

    while tentativas > 0 and set(palavra) != acertos:
        print(f'\nPalavra: {exibir_palavra(palavra, acertos)}')
        print(f'Tentativas restantes: {tentativas}')
        print(f'Erros: {', '.join(erros)}')

        tentativa = input('Digite uma letra: ').lower()
        if tentativa in acertos or tentativa in erros:
            print('Você já tentou essa letra')
        elif tentativa in palavra:
            acertos.add(tentativa)
        else:
            erros.add(tentativa)
            tentativas -= 1

    if set(palavra) == acertos:
        print(f'Parabéns! Você acertou a palavra: {palavra}')
    else:
        print(f'Você perdeu! A palavra certa era: {palavra}')

jogo_da_forca()