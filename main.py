
class Animal:
    def speak(self):
        return f'Ррррр!'
class Dog(Animal):
    def speak(self):
        return super().speak() + ' Гав-Гав'


dog = Dog()
print(dog.speak())