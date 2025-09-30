import matplotlib.pyplot as plt

def bar_chart(stock):
    """
    Affiche un histogramme (bar chart) des quantités par produit.
    """
    if not stock:
        print("Le stock est vide, impossible d'afficher le graphique.")
        return
    names = [p[0] for p in stock]
    quantities = [p[1] for p in stock]

    plt.figure(figsize=(8, 5))
    plt.bar(names, quantities, color="skyblue", edgecolor="black")
    plt.title("Quantités en stock par produit")
    plt.xlabel("Produits")
    plt.ylabel("Quantité")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def pie_chart(stock):
    """
    Affiche un diagramme circulaire (camembert) de la valeur du stock par produit.
    """
    if not stock:
        print("Le stock est vide, impossible d'afficher le graphique.")
        return
    names = [p[0] for p in stock]
    values = [p[1] * p[2] for p in stock]  # quantité * prix

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=names, autopct="%1.1f%%", startangle=140)
    plt.title("Répartition de la valeur du stock par produit")
    plt.tight_layout()
    plt.show()
