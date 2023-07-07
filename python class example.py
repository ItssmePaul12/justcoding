class Person:
  def __init__(self, name, age, DOB, Sex):
    self.name = name
    self.age = age
    self.date_of_birth = DOB
    self.sex = Sex
person1 = Person("Alexa", 18, "Feb 29", "Female")
person2 = Person("John", 19, "Feb 2", "male")

print(person1.name)
print(person2.name)
