from random import randint

# Génération d'un nombre aléatoire compris entre 1 et 100
nombre_a_deviner = randint(1, 100)

# Définition du nombre d'essais
nombre_essais = range(5)

# Le jeu commence...
for i in nombre_essais:
    
    essai = input('Entrez un nombre (essai {0}): '.format(i + 1))

    if essai < nombre_a_deviner:
        print('Le nombre a deviner est plus grand que {0}'.format(essai))
    elif essai > nombre_a_deviner:
        print('Le nombre a deviner est plus petit que {0}'.format(essai))
    elif essai == nombre_a_deviner:
        print('Bravo, vous avez gagne en {0} essai(s)'.format(i + 1))
        break

# Le joueur n'a pas trouvé le nombre à deviner...
if essai != nombre_a_deviner:
    print('Vous avez perdu')
    print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu.')