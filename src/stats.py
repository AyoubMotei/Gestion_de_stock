import numpy as np

def valeur_totale(stock):
    return sum(q * p for _, q, p in stock)

def prix_moyen(stock):
    return np.mean([p for _, _, p in stock])