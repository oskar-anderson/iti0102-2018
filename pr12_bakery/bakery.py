"""Bakery model."""
from math import inf
from copy import deepcopy


class Baker:
    """Bakers."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Class constructor."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __repr__(self):
        """Enable print."""
        return f"Baker: {self.name}({self.experience_level})"


class Pastry:
    """Pastries."""

    def __init__(self, name: str, complexity_level: int):
        """Class constructor."""
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """Enable print."""
        return self.name


class Bakery:
    """Bakeries."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Class constructor."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = []
        self.pastries = []
        self.recipes = {}

    def add_baker(self, baker: Baker) -> Baker:
        """Add baker to bakers list."""
        if baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            print(f"{baker} added.")
            return baker
        else:
            print("Exp level too low!")

    def remove_baker(self, baker: Baker):
        """Remove baker from bakers list."""
        print(baker)
        try:
            self.bakers.remove(baker)
        except ValueError:
            pass

    def add_recipe(self, name: str):
        """
        Add recipe to recipe list if conditions are met.

        Conditions: there are bakers in the bakery, bakery can afford to buy recipe and recipe not already acquired.
        """
        if len(self.bakers) >= 1 and self.budget >= len(name) and name not in self.recipes:
            self.budget -= len(name)
            print(f"Current budget: {self.budget}")

            lowest_xp_level = inf
            for baker in self.bakers:
                current_xp_level = baker.experience_level
                if lowest_xp_level > current_xp_level:
                    lowest_xp_level = baker.experience_level

            complexity_level = abs(len(name) * len(self.bakers) - lowest_xp_level)
            self.recipes[name] = complexity_level
            print(f"All recipes: {self.recipes}")
        else:
            print("Conditions not met!")

    def make_order(self, name: str) -> Pastry:
        """Make pastry, assuming the bakery has the recipe and a qualified baker."""
        if name in self.recipes:
            # print(f"Recipe xp: {self.recipes[name]}")
            qualified_bakers = []
            lowest_experience = inf
            for baker in self.bakers:
                if self.recipes[name] <= baker.experience_level < lowest_experience:
                    qualified_bakers.append(baker)
                    if lowest_experience > baker.experience_level:
                        lowest_experience = baker.experience_level
            # print(qualified_bakers)
            if len(qualified_bakers) != 0:
                servicing_baker = qualified_bakers[-1]
                print(f"Servicing baker: {servicing_baker}")
                servicing_baker.experience_level += len(name)
                servicing_baker.money += 2 * len(name)
                self.budget += 2 * len(name)
                self.min_experience_level += 1
                self.pastries.append([name, self.recipes[name]])
                pastry = Pastry(name, self.recipes[name])
                print(pastry)
                return pastry
            else:
                print("No bakers!")
        else:
            print("No such recipe!")

    def get_recipes(self) -> dict:
        """Return list of bakery recipes."""
        return self.recipes

    def get_pastries(self) -> list:
        """Sort and return pastries in descending order."""
        sorted_pastries = []
        pastries_list = deepcopy(self.pastries)
        print(pastries_list)
        for i in range(len(pastries_list)):
            highest_xp_level = -inf
            for pastry_product in list(pastries_list):
                if highest_xp_level < pastry_product[1]:
                    highest_xp_level = pastry_product[1]
            for pastry_product in pastries_list:
                if pastry_product[1] == highest_xp_level:
                    pastry_product[0] = Pastry(pastry_product[0], pastry_product[1])
                    sorted_pastries.append(pastry_product[0])
                    pastries_list.remove(pastry_product)
                    break
        return sorted_pastries

    def get_bakers(self) -> list:
        """Sort and return bakers in descending order."""
        sorted_bakers = []
        # print(f"Original bakers list:{self.bakers}")
        bakers_list = deepcopy(self.bakers)
        for i in range(len(bakers_list)):
            highest_xp_level = -inf
            for baker in bakers_list:
                if highest_xp_level < baker.experience_level:
                    highest_xp_level = baker.experience_level
            for baker in bakers_list:
                if baker.experience_level == highest_xp_level:
                    sorted_bakers.append(baker)
                    bakers_list.remove(baker)
                    break
        return sorted_bakers

    def __repr__(self):
        """Enable print."""
        return f"Bakery {self.name}: {len(self.bakers)} baker(s)"


if __name__ == '__main__':

    bakery1 = Bakery("Pagariposid", 10, 100)
    print(bakery1)  # Bakery Pagariposid: 0 baker(s)
    print()

    bakery1.add_baker(Baker("Ago", 9, 0))
    print(bakery1)  # Bakery Pagariposid: 0 baker(s) => Baker Ago was not added because of low experience level (
    # Sorry Ago)
    print()

    print(bakery1.make_order("cake"))  # None => No such recipe nor baker in bakery
    print()

    ########################################################################

    polly = Baker("Polly", 10, 5)
    sam = Baker("Sam", 11, 0)
    emma = Baker("Emma", 12, 6)

    bakery1.add_baker(polly)
    bakery1.add_baker(sam)
    bakery1.add_baker(emma)

#    print(bakery1.get_bakers())
#    bakery1.remove_baker(sam)
#    bakery1.remove_baker(sam)
#    print(bakery1.get_bakers())

    # Trying to make order when no recipes are in bakery

    print(bakery1.make_order("cake"))  # None
    print()

    bakery1.add_recipe("cake")
    print(bakery1.budget)  # 96 (100 - len('cake') = 96 => price for recipe)
    print()
    print(bakery1.get_recipes())  # {'cake': 2}
    print()

    print(bakery1.make_order("cake"))  # cake
    print()

    print(bakery1.get_bakers())  # [Baker: Polly(14), Baker: Emma(12), Baker: Sam(11)] =>
    # Polly was chosen to be the baker because 'cake' complexity and Polly experience lever were the closest
    # Polly experience level was increased by len('cake') => 10 + 4 = 14
    print()

    print(bakery1.budget)  # 104 (used to be 96: 96 + len('cake') * 2 = 104)
    print()

    print(polly.money)  # 13 (5 she had + len('cake') * 2 = 13)
    print()

    print(bakery1.get_pastries())  # [cake] ("NB! cake is instance of class Pastry, not a string)
    print()

    ########################################################################

    bakery2 = Bakery("Pihlaka", 11, 100)

    john = Baker("John", 11, 5)
    megane = Baker("Megane", 17, 4)
    kate = Baker("Megane", 18, 8)

    bakery2.add_baker(john)
    bakery2.add_baker(megane)
    bakery2.add_baker(kate)

    bakery2.add_recipe("muffin")
    bakery2.add_recipe("cupcake")
    bakery2.add_recipe("biscuits")

    print(bakery2.get_recipes())  # {'muffin': 7, 'cupcake': 10, 'biscuits': 13}
    print()

    print(bakery2.get_bakers())  # [Baker: Megane(18), Baker: Megane(17), Baker: John(11)]
    print()

    bakery2.make_order("biscuits")
    print()
    print(bakery2.get_bakers())  # [Baker: Megane(25), Baker: Megane(18), Baker: John(11)]
    # Magane was chosen to be the baker as the most closest experience (which is also greater than complexity) was 17.
    print()
    bakery2.make_order("biscuits")
    bakery2.make_order("muffin")
    bakery2.make_order("cupcake")
    print(bakery2.get_pastries())
