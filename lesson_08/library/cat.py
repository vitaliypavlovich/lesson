from lesson_08.library.animal import Animal

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")
