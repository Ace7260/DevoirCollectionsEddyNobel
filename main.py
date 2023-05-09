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
