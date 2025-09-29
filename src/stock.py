# src/stock.py
# Fonctions pour gérer le stock
# Chaque produit = [nom (str), quantité (int), prix (float)]

def find_product_index(stock, name):
    """Retourne l’index du produit par son nom (insensible à la casse)."""
    for i, product in enumerate(stock):
        if product[0].lower() == name.lower():
            return i
    return None

def add_product(stock, name, quantity, price):
    """Ajoute un produit ou met à jour s’il existe déjà."""
    idx = find_product_index(stock, name)
    if idx is not None:
        stock[idx][1] += quantity
        stock[idx][2] = price
        return f"Produit '{name}' mis à jour (+{quantity}, prix={price})."
    else:
        stock.append([name, quantity, price])
        return f"Produit '{name}' ajouté."

def remove_product(stock, name):
    """Supprime un produit du stock."""
    idx = find_product_index(stock, name)
    if idx is None:
        return f"Produit '{name}' introuvable."
    del stock[idx]
    return f"Produit '{name}' supprimé."

def update_quantity(stock, name, new_quantity):
    """Modifie la quantité d’un produit."""
    idx = find_product_index(stock, name)
    if idx is None:
        return f"Produit '{name}' introuvable."
    stock[idx][1] = new_quantity
    return f"Quantité de '{name}' mise à {new_quantity}."

def get_products(stock):
    """Retourne la liste complète des produits."""
    return stock
