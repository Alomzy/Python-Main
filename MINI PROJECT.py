
class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def display_info(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ₦{self.price:,.2f}")
        print(f"Quantity in stock: {self.quantity}")
        print("-" * 30)

    def stock_value(self):
        return self.price * self.quantity

    def is_low_stock(self):
        return self.quantity < 5

    def reduce_stock(self, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        if quantity > self.quantity:
            print("Insufficient stock.")
            return False

        self.__quantity -= quantity
        return True

    def add_stock(self, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        self.__quantity += quantity
        return True


class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.sales_history = []
        self.total_revenue = 0

    def register_product(self, product):
        if self.find_product(product.product_id):
            print("Product ID already exists.")
            return

        self.products.append(product)
        print("Product registered successfully.")

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def display_products(self):
        if not self.products:
            print("No products registered.")
            return

        for product in self.products:
            product.display_info()

    def search_product(self, product_id):
        product = self.find_product(product_id)

        if product:
            product.display_info()
        else:
            print("Product not found.")

    def filter_by_category(self, category):
        found = False

        for product in self.products:
            if product.category.lower() == category.lower():
                product.display_info()
                found = True

        if not found:
            print("No products found in this category.")

    def check_low_stock(self):
        found = False

        for product in self.products:
            if product.is_low_stock():
                product.display_info()
                found = True

        if not found:
            print("No products need restocking.")

    def sell_product(self, product_id, quantity):
        product = self.find_product(product_id)

        if product is None:
            print("Sale failed: product not found.")
            return

        if quantity <= 0:
            print("Sale failed: quantity must be positive.")
            return

        if quantity > product.quantity:
            print("Sale failed: insufficient stock.")
            return

        total = product.price * quantity

        if product.reduce_stock(quantity):
            self.total_revenue += total

            sale = {
                "product_name": product.name,
                "quantity": quantity,
                "unit_price": product.price,
                "total": total
            }

            self.sales_history.append(sale)

            print("\n========== SALES RECEIPT ==========")
            print(f"Product: {product.name}")
            print(f"Quantity: {quantity}")
            print(f"Unit price: ₦{product.price:,.2f}")
            print(f"Total amount: ₦{total:,.2f}")
            print("Sale successful!")
            print("===================================")

    def view_sales_history(self):
        if not self.sales_history:
            print("No sales recorded.")
            return

        for number, sale in enumerate(self.sales_history, start=1):
            print(f"\nSale {number}")
            print(f"Product: {sale['product_name']}")
            print(f"Quantity: {sale['quantity']}")
            print(f"Unit price: ₦{sale['unit_price']:,.2f}")
            print(f"Total: ₦{sale['total']:,.2f}")

        print(f"\nTotal revenue: ₦{self.total_revenue:,.2f}")

    def generate_report(self):
        total_units = sum(
            product.quantity for product in self.products
        )

        stock_value = sum(
            product.stock_value() for product in self.products
        )

        low_stock = [
            product for product in self.products
            if product.is_low_stock()
        ]

        print("\n========== BUSINESS REPORT ==========")
        print(f"Shop name: {self.name}")
        print(f"Registered products: {len(self.products)}")
        print(f"Completed sales: {len(self.sales_history)}")
        print(f"Total units remaining: {total_units}")
        print(f"Value of remaining stock: ₦{stock_value:,.2f}")
        print(f"Total revenue: ₦{self.total_revenue:,.2f}")

        print("\nProducts needing restocking:")

        if low_stock:
            for product in low_stock:
                print(
                    f"{product.name}: "
                    f"{product.quantity} unit(s) remaining"
                )
        else:
            print("None")

        print("=====================================")


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_price(prompt):
    while True:
        try:
            value = float(input(prompt).replace(",", ""))
            if value > 0:
                return value
            print("Price must be greater than zero.")
        except ValueError:
            print("Enter a valid price, e.g. 2000.")


def register_product_menu(shop):
    product_id = input("Enter product ID: ").strip()
    name = input("Enter product name: ").strip()
    category = input("Enter product category: ").strip()

    if not product_id or not name or not category:
        print("ID, name and category cannot be empty.")
        return

    if shop.find_product(product_id):
        print("Product ID already exists.")
        return

    price = get_price("Enter unit price (₦): ")

    while True:
        try:
            quantity = int(input("Enter quantity in stock: "))
            if quantity >= 0:
                break
            print("Quantity cannot be negative.")
        except ValueError:
            print("Enter a valid whole number.")

    product = Product(
        product_id, name, category, price, quantity
    )

    shop.register_product(product)


def main():
    shop = Shop("Obinna Retail Store")

    # Register five sample products
    sample_products = [
        Product("P001", "Rice", "Food", 2000, 10),
        Product("P002", "Malt Beverage", "Beverages", 1200, 3),
        Product("P003", "Cooking Oil", "Food", 6500, 8),
        Product("P004", "Bathing Soap", "Toiletries", 900, 4),
        Product("P005", "Bottled Water", "Beverages", 500, 20)
    ]

    for product in sample_products:
        shop.register_product(product)

    while True:
        print("\n===== BUSINESS SALES AND INVENTORY SYSTEM =====")
        print("1. Register a product")
        print("2. Display all products")
        print("3. Search for a product")
        print("4. Filter products by category")
        print("5. Sell a product")
        print("6. Display low-stock products")
        print("7. View sales history")
        print("8. Generate business report")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            register_product_menu(shop)

        elif choice == "2":
            shop.display_products()

        elif choice == "3":
            product_id = input("Enter product ID: ")
            shop.search_product(product_id)

        elif choice == "4":
            category = input("Enter category: ")
            shop.filter_by_category(category)

        elif choice == "5":
            product_id = input("Enter product ID: ")
            quantity = get_integer("Enter quantity to sell: ")
            shop.sell_product(product_id, quantity)

        elif choice == "6":
            shop.check_low_stock()

        elif choice == "7":
            shop.view_sales_history()

        elif choice == "8":
            shop.generate_report()

        elif choice == "9":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Select from 1 to 9.")


if __name__ == "__main__":
    main()
