class Carro:
    '''
    Classe que representa um carro com marca, modelo, cor e ano
    '''
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def detalhes(self):
        return f"{self.marca} {self.modelo} ({self.cor}, {self.ano})"


class Pessoa:
    '''
    Classe que representa uma pessoa com nome, idade, cidade e um carro
    '''
    def __init__(self, nome, idade, cidade, carro):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.carro = carro  # objeto da classe Carro

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, moro em {self.cidade} e dirijo um {self.carro.detalhes()}.")
        

# Criando instâncias de Carro
carro1 = Carro("Toyota", "Corolla", "Prata", 2020)
carro2 = Carro("Honda", "Civic", "Preto", 2018)
carro3 = Carro("BMW", "X1", "Branco", 2022)

# Criando instâncias de Pessoa com seus respectivos carros
pessoa1 = Pessoa("Ana", 25, "São Paulo", carro1)
pessoa2 = Pessoa("Carlos", 32, "Rio de Janeiro", carro2)
pessoa3 = Pessoa("Beatriz", 19, "Belo Horizonte", carro3)

# Chamando o método apresentar
pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()
