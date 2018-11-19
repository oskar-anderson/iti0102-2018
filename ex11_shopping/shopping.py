"""Store imitation."""


class ProductCannotBeSold(Exception):
    """Create a new exception called "ProductCannotBeSold"."""


class Product:
    """Represents product model."""

    def __init__(self, name: str, price: int) -> None:
        """
        Class constructor. Each product has name and price.

        :param name: product name
        :param price: product price
        """
        self.name = name
        self.price = price
        print(f"Product_name: {self.name}, price: {self.price}")

    def __str__(self) -> str:
        """
        Product object representation in string format.

        :return: string
        """
        return f"Product: {self.name}, price: {self.price}"

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return self.name


class Customer:
    """Represents customer model."""

    def __init__(self, name: str, age: int, money: int = 0) -> None:
        """
        Class constructor. Each customer has name, age and money when being created.

        Customer also has storage for bought items.
        :param name: customer's name
        :param age: customer's age
        :param money: customer's money
        """
        self.name = name
        self.age = age
        self.money = money
        self.bought_items = []
        print(f"Name: {self.name}, age: {self.age}, money: {self.money}")

    def add_item(self, product: Product, amount: int) -> None:
        """
        Add bought items to customer's items.

        :param product: product
        :param amount: amount
        """
        for i in range(amount):
            self.bought_items.append(product)
        print(f"Bought items:{self.bought_items}")

    def pay(self, money_to_pay: int) -> None:
        """
        Check if customer has enough money to pay for the product.

        Returns nothing, but raises exception if customer has not enough money to pay.
        In other case reduces amount of customer's money.
        :param money_to_pay: money amount needed to be paid
        """
        if self.money < money_to_pay:
            raise ProductCannotBeSold("You do not have enough money to pay for chosen product!")
        else:
            self.money -= money_to_pay
            print(f"Customer money remaining: {self.money}")

    def __str__(self) -> str:
        """
        Customer object representation in string format.

        :return: string
        """
        formatted_bought_items = []
        duplicates_removed = set(self.bought_items)
        for i in range(len(duplicates_removed)):
            product_key = duplicates_removed.pop()
            product_amount = self.bought_items.count(product_key)
            if product_amount == 1:
                formatted_bought_items.append(product_key)
            else:
                end_length = (str(product_key).find(", price"))
                product_key = str(product_key)[9:end_length] + "(" + str(product_amount) + ")"
                # print(product_key)
                formatted_bought_items.append(product_key)
        # print(formatted_bought_items)
        symbols_to_strip = "\'[]"
        # formatted_bought_items = str(formatted_bought_items).strip(symbols_to_strip)  # water, 'chocolate(2)  why?
        while True:
            formatted_bought_items = str(formatted_bought_items).strip(symbols_to_strip)
            if formatted_bought_items.find("'") == -1:
                break
            remove_character = formatted_bought_items.find("'")
            formatted_bought_items = formatted_bought_items[:remove_character] + formatted_bought_items[remove_character + 1:]
        return f"{self.name}'s items: {formatted_bought_items}; money: {self.money}."


class Store:
    """Represents store model."""

    def __init__(self) -> None:
        """Class constructor."""
        self.money = 0
        self.products = []
        self.amount = 0

    def buy(self, product: Product, amount: int, customer: Customer) -> str:
        """
        Represent how customer buys product.

        :param product: product the customer wants
        :param amount: pieces of product
        :param customer: customer who wants to buy
        :return: message
        """
        print(f"Products in store: {self.products}")
        if self.check_product_availability(product, amount) is None:   # store is Store() in tester?
            pass
        if self.allowed_to_buy(product, customer) is None:
            pass
        if customer.pay(product.price * amount):
            pass
        # if customer.money < product.price * amount:
        #    raise ProductCannotBeSold("You do not have enough money to pay for chosen product!")
        self.amount += amount
        self.products.remove(product)
        # print(self.products)
        customer.add_item(product, amount)
        self.money += product.price * amount
        return "Thank you for the purchase!"

    def allowed_to_buy(self, product: Product, customer: Customer):
        """
        Check if customer is allowed to buy some particular products.

        Permission depends on customer's age

        Customers under 18 are not allowed to buy beer and tobacco.
        Must raise exception if customer has no permission to buy chosen product.
        :param product: product to buy
        :param customer: customer who makes the purchase
        """
        if product.name in ["beer", "tobacco"] and customer.age < 18:
            # print(product.name)
            # print(customer.age)
            # raise ProductCannotBeSold(f"You are too young to buy Product: {product.name}!")
            raise ProductCannotBeSold(f"You are too young to buy {product.name}!")

    def check_product_availability(self, product: Product, amount: int):
        """
        Check if chosen amount of product is present in stock.

        Must raise exception if no product found or not enough in stock.
        :param product: product to be bought
        :param amount: amount of product
        """
        if product in self.products:
            if self.products.count(product) >= amount:
                pass
            else:
                raise ProductCannotBeSold("Item is not available in chosen amount!")
        else:
            raise ProductCannotBeSold("Item not found!")

    def add_product(self, product: Product) -> None:
        """
        Adding product to store.

        :param product:  product name
        """
        self.products.append(product)

    def __str__(self) -> str:
        """
        Store object representation in string format.

        :return: string
        """
        # return f"Store items: {self.products}; store money: {self.money}."
        formatted_bought_items = []
        duplicates_removed = set(self.products)
        for i in range(len(duplicates_removed)):
            product_key = duplicates_removed.pop()
            product_amount = self.products.count(product_key)
            if product_amount == 1:
                formatted_bought_items.append(product_key)
            else:
                end_length = (str(product_key).find(", price"))
                product_key = str(product_key)[9:end_length] + "(" + str(product_amount) + ")"
                print(product_key)
                formatted_bought_items.append(product_key)
        print(formatted_bought_items)
        symbols_to_strip = "\'[]"
        while True:
            formatted_bought_items = str(formatted_bought_items).strip(symbols_to_strip)
            remove_character = formatted_bought_items.find("'")
            formatted_bought_items = formatted_bought_items[:remove_character] + formatted_bought_items[remove_character + 1:]
            if formatted_bought_items.find("'") == -1:
                break
        return f"Store items: {formatted_bought_items}; store money: {self.money}."


if __name__ == "__main__":
    john = Customer("John", 20, 300)
    bobby = Customer("Bobby", 17, 150)
    sandy = Customer("Sandy", 12, 100)

    store = Store()

    beer = Product("beer", 50)
    water = Product("water", 30)
    choco = Product("chocolate", 45)
    pretzel = Product("pretzel", 35)

    store.add_product(beer)
    store.add_product(water)
    for _ in range(3):
        store.add_product(choco)
        store.add_product(pretzel)
    print(store)   # Products: [beer, water, chocolate, pretzel, chocolate, pretzel, chocolate, pretzel] from store

    print()
    print(store.buy(beer, 1, john))  # -> Thank you for the purchase!
    print()
    print(beer not in store.products)  # -> True
    print()
    print(john)  # -> John's items: beer; money: 250.
    print()

    # tobacco = Product("tobacco", 55)
    # store.add_product(tobacco)
    # print(store.buy(tobacco, 1, bobby))  # -> You are too young to buy Product: tobacco, price: 55!

    # print(store.buy(water, 2, sandy))  # -> Item is not available in chosen amount!

    # candy = Product("candy", 25)
    # print(store.buy(candy, 1, bobby))  # -> Item not found!

    store.buy(choco, 2, bobby)
    print(bobby.money)  # -> 60
    print()
    store.buy(water, 1, bobby)
    print(bobby)  # -> Bobby's items: chocolate(2), water; money: 30
