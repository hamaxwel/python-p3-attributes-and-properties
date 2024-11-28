approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            if 1 <= len(name) <= 25:
                self._name = name
            else:
                print("Name must be string between 1 and 25 characters.")
                self._name = None  # Ensure name is set to None to avoid invalid state.
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Ensure name is set to None to avoid invalid state.

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if self._name:  # Only validate breed if name is valid
            if breed in approved_breeds:
                self._breed = breed
            else:
                print("Breed must be in list of approved breeds.")
        else:
            self._breed = None  # Avoid saving breed if name is invalid

    breed = property(get_breed, set_breed)
