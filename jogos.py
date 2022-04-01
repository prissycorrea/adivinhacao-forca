import forca
import adivinhacao


def escolhe_jogo():
    print("__________________________________ \n")
    print("             Jogos")
    print("__________________________________ \n")

    print("[1] Forca     [2] Adivinhação")

    jogo = int(input("O que vamos jogar?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("Opção inválida.")


if(__name__ == "__main__"):
    escolhe_jogo()
