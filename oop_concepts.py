class Pesrson:
    def __init__(self, name):
        self.name = name
    def getPerson(self):
        return self.name

person = Pesrson("Nagu")
print(person.getPerson())