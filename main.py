# 1. Criamos o dicionário com as gírias (chaves) e significados (valores)
meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    "VDD": "Abreviação da palavra 'verdade'",
    "BISCOITAR": "Postar algo apenas para chamar a atenção",
    "HATER": "Pessoa que está constantemente criticando os outros",
    "VLW": "Abreviação da palavra 'valeu'"
}

# Desafio extra 3: Saudação inicial
print("=== Bem-vindo ao Dicionário de Gírias da Internet! ===")
print("Ajude as gerações passadas a entenderem o que a gente fala.\n")

# Desafio extra 2: Loop para repetir o processo 5 vezes
for i in range(5):
    word = input("Digite uma gíria em LETRAS MAIÚSCULAS para traduzir: ")
    
    # Conferindo se a palavra existe no nosso dicionário
    if word in meme_dict.keys():
        print("Significado: " + meme_dict[word] + "\n")
    else:
        print("Ainda não temos essa gíria... Mas estamos trabalhando nela!\n")

print("Fim das 5 tentativas de pesquisa!")
