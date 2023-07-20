alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alpha_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x',
              'y', 'z']


def dechiffrer(word: str, key: str):
    count = 0
    new_word = []
    for i in word:
        if word.index(i) != len(word):
            if count > len(key) - 1:
                count = 0
            if i in alpha:
                z = (alpha.index(i) - alpha.index(key[count])) % 26
                char = alpha[z]
            elif i in alpha_min:
                z = (alpha_min.index(i) - alpha_min.index(key[count])) % 26
                char = alpha_min[z]
            else:
                char = i
            new_word.append(char)
        count += 1
    return ''.join(new_word)


def chiffrer(word: str, key: str):
    count = 0
    new_word = []
    for i in word:
        if word.index(i) != len(word):
            if count > len(key) - 1:
                count = 0
            if i in alpha and key[count] in alpha:
                y = (alpha.index(i) +
                 alpha.index(key[count])) % 26
                char = alpha[y] 
            elif i in alpha_min and key[count] in alpha_min:
                y = (alpha_min.index(i) +
                 alpha_min.index(key[count])) % 26
                char = alpha_min[y]
            else: 
                char = i
            new_word.append(char)
        count += 1
    word_crypted = ''.join(new_word)
    return word_crypted


def ask() -> int:
    print("Menu\n\t1) Chiffrer du texte\n\t2) Déchiffrer du texte\n")
    option = int(input(">>>"))
    return option


def ecrire(file_name: str, new_line: str):
    with open(f"(Version chiffré)_{file_name}", "a") as file:
        file.write(''.join(new_line))


def lecture(url: str, key: str, action: int):
    file = open(url, "r")
    file_name = file.name.split("\\")
    with file as f:
        line = f.read()
        word_in_line = line.split(' ')
        new_line = []
        for i in word_in_line:
            if action == 1:
                new_line.append(chiffrer(i, key))
            elif action == 2:
                new_line.append(dechiffrer(i, key))
        ecrire(file_name[-1], " ".join([str(i) for i in new_line]))

def run():
    choice = ask()
    while choice != 0:
        url = str(input("Entrez l'url du fichier : "))
        key = str(input("Entrez la clé : "))
        lecture(url, key, choice)
        choice = ask()
   