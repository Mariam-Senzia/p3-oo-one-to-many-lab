class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in self.PET_TYPES:
            raise TypeError("Pet_type must be included in PET_TYPES")
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name 

    def pets(self): 
        return Pet.all
    
    def add_pet(self, pet):
        if pet.pet_type in Pet.PET_TYPES:
            pet.owner = self
            Pet.all.append(pet)

    def pet_name(self, pet):
        return pet.name

    def get_sorted_pets(self):
        return sorted(Pet.all, key=self.pet_name)
    
owner = Owner("John")
pet = Pet("Fluffy", "dog", owner)

