import numpy as np

def total_value(stock):
    """
    Calcule la valeur totale du stock = somme(prix * quantité).
    """
    if not stock:
        return 0.0
    quantities = np.array([p[1] for p in stock])
    prices = np.array([p[2] for p in stock])
    return float(np.sum(quantities * prices))

def average_price(stock):
    """
    Prix moyen des produits.
    """
    if not stock:
        return 0.0
    prices = np.array([p[2] for p in stock])
    return float(np.mean(prices))

def min_price(stock):
    """
    Prix minimum parmi les produits.
    """
    if not stock:
        return None
    prices = np.array([p[2] for p in stock])
    return float(np.min(prices))

def max_price(stock):
    """
    Prix maximum parmi les produits.
    """
    if not stock:
        return None
    prices = np.array([p[2] for p in stock])
    return float(np.max(prices))

def cheapest_product(stock):
    """
    Retourne le produit le moins cher (nom, prix).
    """
    if not stock:
        return None
    min_p = min(stock, key=lambda p: p[2])
    return (min_p[0], min_p[2])

def most_expensive_product(stock):
    """
    Retourne le produit le plus cher (nom, prix).
    """
    if not stock:
        return None
    max_p = max(stock, key=lambda p: p[2])
    return (max_p[0], max_p[2])
