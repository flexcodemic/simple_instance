class Person:
    # Declare the required attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # Declare the method here...
    def introduce(self):
        print(f'{self.name} is {self.age} years old {self.gender}');

# Create an Instance or Object
p1 = Person('Joe', 35, 'male')
p1.introduce()