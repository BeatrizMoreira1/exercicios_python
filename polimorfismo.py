'''
o que é polimorfismo?

É quando um mesmo método tem comportamentos diferentes dependendo da classe que o usa.

pensa assim:

todas as classes têm o método apresentar()

mas cada classe fala de um jeito próprio quando você chama esse método.
'''


class Pessoa:
    def __init__(self, nome):
        self.nome = nome 

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}.")

class cliente(Pessoa):
     def apresentar(self): # mesmo nome, mas comportamento diferente
         print(f"sou cliente {self.nome}, vim comprar algo.")

class aluno(Pessoa):
    def apresentar(self):  # mesmo nome, mas comportamento diferente
        print(f"sou aluno {self.nome}, estou estudando,")

# criando objetos
p = Pessoa("Carlos")
c = cliente("Maria")
a = aluno("João")

# chamando o MESMO método "apresentar"
p.apresentar()
c.apresentar()
a.apresentar()