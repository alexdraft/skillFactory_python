class Participant:
    def __init__(self, name, city, role):
        self.name = name
        self.city = city
        self.role = role

    def part_card(self):
        return self.name+", г. "+self.city+", статус \""+self.role+"\""

class Organizer(Participant):
    def __init__(self, name, city, role, responsibilities):
        self.name = name
        self.city = city
        self.role = role
        self.responsibilities = responsibilities

    def get_respons(self):
        return self.responsibilities


person_1 = Participant("Иван Петров", "Москва", "Наставник")
person_2 = Participant("Петр Сидоров", "Юваново", "Куратор")
person_3 = Organizer("Сидр Иванов", "Самара", "Руководитель", "Отвечает за помещение и оформление")

print(person_1.part_card())
print(person_2.part_card())
print(person_3.part_card(), person_3.get_respons())
