class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Puppy(Dog):
    def weeps(self):
        print("Puppy weeps")
dog = Dog()
dog.speak()
dog.bark()

puppy = Puppy()
puppy.speak()
puppy.bark()
puppy.weeps()