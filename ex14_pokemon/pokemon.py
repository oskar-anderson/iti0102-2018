"""Pokemon game."""
import requests
from collections import defaultdict
from random import randint
# from itertools import chain


class CannotAddPokemonException(Exception):
    """Custom exception."""

    pass


class NoAvailablePokemonsInWorldException(Exception):
    """Custom exception."""

    pass


class Person:
    """Simple Person class."""

    def __init__(self, name, age):
        """
        Person constructor.

        :param name: Name of the Person.
        :param age:  Age of the Person.
        """
        self.name = name
        self.age = age
        self.persons_pokemon = None

    def add_pokemon(self, pokemon):
        """
        Add pokemon to Person.

        :param pokemon: Pokemon to add.
        """
        if not isinstance(pokemon, Pokemon):
            raise CannotAddPokemonException("Must be instance of Pokemon!")
        if self.persons_pokemon is None:
            self.persons_pokemon = pokemon
        else:
            raise CannotAddPokemonException("Person already has a pokemon!")

    def get_pokemon(self):
        """
        Get Person's Pokemon.

        :return: Pokemon or None.
        """
        return self.persons_pokemon

    def remove_pokemon(self):
        """Remove Person's Pokemon."""
        self.persons_pokemon = None

    def __repr__(self):
        """
        Representation of object.

        :return: Person's name, Person's age, Pokemon: Person's pokemon.
        """
        return f"{self.name}, {self.age}, Pokemon: {self.persons_pokemon}"


class Data:
    """Class for getting data from API."""

    @staticmethod
    def get_all_pokemons_data(url):
        """
        Make request to API.

        :param url: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(url).json()

    @staticmethod
    def get_additional_data(url):
        """
        Make request to API to get additional data for each Pokemon.

        :param url: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(url).json()


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, name, experience, attack, defence, types):
        """
        Class constructor.

        :param name: Pokemon's name.
        :param experience: Pokemon's experience
        :param attack: Pokemon's attack level
        :param defence: Pokemon's defence level.
        :param types: Pokemon's types.
        """
        self.name = name
        self.experience = experience
        self.attack = attack
        self.defence = defence
        self.types = types
        self.owner = None
        self.sorting_helper = None

    def get_power(self):
        """
        Calculate power of Pokemon.

        :return: Power.
        """
        return (self.experience / self.attack + self.defence) * len(self.name)

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        return f"{self.name} experience: {self.experience} att: {self.attack} def: {self.defence} types: {self.types}"

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        return f"{self.name}"


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        self.pokemons = []
        self.available_pokemons = []

    def add_pokemons(self, no_of_pokemons):
        """Add Pokemons to world, GET data from the API."""
        pokemon_links = Data.get_all_pokemons_data("https://pokeapi.co/api/v2/pokemon/")
        for i in range(no_of_pokemons):
            url = pokemon_links["results"][i]["url"]
            pokemons = Data.get_additional_data(url)
            pokemon_types = []
            for pokemon_type in pokemons["types"]:
                pokemon_types.append(pokemon_type["type"]["name"])

            print(f"Pokemon index: {i + 1}")
            print(pokemons["name"].upper())
            print("Base XP: " + str(pokemons["base_experience"]))
            print("Defense: " + str(pokemons["stats"][1]["base_stat"]))
            print("Attack: " + str(pokemons["stats"][2]["base_stat"]))
            print("Pokemon type(s): " + str(pokemon_types))
            print()

            pokemon = Pokemon(pokemons["name"].upper(),
                              pokemons["base_experience"],
                              pokemons["stats"][1]["base_stat"],
                              pokemons["stats"][2]["base_stat"],
                              pokemon_types)
            self.pokemons.append(pokemon)
            self.available_pokemons.append(pokemon)

    def get_pokemons_by_type(self):
        """
        Get Pokemons by type.

        :return: Dict of Pokemons, grouped by types.
        """
        pokemons_by_type = defaultdict(list)
        for pokemon in self.pokemons:
            for pokemon_type in pokemon.types:
                pokemons_by_type[pokemon_type].append(pokemon.name)
        return pokemons_by_type

    def hike(self, person: Person):
        """
        Person goes to a hike to find a Pokemon.

        :param person: Person who goes to hike.
        """
        if not self.available_pokemons:
            raise NoAvailablePokemonsInWorldException("Could not find any pokemons.")
        pokemon_index = randint(0, len(self.available_pokemons) - 1)    # inclusive
        self.available_pokemons[pokemon_index].owner = person
        print(f"Pokemon index: {pokemon_index}, {self.available_pokemons[pokemon_index]}")
        person.add_pokemon(self.available_pokemons[pokemon_index])
        self.remove_available_pokemon(self.available_pokemons[pokemon_index])

    def remove_available_pokemon(self, pokemon: Pokemon):
        """
        Remove Pokemon from available Pokemons, which means that the Pokemon got a owner.

        :param pokemon: Pokemon to be removed.
        """
        self.available_pokemons.remove(pokemon)

    def remove_pokemon_from_world(self, pokemon: Pokemon):
        """
        Remove Pokemon from the world, which means that the Pokemon died.

        :param pokemon: Pokemon to be removed.
        """
        if pokemon.owner is not None:
            pokemon.owner.persons_pokemon = None
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
        if pokemon in self.available_pokemons:
            self.available_pokemons.remove(pokemon)

    def fight(self, person1: Person, person2: Person):
        """
        Two people fight with their Pokemons.

        :param person1:
        :param person2:
        :return: Pokemon which wins.
        """
        if person1.persons_pokemon.get_power() > person2.persons_pokemon.get_power():
            destroyed_pokemons_name = person2.persons_pokemon.name
            self.remove_pokemon_from_world(person2.persons_pokemon)
            person2.remove_pokemon()
            return f"There was a battle between {person1.persons_pokemon.name} and {destroyed_pokemons_name} and " \
                   f"the winner was {person1.name}"
        else:
            destroyed_pokemons_name = person1.persons_pokemon.name
            self.remove_pokemon_from_world(person1.persons_pokemon)
            person1.remove_pokemon()
            return f"There was a battle between {destroyed_pokemons_name} and {person2.persons_pokemon.name} and " \
                   f"the winner was {person2.name}"

    def group_pokemons(self):
        """
        Group Pokemons by given format.

        :return: Dictionary of grouped Pokemons.
        """
        pokemon_general_groups = ["EARTH", "FIRE", "WATER", "AIR", "OTHER"]
        pokemon_groups = {
            "EARTH": ["poison", "grass", "bug", "ground", "rock"],
            "FIRE": ["fire", "electric"],
            "WATER": ["water", "ice"],
            "AIR": ["flying", "fairy", "ghost"],
            "OTHER": ["normal", "fighting", "psychic", "steel"]}
        grouped_pokemons = defaultdict(list)
        for pokemon in self.pokemons:
            for group in pokemon_general_groups:
                if pokemon.types[0] in pokemon_groups[group]:
                    grouped_pokemons[group].append(pokemon)
        return grouped_pokemons

    def sort_by_type_experience(self):
        """
        Sort Pokemons by type and experience. The first Pokemons should be Fire type and experience level of under 100.

        :return: List of sorted Pokemons.
        """
    #    pokemon_type_order = ["poison", "grass", "bug", "ground", "rock", "electric", "water", "ice",
    #                          "flying", "fairy", "ghost", "normal", "fighting", "psychic", "steel"]
    #    pokemons_by_type = [[] for i in range(15)]
    #    for pokemon_type in pokemon_type_order:
    #        for pokemon in self.pokemons:
    #            if pokemon.types[0] == pokemon_type:
    #                pokemons_by_type[pokemon_type_order.index(pokemon_type)].append(pokemon)
    #    pokemons_by_type.insert(0, [pokemon for pokemon in self.pokemons if pokemon.types[0] == "fire" and
    #                                pokemon.experience <= 100])
    #    pokemons_by_type.insert(6, [pokemon for pokemon in self.pokemons if pokemon.types[0] == "fire" and
    #                                pokemon.experience > 100])
    #    for pokemons in pokemons_by_type:
    #        pokemons.sort(key=lambda x: -x.experience)
    #    return list(chain.from_iterable(pokemons_by_type))

        pokemon_type_order = ["poison", "grass", "bug", "ground", "rock", "fire", "electric", "water", "ice",
                              "flying", "fairy", "ghost", "normal", "fighting", "psychic", "steel"]
        for pokemon in self.pokemons:
            if pokemon.types[0] == "fire" and pokemon.experience <= 100:
                pokemon.sorting_helper = 0
            else:
                pokemon.sorting_helper = 1
        return sorted(self.pokemons, key=lambda x: (x.sorting_helper,
                                                    pokemon_type_order.index(x.types[0]),
                                                    -x.experience))

    def get_most_experienced_pokemon(self):
        """Get the Pokemon(s) which has the maximum experience level."""
        return self.get_min_or_max_experience_pokemon(max)

    def get_min_experience_pokemon(self):
        """Get the Pokemon(s) which has the minimum experience level."""
        return self.get_min_or_max_experience_pokemon(min)

    def get_min_or_max_experience_pokemon(self, min_or_max):
        """Get the Pokemon(s) which has the minimum/maximum experience level."""
        return [pokemon for pokemon in self.pokemons if pokemon.experience == (min_or_max(self.pokemons, key=lambda
                x: x.experience)).experience]


class Main:
    """No idea why this is a class."""

    if __name__ == '__main__':
        world = World("Poke land")
        world.add_pokemons(128)
        print(len(world.pokemons))  # -> 128
        print(len(world.get_pokemons_by_type().keys()))  # -> 16
        ago = Person("Ago", 10)
        peeter = Person("Peeter", 11)
        print(len(world.available_pokemons))  # -> 128
        world.hike(ago)
        ago.get_pokemon()
        world.hike(peeter)
        peeter.get_pokemon()
        print(len(world.available_pokemons))  # -> 126
        print(world.get_most_experienced_pokemon())  # -> [CHANSEY]
        print(world.get_min_experience_pokemon())  # -> [CATERPIE, WEEDLE]
        print(world.fight(ago, peeter))  # String that says who battled with who and who won.

        print()
        print(world.sort_by_type_experience())
        print(world.group_pokemons())
        print(world.get_pokemons_by_type())
        print()
