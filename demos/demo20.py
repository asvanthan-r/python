class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species =species
    def sound(self, sound):
        return print(f"{self._name} namkes {sound}")
    
cat = Animal("agy", "cat")
cat.sound("meow")

print(cat._name)