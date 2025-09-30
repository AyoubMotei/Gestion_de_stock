# Stock Manager – Project Documentation

## 📖 Overview

The **Stock Manager** is a simple Python application for managing a product inventory.
It allows the user to:

* Add, remove, and update products.
* Display stock details in a formatted table.
* Calculate basic statistics (total value, mean price, min/max, most/least expensive).
* Visualize stock using bar and pie charts.
* Interact with everything via a console menu.

This project is beginner-friendly and modular. Each feature is isolated in a dedicated Python file to encourage clean design and maintainability.

---

## 📂 Project Structure

```
stock-manager/
├─ src/
│  ├─ main.py          # Entry point (CLI menu logic)
│  ├─ stock.py         # Stock management (CRUD operations)
│  ├─ stats.py         # Statistical calculations
│  ├─ visualize.py     # Graphical visualizations (matplotlib)
│  └─ menu.py          # Menu and input validation helpers
├─ README.md           # Basic project setup and usage
├─ requirements.txt    # Dependencies (numpy, matplotlib)
└─ .gitignore          # Ignore Python cache and venv files
```

---

## ⚙️ Installation & Setup

1. **Clone or create project folder**

   ```bash
   git clone <your-repo-url> stock-manager
   cd stock-manager
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   ```

   * On Linux/macOS:

     ```bash
     source venv/bin/activate
     ```
   * On Windows (PowerShell):

     ```bash
     venv\Scripts\Activate.ps1
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run application**

   ```bash
   python src/main.py
   ```

---

## 🗂 Module Documentation

### 1. `stock.py`

Handles the **in-memory stock list** and CRUD operations.
Each product is stored as a list: `[name, quantity, unit_price]`.

#### Functions

* `add_product(stock, name, quantity, price)` → Add a new product.
* `remove_product(stock, name)` → Remove product by name.
* `update_quantity(stock, name, new_quantity)` → Modify quantity.
* `list_products(stock)` → Return a copy of the stock list.
* `product_value(product)` → Compute value = quantity × price.
* `find_index(stock, name)` (internal) → Locate product index.
* `_normalize(name)` (internal) → Clean and lowercase names.

#### Notes

* Validates negative values.
* Prevents duplicates.
* Errors are raised as `ValueError`.

---

### 2. `stats.py`

Provides **statistical insights** using `numpy`.

#### Functions

* `total_stock_value(stock)` → Sum of all products’ values.
* `mean_unit_price(stock)` → Average price of products.
* `min_max_price(stock)` → Returns `(min_price, max_price)`.
* `most_and_least_expensive(stock)` → Dicts of most/least expensive products.

#### Example

```python
from stats import total_stock_value
print(total_stock_value(stock))  # 1525.50
```

---

### 3. `visualize.py`

Generates **charts with matplotlib**.

#### Functions

* `bar_chart_quantity(stock)` → Bar chart of quantities per product.
* `pie_chart_value(stock)` → Pie chart of stock value distribution.

#### Notes

* Gracefully handles empty stock.
* No explicit colors (uses matplotlib defaults).
* Calls `plt.show()` directly.

---

### 4. `menu.py`

Utility functions for **CLI menus and input validation**.

#### Functions

* `print_menu()` → Display interactive menu.
* `input_positive_int(prompt)` → Read non-negative integer.
* `input_non_negative_float(prompt)` → Read non-negative float.

#### Example

```python
qty = menu.input_positive_int("Quantité: ")
```

---

### 5. `main.py`

The **entry point** that connects all modules.

#### Features

* Console menu for CRUD, statistics, and visualization.
* Displays stock table with formatted columns.
* Preloaded with sample products (`Clavier`, `Souris`, `Écran`).
* Loop until user chooses “Quitter”.

---

## 🖥️ Usage Walkthrough

1. Start app:

   ```
   python src/main.py
   ```

2. Menu options:

   ```
   1. Ajouter un produit
   2. Supprimer un produit
   3. Modifier la quantité
   4. Afficher le stock
   5. Afficher les statistiques
   6. Afficher un graphique
   7. Quitter
   ```

3. Example session:

   * Add `Chaise (5 × 120.0)`.
   * Display stock → see new row.
   * Check statistics → updated totals.
   * Show pie chart → distribution updated.

---

## 📊 Example Outputs

### Stock Table

```
Produit                   | Quantité | Prix unité | Valeur totale
-----------------------------------------------------------------
Clavier                   |       10 |      45.00 |        450.00
Souris                    |       15 |      25.00 |        375.00
Écran                     |        5 |     250.00 |       1250.00
Chaise                    |        5 |     120.00 |        600.00
```

### Statistics

```
Valeur totale du stock: 2675.00
Prix moyen des produits: 110.00
Prix minimum: 25.00, prix maximum: 250.00
Produit le plus cher: Écran à 250.00
Produit le moins cher: Souris à 25.00
```

### Graphs

* **Bar chart:** Product quantities.
* **Pie chart:** Share of total value.

---

## 🛠️ Testing Checklist

* [ ] Add product with valid/invalid inputs.
* [ ] Remove non-existing product (expect error).
* [ ] Update quantity (negative value blocked).
* [ ] Display stock table with/without products.
* [ ] Check statistics on empty stock.
* [ ] Generate bar/pie chart with products.

---

## 🗃️ Git Workflow

* Initialize repo:

  ```bash
  git init
  git add .
  git commit -m "Initial project setup"
  ```

* Create feature branch:

  ```bash
  git checkout -b feature/add-stats
  ```

* Merge branch after testing:

  ```bash
  git checkout main
  git merge feature/add-stats
  ```

* Example commit messages:

  * `feat: add stock CRUD functions`
  * `feat: add bar and pie charts`
  * `fix: handle empty stock gracefully`

---

## 📌 Possible Improvements

* **Persistence**: Save/load stock to JSON or CSV files.
* **Search/filter**: Find products by partial name or price range.
* **Unit testing**: Use `pytest` for automatic verification.
* **Refactor**: Replace list-of-lists with dataclasses/dicts.
* **Export**: Generate PDF/Excel reports.
* **GUI**: Build a simple Tkinter or web-based interface.

---

## 👥 Jira Task Breakdown

* **Epic: Stock Manager**

  * Task: Project skeleton & README
  * Task: Implement `stock.py` (CRUD)
  * Task: Implement `stats.py` (statistics)
  * Task: Implement `visualize.py` (charts)
  * Task: Implement `menu.py` (inputs)
  * Task: Implement `main.py` (menu loop)
  * Task: Write documentation
  * Task: Testing & bug fixes

---

## 📜 License

MIT License (example – update according to your needs).
