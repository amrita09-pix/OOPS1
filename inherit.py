class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f'{self.name} is speaking')

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def barks(self):
        super().speak()
        print(f'{self.name} is a {self.breed} who loves to play')

bud = Dog('Tom','Pug')
bud.barks()
print(bud.name)
