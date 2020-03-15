import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.split()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero][0]
    palavra_secreta = palavra_secreta.upper()
    print(type(palavra_secreta))
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto (True and True)
    while(True):
        chute = input("Qual a letra?")
        chute = chute.strip().upper();

        print("Jogando........")
        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:

                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra

                index +=1
        else:
            erros +=1

        enforcou = erros == 6

        if(enforcou):
            break


        acertou = "_" not in letras_acertadas

        if(acertou):
            break

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

        print("Você tem mais {} tentativas".format(6-erros))

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
