import matplotlib.pyplot as plt

def bar_chart(stock):
    noms = [p[0] for p in stock]
    quantites = [p[1] for p in stock]
    plt.bar(noms, quantites)
    plt.title("Quantité par produit")
    plt.show()