"""Gym model."""
from math import inf
from statistics import mean


class Trainers:
    """Trainers."""

    def __init__(self, stamina: int, color: str):
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        return f"Trainers: [{self.stamina}, {self.color}]"


class Member:
    """Members."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        self.name = name
        self.age = age
        self.trainers = trainers

    def get_all_gyms(self) -> list:
        pass

    def __repr__(self):
        return f"{self.name}, {self.age}: {self.trainers}"

    def get_gyms(self) -> list:
        pass


class Gym:
    """Gym."""

    def __init__(self, name: str, max_members_number: int):
        self.name = name
        self.max_members_number = max_members_number
        self.members = []

    def add_member(self, member: Member) -> Member:
        if self.can_add_member(member) is True:
            if len(self.members) == self.max_members_number:
                min_stamina = inf
                for member in self.members:
                    if member.trainers.stamina < min_stamina:
                        min_stamina = member.trainers.stamina
                number_of_removes = 0
                for x in range(len(self.members)):
                    if self.members[x - number_of_removes].trainers.stamina == min_stamina:
                        self.remove_member(self.members[x - number_of_removes])
                        number_of_removes += 1
            self.members.append(member)
            return member

    def can_add_member(self, member: Member) -> bool:
        if isinstance(member, Member) is True and member not in self.members and member.trainers is not None:
            if member.trainers.color is not None and member.trainers.stamina >= 0:
                return True
        return False

    def remove_member(self, member: Member):
        if member in self.members:
            self.members.remove(member)

    def get_total_stamina(self) -> int:
        total_stamina = 0
        for member in self.members:
            total_stamina += member.trainers.stamina
        return total_stamina

    def get_members_number(self) -> int:
        return len(self.members)

    def get_all_members(self) -> list:
        return self.members

    def get_average_age(self) -> float:
        total_age = 0
        for member in self.members:
            total_age += member.age
        return total_age / len(self.members)

    def __repr__(self):
        return f"Gym {self.name} : {len(self.members)} member(s)"  # {members_number}


class City:
    """City."""

    def __init__(self, max_gym_number: int):
        self.max_gym_number = max_gym_number
        self.gyms = []

    def build_gym(self, gym: Gym) -> Gym:
        if self.can_build_gym():
            self.gyms.append(gym)
            return gym

    def can_build_gym(self) -> bool:
        if self.max_gym_number > len(self.gyms):    # test puts in 9 with limit 10 and 10th should return False?
            return True
        else:
            return False

    def destroy_gym(self):
        min_members_count = inf
        for gym in self.gyms:
            if min_members_count < len(gym.members):
                min_members_count = len(gym.members)
        gyms_to_destroy = []
        for gym in self.gyms:
            if len(gym.members) <= min_members_count:
                gyms_to_destroy.append(gym)

        for gym in gyms_to_destroy:
            if gym in self.gyms:
                self.gyms.remove(gym)

    def get_max_members_gym(self) -> list:
        max_members_count = -inf
        for gym in self.gyms:
            if max_members_count < len(gym.members):
                max_members_count = len(gym.members)
        # print(max_members_count)
        max_members_gym = []
        for gym in self.gyms:
            if len(gym.members) == max_members_count:
                max_members_gym.append(gym)
        return max_members_gym

    def get_max_stamina_gyms(self) -> list:
        gym_stamina_values = []
        for gym in self.gyms:
            individual_gym_stamina = []
            for x in range(len(gym.members)):
                individual_gym_stamina.append(gym.members[x].trainers.stamina)
            gym_stamina_values.append(mean(individual_gym_stamina))
        max_stamina = max(gym_stamina_values)
        max_gym_stamina = []
        for x in range(len(gym_stamina_values)):
            if gym_stamina_values[x] == max_stamina:
                max_gym_stamina.append(self.gyms[x])
        return max_gym_stamina

    def get_max_average_ages(self) -> list:
        return self.get_min_or_max_average_ages(max)

    def get_min_average_ages(self) -> list:
        return self.get_min_or_max_average_ages(min)

    def get_min_or_max_average_ages(self, max_or_min) -> list:
        max_or_min_average_age_value_list = []
        max_or_min_average_age_list = []
        for gym in self.gyms:
            individual_average_age = []
            for gym_member in gym.members:
                individual_average_age.append(gym_member.age)
            max_or_min_average_age_value_list.append(mean(individual_average_age))
        max_or_min_average_age = (max_or_min(max_or_min_average_age_value_list))
        print(f"Max or min average age: {max_or_min_average_age}")
        for x in range(len(max_or_min_average_age_value_list)):
            if max_or_min_average_age_value_list[x] == max_or_min_average_age:
                max_or_min_average_age_list.append(self.gyms[x])
        return max_or_min_average_age_list

    def get_gyms_by_trainers_color(self, color: str) -> list:
        pass

    def get_gyms_by_name(self, name: str) -> list:
        pass

    def get_all_gyms(self) -> list:
        return self.gyms


if __name__ == "__main__":
    city1 = City(100)
    gym1 = Gym("TTÜ Sport", 50)
    city1.build_gym(gym1)

    trainers1 = Trainers(50, "blue")
    trainers2 = Trainers(50, "grey")

    member1 = Member("Ago Luberg", 35, trainers1)
    member2 = Member("Ahti Lohk", 35, trainers2)

    gym1.add_member(member1)
    gym1.add_member(member2)

    print(gym1.get_members_number())  # 2

    print(gym1.get_all_members())  # [Ago Luberg, 35: Trainers: [50, blue], Ahti Lohk, 35: Trainers: [50, grey]]

    gym1.add_member(member1)  # Trying to add Ago again
    print(gym1.get_members_number())  # 2 //We can't...

    for i in range(48):
        gym1.add_member(Member("Tudeng Tudeng", 20, Trainers(49, "blue")))

    print(gym1.get_members_number())  # 50

    trainers3 = Trainers(60, "blue")
    member_new = Member("Megane", 19, trainers3)
    gym1.add_member(member_new)

    print(gym1.get_members_number())
    # 3 -> Ago, Ahti and Megan, all others were removed because of the lowest trainers' stamina

    city2 = City(10)
    gym2 = Gym("MyFitness", 100)
    city2.build_gym(gym2)
    city2.destroy_gym()

    for i in range(9):
        city2.build_gym(Gym("Super Gym", 10))

    print(city2.can_build_gym())  # False -> Cannot build gym, city is full of them
    print()
    #######################################################################################

    city3 = City(100)

    gym4 = Gym("Sparta", 50)
    gym5 = Gym("People Fitness", 30)
    gym6 = Gym("Gym Eesti", 100)

    print(city3.build_gym(gym4))
    print(city3.build_gym(gym5))
    print(city3.build_gym(gym6))

    print()
    print(gym4.add_member(Member("Bob", 18, Trainers(50, "black"))))
    print(gym4.add_member(Member("Emma", 20, Trainers(70, "red"))))
    print(gym4.add_member(Member("Ken", 25, Trainers(40, "grey"))))

    print()
    print(gym5.add_member(Member("Merili", 18, Trainers(100, "pink"))))
    print(gym5.add_member(Member("Richard", 20, Trainers(70, "green"))))

    print()
    print(gym6.add_member(Member("Bella", 40, Trainers(15, "green"))))
    print(gym6.add_member(Member("Bob", 50, Trainers(70, "green"))))
    print(gym6.add_member(Member("Sandra", 25, Trainers(30, "pink"))))
    print(gym6.add_member(Member("Bob", 35, Trainers(50, "black"))))

    print()
    print(city3.get_max_members_gym())  # [Gym Gym Eesti : 4 member(s)]
    print(city3.get_max_stamina_gyms())  # [Gym People Fitness : 2 member(s)]
    print()
    print(city3.get_max_average_ages())  # [Gym Gym Eesti : 4 member(s)] => average age 37,5
    print(city3.get_min_average_ages())  # [Gym People Fitness : 2 member(s)] => average age 19
    print()
    print(city3.get_gyms_by_trainers_color("green"))
    # [Gym Gym Eesti : 4 member(s), Gym People Fitness : 2 member(s)] => Gym Eesti has 2 members with green trainers,
    # People Fitness has 1.
    print(city3.get_gyms_by_name("Bob"))
    # [Gym Gym Eesti : 4 member(s), Gym Sparta : 2 member(s)] => Gym Eesti has 2 members with name Bob, Sparta has 1.

    print()
    print(city3.get_all_gyms())
