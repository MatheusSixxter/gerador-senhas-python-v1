import string
from random import choice
caixa_letras_maiusculas = string.ascii_uppercase
caixa_letras_minusculas = string.ascii_lowercase
caixa_numeros = string.digits
caixa_simbolos = string.punctuation


print("-=" * 20)
print(" GERADOR DE SENHAS ".center(40))
print("-=" * 20)

while True:
    print(">> Como quer a senha ?")
    print("-" * 25)

    v_maiuscula = " "
    while not v_maiuscula in "SN":
        v_maiuscula = str(input("Quer letra maiúscula ? [S/N] ")).strip().upper()
        if v_maiuscula not in "SN":
            print("> Letra inválida. Tente S ou N.")

    v_minuscula = " "
    while not v_minuscula in "SN":
        v_minuscula = str(input("Quer letra minúscula ? [S/N] ")).strip().upper()
        if v_minuscula not in "SN":
            print("> Letra inválida. Tente S ou N.")

    v_numeros = " "
    while not v_numeros in "SN":
        v_numeros = str(input("Quer números ? [S/N] ")).strip().upper()
        if v_numeros not in "SN":
            print("> Letra inválida. Tente S ou N.")

    v_simbolos = " "
    while not v_simbolos in "SN":
        v_simbolos = str(input("Quer símbolos ? [S/N] ")).strip().upper()
        if v_simbolos not in "SN":
            print("> Letra inválida. Tente S ou N.")

    caixa_final = ""
    if v_maiuscula == "S":
        caixa_final += caixa_letras_maiusculas
    if v_minuscula == "S":
        caixa_final += caixa_letras_minusculas
    if v_numeros == "S":
        caixa_final += caixa_numeros
    if v_simbolos == "S":
        caixa_final += caixa_simbolos

    if not caixa_final:
        print("\n> Comando Inválido. Escolha pelo menos uma opção com 'S'.")
        print("-" * 25)
        continue

    tamanho = ""
    while not tamanho.isdigit():
        print("-" * 25)
        tamanho = str(input(">> Por favor, insira o tamanho de sua senha. (apenas números): "))
        if not tamanho.isdigit():
            print(">> Escreva apenas números, por favor.")
    tamanho = int(tamanho)

    senha = ""
    for c in range(tamanho):
        senha += choice(caixa_final)

    print(f".Sua senha gerada foi: {senha}")

    repetir = " "
    while not repetir in "SN":
        repetir = str(input(".Gostaria de gerar outra senha ? [S/N] ")).strip().upper()
        if repetir not in "SN":
            print("> Comando inválido. Tente S ou N.")

    print("-" * 25)
    if repetir == "N":
        print("> Programa encerrado.")
        break
