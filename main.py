
def cripitografar_palavra(palavra, indice, chave):
    palavra = [indice[letra] for letra in palavra.lower()]

    cript = []

    for i in range(len(palavra)):
        valor = palavra[i] + chave[i] + i
        cript.append(str(valor))

    return "&".join(cript)


def descriptografar_palavra(cript, indice_invertido, chave):
    numeros = [int(n) for n in cript.split("&")]

    palavra = []

    for i in range(len(numeros)):
        valor = numeros[i] - (chave[i] + i)

        if valor not in indice_invertido:
            raise ValueError(
                f"Valor inválido na posição {i}. Verifique a chave."
            )

        palavra.append(indice_invertido[valor])

    return "".join(palavra)


indices = {
    " ": 99,
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
    "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
    "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
    "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
    "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
    "z": 25,
    "0": 26, "1": 27, "2": 28, "3": 29,
    "4": 30, "5": 31, "6": 32, "7": 33,
    "8": 34, "9": 35
}

indices_invertidos = {
    valor: letra for letra, valor in indices.items()
}

try:
    opcao = input(
        "[1] -> Criptografar\n"
        "[2] -> Descriptografar\n"
        "--> "
    ).strip()

    if opcao not in ("1", "2"):
        raise ValueError("Opção inválida.")

    chave = input("Escreva a chave: ").strip().lower()

    if not chave:
        raise ValueError("A chave não pode estar vazia.")

    if any(letra not in indices for letra in chave):
        raise ValueError("A chave contém caracteres não suportados.")

    if opcao == "1":
        mensagem = input("Escreva a palavra para criptografar: ").lower()

        if any(letra not in indices for letra in mensagem):
            raise ValueError("A mensagem contém caracteres não suportados.")

        tamanho = len(mensagem)

    else:
        mensagem = input("Escreva a mensagem criptografada: ").strip()
        tamanho = len(mensagem.split("&"))
    chave = (chave * ((tamanho // len(chave)) + 1))[:tamanho]
    chave_numerica = [indices[letra] for letra in chave]
    if opcao == "1":
        resultado = cripitografar_palavra(mensagem, indices, chave_numerica)
        print("Mensagem criptografada:", resultado)

    else:
        resultado = descriptografar_palavra(mensagem, indices_invertidos, chave_numerica)
        print("Mensagem descriptografada:", resultado)

except (ValueError, KeyError) as erro:
    print("[ERRO]", erro)