###partie1

##exo 1 et 2

import string

def nettoyage(message):

    #message = input("saisissez votre texte : \n")
    new_message = message.lower()#transforme les minuscles en majuscule
    special = [",",";","!","?",".","$","*","%"," ",":","/","%","^",")","(","@","&","#"] #liste des caractere a supprimer

    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']

    for i in range(len(special)):
        new_message = new_message.replace(special[i],"")#supprimer les element qui se trouve dans la liste special

    for j in range(len(accent)):
        new_message = new_message.replace(accent[j],sans_accent[j])

    print(new_message)



###exo3

def crypt(m,k):

    if m.isupper() or k.isupper():
        print('entrez une lettre en minuscule')
    else:
        x = ord(m.lower())-97
        y = ord(k.lower())-97
        # chiffrement
        chiffre = (x+y) % 26
        l = chr(chiffre+97)
        return l

####exo 4

def crypt_txt():

    txt = input("saisissez votre texte : \n")
    key = input("saisissez votre texte : \n")
    nettoyage(txt)
    nettoyage(key)

    message_code = ""
    for i,c in enumerate(txt) :
        d = key[ i % len(key) ]
        d = ord(d) - 97
        message_code += chr((ord(c)-97+d)%26+97)
    return message_code

######exo5

def decrypt_txt():

    txt = input("saisissez votre texte : \n")
    key = input("saisissez votre texte : \n")
    nettoyage(txt)
    nettoyage(key)

    message_code = ""
    for i,c in enumerate(txt) :
        d = key[ i % len(key) ]
        d = ord(d) - 97
        message_code += chr((ord(c)-97-d)%26+97)
    return message_code


###PARTIE2:

####exo6

def key(txt):

    nettoyage(txt)#enelve les espace et les caractere speciaux

    compteur = 0

    n = len(txt)

    for i in range(len(txt)):

        for j in range(i+4,n):

            if (txt[i:i+3] == txt[j:j+3]):

                compteur = compteur + 1

        print(txt[i:i+3])
        print(compteur)



