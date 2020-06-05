# 2 -Adicione na classe Conta um novo método chamado atualiza() que atualiza a
# conta de acordo com a taxa percentual:
# a. comando: self._saldo += self._saldo * taxa

class Conta: 
    def __init__(self, name, cpf, balance): 
        self.name = name
        self.cpf = cpf
        self.balance = 0
  
    def deposit(self): 
        amount=float(input("Quanto você quer depositar?: ")) 
        self.balance += amount 
        print("Você depositou:",amount)
    
    def atualiza(self,taxa):
        self.balance += self.balance * taxa
        print("Foi adicionado uma taxa de", taxa, "reais.")

class ContaCorrente(Conta):
    def __init__(self, name, cpf, balance): 
        self.name = name
        self.cpf = cpf
        self.balance = 0

    def atualiza(self, taxa):
        self.balance += self.balance * taxa * 2
        print("Foi adicionado uma taxa de", taxa, "reais.")

    def depositCorrente(self, balance):
        amount=float(input("Quanto você quer depositar?: ")) 
        self.balance += balance - 0.10
        print("Você depositou:",amount)
        

class ContaPoupanca(Conta):
    def __init__(self, name, cpf, balance): 
        self.name = name
        self.cpf = cpf
        self.balance = 0

    def atualiza(self, taxa):
        self.balance += self.balance * taxa * 3
        print("Foi adicionado uma taxa de", taxa, "reais.")
  
c = Conta('Joana', '123-345-125.43', 0)
cc = ContaPoupanca('Joana', '123-345-125.43', 0)
ccc = ContaPoupanca('Joana', '123-345-125.43', 0)

c.deposit()
cc.deposit()
ccc.deposit()

c.atualiza(0.01)
cc.atualiza(0.01)
ccc.atualiza(0.01)

print("Você se chama", c.name , "do cpf", c.cpf , "e tem atualmente", c.balance , "reais!")
print("Você se chama", cc.name , "do cpf", cc.cpf , "e tem atualmente", cc.balance , "reais!")
print("Você se chama", ccc.name , "do cpf", ccc.cpf , "e tem atualmente", ccc.balance , "reais!")