from stock import ajouter_produit, afficher_stock, get_stock
from stats import valeur_totale
from visualize import bar_chart
from menu import afficher_menu
stock = get_stock()

while True:
    afficher_menu()
    choix = input("Choix : ")
    if choix == "1":
        nom = input("Nom : ")
        qte = int(input("Quantité : "))
        prix = float(input("Prix : "))
        ajouter_produit(nom, qte, prix)
    elif choix == "2":
        afficher_stock()
    elif choix == "3":
        print("Valeur totale :", valeur_totale(stock))
    elif choix == "4":
        bar_chart(stock)
    elif choix == "5":
        break
    print("Valeur totale :", valeur_totale(get_stock()))