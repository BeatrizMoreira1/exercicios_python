class Carro:
    '''
    Classe que representa um carro com marca e modelo
    '''
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalhes(self):
        return f"{self.marca} {self.modelo}"


class Pessoa:
    '''
    Classe que representa uma pessoa com nome, idade, cidade e um carro
    '''
    def __init__(self, nome, idade, cidade, carro=None):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.carro = carro  # objeto da classe Carro (opcional)

    def apresentar(self):
        mensagem = f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}."
        if self.carro:
            mensagem += f" Eu dirijo um {self.carro.detalhes()}."
        print(mensagem)

    def dirigir(self):
        if self.carro:
            print(f"{self.nome} está dirigindo seu {self.carro.detalhes()}.")
        else:
            print(f"{self.nome} não tem carro para dirigir.")


# Criando carros
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Criando pessoas com e sem carro
pessoa1 = Pessoa("Ana", 25, "São Paulo", carro1)
pessoa2 = Pessoa("Carlos", 32, "Rio de Janeiro", carro2)
pessoa3 = Pessoa("Beatriz", 19, "Belo Horizonte")  # sem carro

# Apresentações
pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()

# Testando dirigir
pessoa1.dirigir()
pessoa3.dirigir()
    