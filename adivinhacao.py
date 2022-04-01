from random import random

import random

def jogar():
    print("__________________________________ \n")
    print("Bem vindo no jogo de Adivinhação. \n")
    print("__________________________________ \n")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Em qual nível de dificuldade voce quer jogar?")
    print("[1] Fácil  |   [2] Médio   |   [3] Difícil")

    nivel= int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #string interpolation ("Tentativa {1} de {0}".format(rodada, total_de_tentativas)) faria imprimir ao contrário
        chute = int(input("Digite o seu número entre 1 e 100: "))
        print("\nVocê digitou:",chute, "\n")

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(rodada > total_de_tentativas):
            print("Suas tentativas acabaram. O número secreto era ", numero_secreto)
        elif(acertou):
            print("Você acertou! Total de pontos: {} \n".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou!!! \n \nSeu chute foi maior que o número secreto \n")
            elif(menor):
                print("Voce errou!!! \n \nSeu chute foi menor que o número secreto \n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("__________________________________ \n")
    print("          Fim de jogo.")
    print("__________________________________ \n")

if(__name__ == "__main__"):
    jogar()

#for rodada in [1, 2, 3, 4, 5] - vai contar 1, 2, 3, 4 e 5
#for rodada range [1,10,2] - começa em 1, vai até 10 e conta de 2 em 2