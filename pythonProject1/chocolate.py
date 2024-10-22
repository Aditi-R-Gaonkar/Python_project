import sqlite3


conn = sqlite3.connect('house.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    flavor_name TEXT NOT NULL,
                    season TEXT NOT NULL
                )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL
                )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    flavor_suggestion TEXT NOT NULL,
                    customer_name TEXT
                )''')


conn.commit()
conn.close()


def add_seasonal_flavor(flavor_name, season):
    conn = sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO seasonal_flavors (flavor_name, season) VALUES (?, ?)', (flavor_name, season))
    conn.commit()
    conn.close()


def add_ingredient(ingredient_name, quantity):
    conn = sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)',
                   (ingredient_name, quantity))
    conn.commit()
    conn.close()


def add_customer_suggestion(flavor_suggestion, customer_name=None):
    conn = sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customer_suggestions (flavor_suggestion, customer_name) VALUES (?, ?)',
                   (flavor_suggestion, customer_name))
    conn.commit()
    conn.close()


def get_seasonal_flavors():
    conn = sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_ingredient_inventory():
    conn = sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ingredient_inventory')
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_customer_suggestions():
    conn = sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customer_suggestions')
    rows = cursor.fetchall()
    conn.close()
    return rows


def main():
    while True:
        print("Choose an option:")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. View Seasonal Flavors")
        print("5. View Ingredient Inventory")
        print("6. View Customer Suggestions")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flavor_name = input("Enter the flavor name: ")
            season = input("Enter the season: ")
            add_seasonal_flavor(flavor_name, season)
        elif choice == '2':
            ingredient_name = input("Enter the ingredient name: ")
            quantity = int(input("Enter the quantity: "))
            add_ingredient(ingredient_name, quantity)
        elif choice == '3':
            flavor_suggestion = input("Enter the flavor suggestion: ")
            customer_name = input("Enter the customer name: (Press Enter to skip) ")
            add_customer_suggestion(flavor_suggestion, customer_name)
        elif choice == '4':
            flavors = get_seasonal_flavors()
            for flavor in flavors:
                print(flavor)
        elif choice == '5':
            ingredients = get_ingredient_inventory()
            for ingredient in ingredients:
                print(ingredient)
        elif choice == '6':
            suggestions = get_customer_suggestions()
            for suggestion in suggestions:
                print(suggestion)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()