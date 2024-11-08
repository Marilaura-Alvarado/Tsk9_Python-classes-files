class Animals:
    """This class is about animals"""

    def __init__(self, genus, name, year_of_b, origins):
        self.genus = genus
        self.name = name
        self.year_of_b = year_of_b
        self.origins = origins

    def get_age(self):
        return 2024 - self.year_of_b

    def get_info(self):
        return self.name + " is a " + self.genus


animal1 = Animals("fox", "Alice", 2010, "Sweden")
print(animal1.get_age())
print(animal1.get_info())
animal2 = Animals("lion", "Moto", 2009, "Africa")
print(animal2.get_age())
print(animal2.get_info())
animal3 = Animals("otter", "Chip", 2007, "Australia")
print(animal3.get_age())
print(animal3.get_info())

animals_list = [animal1, animal2, animal3]


def find_oldest(animals_list):
    oldest_animal = animals_list[0]
    for animal in animals_list:
        if animal.get_age() > oldest_animal.get_age():
            oldest_animal = animal
    return oldest_animal


oldest = find_oldest(animals_list)
print(f"The {oldest.name} is a {oldest.genus}, it's {oldest.get_age()} y.o.")

with open("animals.txt", "w") as file:
    for animal in animals_list:
        file.write(f"{animal.name}, {animal.genus}\n")
