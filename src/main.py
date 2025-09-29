
from menu import show_menu

def main():
    # Stock initial
    stock = [
        ["Clavier", 10, 45.0],
        ["Souris", 25, 15.5],
        ["Écran", 5, 320.0],
    ]

    show_menu(stock)

if __name__ == "__main__":
    main()
