class Person:
    
    GENDER = ['F', 'M']
    deceased = False
    
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.pets = []
    
    def mark_as_deceased(self):
        self.deceased = True
    
    def printing (self):
        print(self.name)
        print(self.title)
        
    def add_pets(self, pet):
        self.pets.append(pet)
    
namuObj = Person (
    "Nami",
    'Mr'
    )

# namuObj.printing()
# print(Person.GENDER)
# print(namuObj.GENDER)
# #print(Person.title)

rutuObj = Person (
    "Rutu",
    'Mr'
    )

# namuObj.mark_as_deceased()
# print(namuObj.deceased)
# print(rutuObj.deceased)

rutuObj.add_pets('cat')
print(namuObj.pets)
print(rutuObj.pets)