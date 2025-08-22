
class Carro:
  
    '''
     Comenta mais de uma linha 3 aspas simples
    '''

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} está acelerando")



carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro3 = Carro("BMW", "X1")


carro1.acelerar() 
carro2.acelerar() 
carro3.acelerar() 