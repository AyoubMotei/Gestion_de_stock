import stock
import stats
import visualize

def print_products(stock_list):
    """Affiche tous les produits en tableau."""
    if not stock_list:
        print("Stock vide.")
        return
    print(f"{'Nom':20} {'Quantité':>8} {'Prix':>10}")
    print("-" * 40)
    for name, qty, price in stock_list:
        print(f"{name:20} {qty:8} {price:10.2f}")

def input_int(prompt):
    """Assure que l’utilisateur entre un entier."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrez un entier valide.")

def input_float(prompt):
    """Assure que l’utilisateur entre un float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrez un nombre valide (ex: 12.5).")

def show_menu(stock_list):
    """Boucle principale du menu."""
    while True:
        print("\n--- Gestion du stock ---")
        print("1. Ajouter un produit")
        print("2. Supprimer un produit")
        print("3. Mettre à jour une quantité")
        print("4. Afficher le stock")
        print("5. Statistiques") 
        print("6. Visualisation") 
        print("7. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            name = input("Nom du produit : ").strip()
            qty = input_int("Quantité : ")
            price = input_float("Prix unitaire : ")
            print(stock.add_product(stock_list, name, qty, price))

        elif choix == "2":
            name = input("Nom du produit à supprimer : ").strip()
            print(stock.remove_product(stock_list, name))

        elif choix == "3":
            name = input("Nom du produit : ").strip()
            qty = input_int("Nouvelle quantité : ")
            print(stock.update_quantity(stock_list, name, qty))

        elif choix == "4":
            print_products(stock.get_products(stock_list))

        elif choix == "5":
            print("\n--- Statistiques ---")
            print(f"Valeur totale du stock : {stats.total_value(stock_list):.2f}")
            print(f"Prix moyen : {stats.average_price(stock_list):.2f}")
            print(f"Prix minimum : {stats.min_price(stock_list):.2f}")
            print(f"Prix maximum : {stats.max_price(stock_list):.2f}")
            cheapest = stats.cheapest_product(stock_list)
            expensive = stats.most_expensive_product(stock_list)
            print(f"Produit le moins cher : {cheapest[0]} ({cheapest[1]:.2f})")
            print(f"Produit le plus cher : {expensive[0]} ({expensive[1]:.2f})")
            
        elif choix == "6":
            print("\n--- Visualisation ---")
            print("1. Histogramme des quantités")
            print("2. Camembert de la valeur du stock")
            sub_choice = input("Choix : ").strip()
            if sub_choice == "1":
                visualize.bar_chart(stock_list)
            elif sub_choice == "2":
                visualize.pie_chart(stock_list)
            else:
                print("Choix invalide.")
        elif choix == "7":
            print("Au revoir")
            break
        else:
            print("Choix invalide, essayez encore.")
            