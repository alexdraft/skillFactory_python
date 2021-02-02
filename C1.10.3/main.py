class Client:
    def __init__(self, name, lastname, balance):
        self.name = name
        self.lastname = lastname
        self.balance = balance

    def client_card(self):
         return "Клиент \""+self.name+" "+self.lastname+"\". Баланс: "+str(self.balance)+" руб."


client_1 = Client("Иван", "Петров", 50)
print(client_1.client_card())
