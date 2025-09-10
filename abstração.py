'''
O que é Abstração?

é esconder os detalhes internos de implementação e mostrar apenas o que é necessário.

A ideia é trabalhar no nivel mais genérico e deixar que as classes
mais especificas implementem os detalhes.
'''


from abc import ABC, abstractmethod

# classe abstrata (não pode ser instanciada diretamente)
class pessoa(ABC):
    def __init__(self, nome):
      self.nome = nome 
    

    @abstractmethod
    def apresentar(self): # método abstrato ()
        pass
# classe concreta Cliente
class cliente(pessoa):
    def apresentar(self):
        print(f"sou cliente {self.nome}, comprando no sistema.")

# classe concreta aluno
class Aluno(pessoa):
     def apresentar(self):
         print(f"Sou aluno {self.nome},, estudando no sistema.")

# p = pessoa("carlos")  # isso dá erro: pessoa é abstrata! 