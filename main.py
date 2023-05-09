if __name__ == '__main__':
    # Question I
    # Creation d'une liste de 10 elements de type chaîne de caractères
    animaux = ["chat", "chien", "souris", "oiseau", "poisson", "cheval", "vache", "mouton", "cochon", "lapin"]
    
    # 1- Affichage des elements de la liste
    print("1) Affichage des elements de la liste")
    print("--------------------------------------------------")
    print(animaux)
    print("--------------------------------------------------\n")
    
    # 2- Changer le contenu de l'element numero 5
    print("2) Changement du contenu de l'element numero 5")
    print("--------------------------------------------------")
    animaux[4] = "requin"
    print(animaux)
   
    #3- Creation d' une nouvelle liste
    nouvelle_liste = []
    # remplissage avec les elements de la liste precedente contenant la lettre "a"
    for element in animaux:
        if "a" in element:
            nouvelle_liste.append(element)
    print("\n3) les elements de la liste contenant la letter a:")
    print("--------------------------------------------------")
    print(nouvelle_liste)
    
    #4 Ajout d'un element a la fin de la liste
    print("\n4) Ajout d'un element a la fin de la liste")
    print("--------------------------------------------------")
    animaux.append("tortue")
    print(animaux)
    
    # #5 Ajout d'un element a l'index numero 2
    print("\n5) Ajout d'un element a l'index numero 2")
    print("--------------------------------------------------")
    animaux.insert(2, "serpent")
    print(animaux)

    # #6 Suppression de l'element numero 3
    print("\n6) Suppression de l'element numero 3")
    print("--------------------------------------------------")
    animaux.remove("souris")
    print(animaux)
    
    # #7. Suppression l'element a l'index numero 2
    print("\n7) Suppression de l'element a l'index numero 2")
    print("--------------------------------------------------")
    del animaux[2]
    print(animaux)
    
    # #8 Ordonner la liste
    print("\n8) Ordonnancement de la liste")
    print("--------------------------------------------------")
    animaux.sort()
    print(animaux)
 
    # #9 Afficher le sens au sens inverse
    print("\n9) Affichage dans le sens inverse")
    print("--------------------------------------------------")
    animaux.reverse()
    print(animaux)
    
    # #10 Vider la liste
    print("\n10) Vidange de la liste")
    print("--------------------------------------------------")
    animaux.clear()
    print(animaux)
    
    # #11 Suppression de la liste
    del animaux

    # Question 2
    print("==========Question 2============")
    # Creation d' une tuple de 10 elements de type entier
    chiffre = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    # Affichage des elements de la tuple chiffre
    print("\nAffichage des elements de la tuple")
    print("--------------------------------------------------")
    print(chiffre)
    
    #1) Affichage du nombre de fois que valeur 3 apparait dans la tuple chiffre
    print("\n1) Affichage du nombre de fois que valeur 3 apparait dans la tuple")
    print("--------------------------------------------------")
    print(chiffre.count(3))

    #2) Affichage du contenu de l'element numero 5
    print("\n2) Affichage du contenu de l'element numero 5")
    print("--------------------------------------------------")
    print(chiffre[4])
    
    #3) Ordonnancement du tuple
    print("\n3) Ordonnancement du tuple")
    print("--------------------------------------------------")
    chiffre = tuple(sorted(chiffre))
    print(chiffre)
    
    #4) Ajout d' un element a la fin de la tuple
    print("\n4) Ajout d' un element a la fin de la tuple")
    print("--------------------------------------------------")
    # On ne peut pas modifier une tuple directement, il faut creer une nouvelle tuple
    liste = list(chiffre)
    # Ajouter un element a la fin de la liste
    liste.append(4)
    # Reconvertir la liste en tuple
    chiffre = tuple(liste)
    # Affichage du nouveau tuple 
    print(chiffre) 
    
    #5) Ajouter un element a l'index numero 3
    print("\n5) Ajouter un element a l'index numero 3")
    print("--------------------------------------------------")
    # On ne peut pas modifier une tuple directement, il faut creer une nouvelle tuple
    chiffre = chiffre[:3] + (12,) + chiffre[3:]
    print(chiffre)

    #6) Affichage de la nouvelle tuple
    print("\n6) Affichage de la nouvelle tuple")
    print("--------------------------------------------------")
    print(chiffre)
  
    # Question 3
    print("==========Question 3============")
    # Creation d'un set de 10 elements de type chaine de caractères
    salutation = {"Bonjour", "Hello", "Hola", "Salut", "Hi", "Ciao", "Ola", "Aloha", "Namaste", "Salam"}
