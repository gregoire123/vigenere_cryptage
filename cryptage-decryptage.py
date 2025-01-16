#fonction de decryptage
def decryptage():
    valeurs_clée = list(input("Quelle est la clé à utiliser pour decrypter la phrase? "))
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","è","é","à","ù"]
    def decryption(caractere, index_cle):
        if caractere == ' ':
            return ' '
        if caractere in alphabet:
            password = alphabet.index(valeurs_clée[index_cle % len(valeurs_clée)])
            output = (alphabet.index(caractere) - password) % 30
            return alphabet[output]
        else:
            return caractere
    
    output = input("sous quelle forme desirez vous l'output? [file/phrase]")
    entrée = input("que voulez vous decrypyter? [file/phrase] : ")
    if entrée == "file" :
        file = input("quel est le nom du fichier texte à crypter? ")
        fichier = open(file,'r')
        phrase = fichier.read()
        fichier.close()
    else :
        phrase = input("Quelle est la phrase à déchiffrer? ")

    lettres_phrase = list(phrase)
    resultat = []
    index_cle = 0
    for lettre in lettres_phrase:
        lettre_decryptee = decryption(lettre, index_cle)
        resultat.append(lettre_decryptee)
        if lettre != ' ':
            index_cle += 1
    if output == "file":
        fichier = open(file,'w')
        resultat = str(''.join(resultat))
        fichier.write(resultat)
        fichier.close()
    else :
        print("Phrase déchiffrée :", ''.join(resultat))
#fonction de cryptage
def encryptage():
    valeurs_clée = list(input("Quelle est la clé à utiliser pour crypter la phrase? "))
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","è","é","à","ù"]
    def cryptage(caractere, index_cle):
        if caractere == ' ':
            return ' '
    
        if caractere in alphabet:
            password = alphabet.index(valeurs_clée[index_cle % len(valeurs_clée)])
        
            output = (alphabet.index(caractere) + password) % 30 
        
            return alphabet[output]
        else:
            return caractere  
    output = input("sous quelle forme desirez vous l'output? [file/phrase]")
    entrée = input("que voulez vous crypyter? [file/phrase] : ")
    if entrée == "file" :
        file = input("quel est le nom du fichier texte à crypter? ")
        fichier = open(file,'r')
        phrase = fichier.read()
        fichier.close()
    else :
        phrase = input("Quelle est la phrase à découper? ")
    lettres_phrase = list(phrase)
    resultat = []
    index_cle = 0  
    for lettre in lettres_phrase:
        lettre_cryptee = cryptage(lettre, index_cle)
        resultat.append(lettre_cryptee)
        if lettre != ' ':
            index_cle += 1  
    if output == "file":
        fichier = open(file,'w')
        resultat = str(''.join(resultat))
        fichier.write(resultat)
        fichier.close()
    else :
        print("Phrase cryptée :", ''.join(resultat))
#debut du script: choix nb cryptage/decryptage; affichage de la bannière
bannière = open("banner.txt",'r')
print(bannière.read())
choice = input("voullez vous crypter ou decrypter? [C/D]")
if choice == "C":
    encryptage()
elif choice == "D":
    decryptage()
#ValueError: si l personne ne choisit pas la valeur C ou D
else:
    raise ValueError("la vous ne pouvez que crypter (C) ou decrypter (D) ")