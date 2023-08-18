# jeux du juste prix
from random import choice
print("Hello cher utilisateur,nous allons jouer au jeux du juste prix\nCe jeux consiste à trouver un nombre choisi au hasard entre 1 et 1000")
hidden_number=int(input("Commençons,entrez un nombre entre 1 et 1000: "))
nombre_essais=1
chosen_number=choice(list(range(1,1001)))
while hidden_number!=chosen_number and nombre_essais<7:
    if hidden_number<chosen_number:
        hidden_number=int(input("la valeur saisie est inférieur au nombre recherché,veuillez réessayer: "))
    else:
        hidden_number=int(input("la valeur saisie est supérieur au nombre recherché,veuillez réessayer: "))
    nombre_essais+=1
if nombre_essais==7 and hidden_number<chosen_number:
    print("la dernière valeur saisie est inférieure au nombre recherché")
else:
    print("la dernière valeur saisie est supérieure au nombre recherché")
print(f"vous avez déja écoulé {nombre_essais} tentatives")
answer=input("voulez vous un indice? ")
if answer.lower()=="oui":
    if(chosen_number%2==0):
        print("en réalité le nombre à trouver est pair")
    else:
        print("en réalité le nombre à trouver est impair")
    hidden_number=int(input("maintenant veuillez réesayer à nouveau: "))
else:
    hidden_number=int(input("Tant pis,veuillez continuer alors: "))
while hidden_number!=chosen_number:
            if hidden_number<chosen_number:
                hidden_number=int(input("la valeur saisie est inférieur au nombre recherché,veuillez réessayer: "))
            else:
                hidden_number=int(input("la valeur saisie est supérieur au nombre recherché,veuillez réessayer: "))
            nombre_essais+=1
if nombre_essais==1:
    print("Bravo,félicitations vous avez trouvé du premier coup")
elif nombre_essais>7:
    print("Bravo,félicitations,vous avez finallement trouvé le juste prix à la {}e tentative".format(nombre_essais+1))
else:
    print("Bravo,félicitations,vous avez trouvé le juste prix à la {}e tentative".format(nombre_essais+1))