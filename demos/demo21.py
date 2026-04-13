class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species =species
    def sound(self, sound):
        return print(f"{self.__name} namkes {sound}")
    
cat = Animal("agy", "cat")
cat.sound("meow")

print(cat._Animal__name)