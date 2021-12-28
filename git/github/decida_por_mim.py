from time import sleep
lista = [1, 4]
lista2 = [1, 3]
print("Olá, seja bem-vindo. Descubra seu destino final através de suas escolhas!!!")
print("Prepare-se para começar em:")
sleep(3)

print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)

transporte = input("\nEscolha o seu meio de locomoção e digite o número correspondente:""""
[1] Carro
[2] Moto
[3] Cavalo
[4] Bicicleta\n""")

sleep(1)

if transporte == "1":
    print("\nVamos de carro então!!\n")
elif transporte == "2":
    print("\nVamos de moto então!!\n")
elif transporte == "3":
    print("\nVamos de cavalo então!!\n")
elif transporte == "4":
    print("\nVamos de bicicleta então!!\n")
elif transporte != lista:
    while transporte != lista:
        print("Você digitou uma resposta inválida.Tente novamente!")
        transporte = input("Escolha o seu meio de locomoção e digite o número correspondente:""""
[1] Carro
[2] Moto
[3] Cavalo
[4] Bicicleta\n""")

        sleep(1)

        if transporte == "1":
            print("\nVamos de carro então!!\n")
            break
        elif transporte == "2":
            print("\nVamos de moto então!!\n")
            break
        elif transporte == "3":
            print("\nVamos de cavalo então!!\n")
            break
        elif transporte == "4":
            print("\nVamos de bicicleta então!!\n")

sleep(1)

for c in range(3):
    print("processando...")
    sleep(1)

escolha = input("\nEscolha uma das opções e digite o número:""""
[1] Esquerda, esquerda, reto, direita
[2] Direita, esquerda, direita, reto, direita
[3] Reto, reto, direita, direita, reto, esquerda\n""").strip()

sleep(1)

if escolha == "1":
    print("\nSeu destino de hoje é o shopping. Vê se não vai gastar de mais heein!!")
elif escolha == "2":
    print("\nSeu destino de hoje é o museu. Tenha um bom passeio!!")
elif escolha == "3":
    print("\nSeu destino de hoje é o cinema. Vê se escolhe um filme daora!!")
elif escolha != lista2:
    while escolha != lista2:
        escolha = input("Opção inválida!! Escolha uma das opções e digite o número: """"
[1] Esquerda, esquerda, reto, direita
[2] Direita, esquerda, direita, reto, direita
[3] Reto, reto, direita, direita, reto, esquerda\n""").strip()

        sleep(1)

        if escolha == "1":
            print("\nSeu destino de hoje é o shopping. Vê se não vai gastar de mais heein!!")
            break
        elif escolha == "2":
            print("\nSeu destino de hoje é o museu. Tenha um bom passeio!!")
            break
        elif escolha == "3":
            print("\nSeu destino de hoje é o cinema. Vê se escolhe um filme daora!!")
            break
