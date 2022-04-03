import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("você errou, há {} chances".format(erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("jogando . . .")

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

#FUNÇÕES
#IMPRIME MENSAGEM DE BOAS VINDAS
def imprime_mensagem_abertura():
    print("__________________________________ \n")
    print("    Bem vindo ao jogo de forca \n")
    print("         Fruits Version \n")
    print("__________________________________ \n")
    print("Será que você consegue acertar a palavra secreta?")

#CARREGA O ARQUIVO CONTENDO AS PALAVRAS SECRETAS
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

#SUBSTITUI AS LETRAS POR UNDERLINE
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

#ENTRADA DE LETRA PELO USUÁRIO
def pede_chute():
    chute = input("Digite uma letra:  ")
    chute = chute.strip().upper()
    return chute

#ACERTOS DO USUÁRIO
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

#DESENHOS DE ERRO NA FORCA
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


#IMPRIME MENSAGEM DE VENCEDOR
def imprime_mensagem_vencedor():
        print("__________________________________ \n")
        print("      Parabéns! Você venceu.")
        print("__________________________________ \n")

#IMPRIME MENSAGEM DE PERDEDOR
def imprime_mensagem_perdedor(palavra_secreta):
        print("__________________________________ \n")
        print("     Que pena :( você perdeu.")
        print("  A palavra secreta era ", palavra_secreta)
        print("__________________________________ \n")

if(__name__ == "__main__"):
    jogar()
