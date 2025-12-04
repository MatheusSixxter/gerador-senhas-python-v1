# 🔐 Gerador de Senhas em Python — Versão 1 (Sem listas e sem dicionários)

Este projeto é um **Gerador de Senhas interativo**, desenvolvido em Python, que permite ao usuário personalizar a composição da senha de acordo com suas preferências.  
Nesta **primeira versão**, o código foi construído **sem o uso de listas ou dicionários**, utilizando apenas variáveis simples, blocos condicionais e loops. Isso torna o projeto ideal para quem está começando a praticar lógica de programação.

---

## 🧠 Sobre o Projeto

O programa pergunta ao usuário quais tipos de caracteres ele deseja incluir na senha:

- Letras **maiúsculas**
- Letras **minúsculas**
- **Números**
- **Símbolos**

Com base nessas escolhas, o programa monta uma “caixa final” contendo apenas os caracteres permitidos.  
Depois, o usuário informa o **tamanho da senha**, e o programa gera uma string aleatória com essa configuração.

Todos os inputs são **validados**, garantindo que o usuário informe apenas comandos válidos e apenas números no tamanho da senha.

---

## 📌 Funcionalidades

- Menu interativo e claro.
- Escolha personalizada de:
  - Maiúsculas
  - Minúsculas
  - Números
  - Símbolos
- Tratamento completo de erros:
  - Evita letras quando o usuário deve digitar números.
  - Evita respostas inválidas (somente S/N).
  - Impede continuar se nenhuma categoria de caracteres for escolhida.
- Geração aleatória da senha usando `random.choice()`.
- Possibilidade de gerar quantas senhas o usuário quiser.

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- Módulos:
  - `string`
  - `random`

---

## 📄 Código Completo

```python
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
```

---

## 📘 Observação Importante

Esta é uma **primeira versão**, focada em lógica básica.  
Não usa **listas**, não usa **dicionários**, e não usa técnicas mais avançadas de Python.  

O código é totalmente sequencial e trabalha apenas com strings concatenadas e fluxos simples de controle.

Futuramente, você pode evoluir para versões:

- Com listas para facilitar combinações.
- Com dicionários para automatizar categorias.
- Com funções separadas.
- Com interface gráfica.
- Com recursos de obrigatoriedade (ex: garantir 1 letra maiúscula).

---

## ✔ Conclusão

Este projeto marca os primeiros passos no aprendizado de Python, lógica de programação e boas práticas como:

- validação de entrada
- modularidade mental
- clareza do código
- montagem dinâmica de dados

Acredito que seja um ótimo trabalho em construir isso desde a base! 🚀  


