# class Person:
#     
#     GENDER = ['F', 'M']
#     deceased = False
#     discount=0
#     def __init__(self, name, title):
#         self.name = name
#         self.title = title
#         self.pets = []
#     
#     def mark_as_deceased(self):
#         self.deceased = True
#     
#     def printing (self):
#         print(self.name)
#         print(self.title)
#         
#     def add_pets(self, pet):
#         self.pets.append(pet)
#     
#     @classmethod
#     def pet_care_discount(cls, discount):
#         cls.discount = discount
#         
#     
# namuObj = Person (
#     "Nami",
#     'Mr'
#     )
# 
# 
# rutuObj = Person (
#     "Rutu",
#     'Mr'
#     )


# print(Person.discount)
# print(namuObj.discount)
# Person.pet_care_discount(10)
# print(Person.discount)
# print(namuObj.discount)



class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return "%s %s" % (self.name, self.surname)

jane = Person("Jane", "Smith")

print(type(Person))



def print_object_attrs(any_object):
    for k, v in any_object.__dict__.items():
        print("%s: %s" % (k, v))
print_object_attrs(jane)