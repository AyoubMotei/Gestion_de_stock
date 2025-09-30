stock = []

def ajouter_produit(nom, quantite, prix):
    stock.append([nom, quantite, prix])

def afficher_stock():
    for produit in stock:
        print(produit)
def get_stock():
    
    return stock
       