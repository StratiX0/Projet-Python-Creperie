import collections
import sys
from liste_crepe import * # import liste_crepe

def menu():
    """
    Fonction permettant au client de choisir l'affichage des crêpes
    Affiche les éléments redirigeant vers d'autres menus
    """
    print("\n-------------------------------")
    print("|  Bienvenue dans la Crêp'ite!  |" )
    print("--------------------------------\n")
    for i, element in enumerate(lstListCrepe): # parcourt les éléments de la liste
        print(f"{i+1} - {element}") # affiche les éléments de la liste avec i+1 place
    affichage() #retourne vers la fonction affichage
    

def choix():
    """
    Fonction recueuillant la réponse de l'utilisateur pour la sélection du menu
    Returns:
        Renvoie la valeur de 'reponse'
    """
    while True: #boucle la fonction si 'reponse' ne répond pas aux exigences
        try:
            reponse = int(input("\nQu'aimeriez-vous ? ")) #input de l'utilisateur
            if reponse >= 1 and reponse <= 6: #teste la valeur de 'reponse' si elle vaut entre 1 et 6
                return reponse #retourne la valeur reponse
            else: # la valeur de 'reponse" n'est pas égale à un nombre entre 1 et 6
                raise ValueError # si reponse n'est pas un nombre entre 1 et 6, il renvoie une erreur
        except ValueError: #renvoie une erreur sous forme de print, cela n'arrête donc pas le programme
            print("\nEntrez un nombre entier entre 1 et 6 compris.") # Renvoie une erreur si l'utilisateur ne renvoie pas la valeur attendue

def retour():
    """
    Fonction recueuillant la réponse de l'utilisateur à la fin d'une réponse
    Returns:
        Renvoie l'utilisateur vers le menu principal 'menu()' ou le fait quitter le programme en fonction de son choix
    """
    while True: #boucle la fonction si 'reponseMenu' ne répond pas aux exigences
            try:
                reponseMenu = int(input("\nQue voulez-vous faire ? : 1 - Retour au menu   2 - Quitter : ")) #input de l'utilisateur
                if reponseMenu == 1: #teste si 'reponseMenu' est égal à 1
                    menu() # redirige l'utilisateur vers le menu principal 'menu()'
                if reponseMenu == 2: #teste si 'reponseMenu' est égal à 2
                    print("\nVous avez quitté le programme.\nA bientôt dans la Crêp'ite!\n") #phrase indiquant à l'utilisateur qu'il a quitté le programme
                    sys.exit() #quitte le programme
                else: #la valeur de 'reponseMenu' n'est pas égale à un nombre entre 1 et 6
                    raise ValueError #si 'reponseMenu' n'est pas égal à 1 ou 2, il renvoie une erreur
            except ValueError: #renvoie une erreur sous forme de print, cela n'arrête donc pas le programme
                print("\nEntrez 1 ou 2.")


def personnalise():
    """
    Fonction permettant à l'utilisateur de créé sa propre crêpe
    """
    choixClient=[] #créé la liste 'choixClient' vide
    prixTotal = 4.5 #prixTotal variable du prix total contenant déjà le prix d'une crêpe nature
    ingredients = "" #chaîne de caractère regroupant tout les ingrédients choisis par l'utilisateur
    print("Vous pouvez sélectionner jusqu'à 5 éléments.") #indique le nombre maximal d'éléments sélectionnables par l'utilisateur
    print("La liste des ingrédients : ")
    print("Tapez 0 pour quitter.") #indique comment quitter la boucle
    for i in range (len(lstIngredients)): #parcourt la longueur de la liste 'lstIngredients'
        print(f"{i+1} - {lstIngredients[i][0]} - {lstIngredients[i][1]}€") #affiche le i+1 ème place de l'ingrédient, l'ingrédient et son prix
    while True: #boucle la fonction tant que l'utilisateur n'a pas 5 ingrédients ou n'a pas décidé d'arrêter d'ajouter des ingrédients
        try:
            if len(choixClient) == 5: #teste si la longueur de la liste de ingrédients choisis est égale à 5 = la limite
                print("Vous avez atteints la quantité maximale d'ingrédients dans votre crêpe.\n")
                break #quitte la boucle
            reponse = int(input("\nQu'est ce que vous aimeriez ? "))
            if reponse == 0: #teste si la longueur de la liste de ingrédients choisis est égale à 0
                break #quitte la boucle
            if reponse >= 0 and reponse <= len(lstIngredients): #si la réponse de l'utilisateur ne fait pas partie des exceptions au dessus et fait partie de liste des ingrédients, ajoute sa réponse à la liste des ingrédients sélectionnés
                choixClient.append(lstIngredients[reponse-1]) #ajoute 'reponse' à la liste 'lstIngredients'
            else:
                raise ValueError #si 'reponse' ne correspond pas aux cas au dessus, il renvoie une erreur
        except ValueError: #renvoie une erreur sous forme de print, cela n'arrête donc pas le programme
            print("\nEntrez un nombre entier compris dans la liste.")
    if reponse == 0: #teste si 'reponse' est égal à 0
        print("\nVous avez quitté la personnalisation de votre crêpe.\n")
    for j in range(len(choixClient)): #parcourt la longueur de la liste 'choixClient'
        prixTotal = prixTotal + choixClient[j][1] #ajoute le prix de l'ingrédient dans 'choixClient' à la variable 'prixTotal'
        ingredients = ingredients + "\n-" + choixClient[j][0] #ajoute le nom de l'ingrédient dans 'choixClient' à la variable 'ingredients'
    print(f"Votre crêpe contient :{ingredients}\n")
    print(f"Le montant de votre crêpe : {prixTotal}€\n")
    with open('crepe_perso', 'w', encoding='utf-8') as f: #créé un fichier texte nommé 'crepe_perso'
        f.write(str(choixClient)) #écrit lz contenu de la liste 'choixClient' sous forme de string dans le fichier crepe_perso


def prixCroissant():
    """
    Fonction créant une liste global basé sur la liste 'lstCrepe' mais triée par ordre alphabétique
    Returns:
        lstCrepeCroissant(list) -> liste triée de 'lstCrepe'
    """
    global lstCrepeCroissant #rend la variable 'lstCrepeCroissant' globale dans tout le programme
    lstCrepeCroissant = lstCrepe #copie tout les éléments de 'lstCrepe' dans 'lstCrepeCroissant'
    l = len(lstCrepeCroissant) # attribue à la variable 'l' la longueur de la liste 'lstCrepeCroissant'
    for i in range(0, l): #parcourt tout ce qu'il y a entre 0 et la longueur 'l' de 'lstCrepeCroissant'
        for j in range(0, l-i-1): #parcourt tout ce qu'il y a entre 0 et la longueur 'l' moins la valeur de 'i' moins 1
            if (lstCrepeCroissant[j][1] > lstCrepeCroissant[j + 1][1]): #teste si l'élément 'lstCrepeCroissant[j][1]' est supérieur à l'élément de 'lstCrepeCroissant[j + 1][1]'
                temp = lstCrepeCroissant[j] #créé une variable temporaire avec la valeur de 'lstCrepeCroissant[j]'
                lstCrepeCroissant[j]= lstCrepeCroissant[j + 1] #'lstCrepeCroissant[j]' prend la valeur de 'lstCrepeCroissant[j + 1]'
                lstCrepeCroissant[j + 1]= temp #'lstCrepeCroissant[j + 1]' prend la valeur de 'temp'
    return lstCrepeCroissant #renvoie la variable 'lstCrepeCroissant'

def affichage():
    """
    Fonction affichant le choix de l'utilisateur dans le menu

    """
    affiche = choix() #prend la valeur retournée par la fonction choix()
    if affiche == 1: #teste si la valeur de affiche vaut 1
        for i in range(len(lstCrepe)): # parcourt les éléments de la liste
            print(f"\n{i+1} - {lstCrepe[i][0]} - {lstCrepe[i][1]}€ - {lstCrepe[i][2]} \n{lstCrepe[i][3]}\n") #affiche toutes les crêpes dans l'ordre alphabétique, les crêpes sont déjà triée depuis leur fichier
        retour() #recueuille la réponse de l'utilisateur après avoir afficher les crêpes
    if affiche == 2: #teste si la valeur de affiche vaut 2
        prixCroissant() #lance la fonction 'prixCroissant'
        for i in range(len(lstCrepeCroissant)): # parcourt la longueur de la liste 'lstCrepeCroissant'
            print(f"\n{i+1} - {lstCrepe[i][0]} - {lstCrepe[i][1]}€ - {lstCrepe[i][2]} \n{lstCrepe[i][3]}\n") #affiche toutes les crêpes par leur prix dans l'ordre ascendant
        retour() #recueuille la réponse de l'utilisateur après avoir afficher les crêpes
    if affiche == 3: #teste si la valeur de affiche vaut 3
        prixCroissant() #lance la fonction 'prixCroissant'
        print(f"La crêpe la plus chère est : {lstCrepeCroissant[-1][0]} - {lstCrepeCroissant[-1][1]}€ - {lstCrepeCroissant[-1][2]} \n{lstCrepeCroissant[-1][3]}\n") #affiche la crêpe la plus chère de la liste triée 'lstCrepeCroissant'
        retour() #recueuille la réponse de l'utilisateur après avoir afficher la crêpe
    if affiche == 4: #teste si la valeur de affiche vaut 4
        prixCroissant() #lance la fonction 'prixCroissant'
        print(f"La crêpe la moins chère est : {lstCrepeCroissant[0][0]} - {lstCrepeCroissant[0][1]}€ - {lstCrepeCroissant[0][2]} \n{lstCrepeCroissant[0][3]}\n") #affiche la crêpe la moins chère de la liste triée 'lstCrepeCroissant'
        retour() #recueuille la réponse de l'utilisateur après avoir afficher la crêpe
    if affiche == 5: #teste si la valeur de affiche vaut 5
        personnalise() #lance la fonction 'personnalise()'
        retour() #recueuille la réponse de l'utilisateur après avoir afficher la crêpe personnalisée
    if affiche == 6: #teste si la valeur de affiche vaut 6
        print("\nVous avez quitté le programme.\nA bientôt dans la Crêp'ite!\n") #phrase indiquant à l'utilisateur qu'il a quitté le programme
        sys.exit() #quitte le programme


menu() #lance le menu au lancement du programme