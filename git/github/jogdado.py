import random
from time import sleep

print("Olá jogador! Já vamos começar em:")

print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)


pergunta = str(input("voce quer jogar o dado? Digite SIM ou NAO\n")).strip().lower()
sleep(1)

for c in range(3):
    print("processando...")
    sleep(1)

if pergunta == "sim":
    print("o numero sorteado foi", random.randint(1, 6))
    while pergunta == "sim":
        sleep(1)
        pergunta = str(input("voce quer jogar o dado novamente?\n")).strip().lower()
        if pergunta == "sim":
            for c in range(3):
                print("processando...")
                sleep(1)
            print("o numero sorteado foi", random.randint(1, 6))

    while pergunta != "nao" and "sim":
        print("Resposta inválida! Tente novamente utilizando somente SIM ou NAO.")
        sleep(1)
        pergunta = str(input("Você quer jogar o dado?\n")).strip().lower()
        if pergunta == "sim":
            for c in range(3):
                print("processando...")
                sleep(1)
            print("O número sorteado foi", random.randint(1, 6))
            while pergunta == "sim":
                sleep(1)
                pergunta = str(input("Você quer jogar o dado novamente?\n")).strip().lower()
                if pergunta == "sim":
                    for c in range(3):
                        print("processando...")
                        sleep(1)
                    print("O número sorteado foi", random.randint(1, 6))

while pergunta != "nao" and "sim":  # irá rodar caso seja teclado o espaço ou enter
    print("Resposta inválida! tente novamente utilizando somente SIM ou NAO.")
    pergunta = str(input("Você quer jogar o dado?: \n")).strip().lower()
    if pergunta == "sim":
        for c in range(3):
            print("processando...")
            sleep(1)
        print("O numero sorteado foi", random.randint(1, 6))
        while pergunta == "sim":
            pergunta = str(input("Você quer jogar o dado novamente?: \n")).strip().lower()
            if pergunta == "sim":
                for c in range(3):
                    print("processando...")
                    sleep(1)
                print("O número sorteado foi", random.randint(1, 6))

else:
    for c in range(3):
        print("processando...")
        sleep(1)
    print("\nBeleza, ate mais entao!!")
 
