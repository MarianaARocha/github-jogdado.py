from datetime import date
maioridade = 0
menoridade = 0
ano = date.today().year

for c in range(7):
    pergunta = int(input("Digite o ano de seu nascimento: "))
    idade = ano - pergunta
    if idade >= 18:
        maioridade += 1
    else:
        menoridade = 7 - c
print("{} pessoas são maiores de idade e {} pessoas são menores de idade.".format(maioridade, menoridade))
