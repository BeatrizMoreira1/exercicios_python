class Pessoa:
    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade


    def apresentar(self):
       print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos. ")

#Classe Cliente (herda de Pessoa)
class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
    #Chamando o construtor da classe pai
       super().__init__(nome, idade)
       self.saldo = saldo
        
    def mostrar_saldo(self):
          print(f"{self.nome} tem um saldo de R$ {self.saldo:.2f}")

#Class aluno (herda de pessoa)
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
       # chamando o contrutor da classe pai
       super().__init__(nome, idade)
       self.matricula = matricula

    def estudar(self):
      print(f"O aluno {self.nome}, matricula {self.matricula}, está estudando!")
          
# Criando obejetos
p1 = Pessoa("Carlos", 40)
c1 = Cliente("Maria", 30, 1500.00)
a1 = Aluno("joão", 20, "A12345")

# Executando métodos
p1.apresentar()
print()

c1.apresentar()
c1.mostrar_saldo()
print()

a1.apresentar()
a1.apresentar()
    
    
    