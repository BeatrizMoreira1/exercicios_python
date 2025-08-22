class ContaBancaria:
    
   # Classe que representa uma conta bancária sem encapsulamento.
   # Todos os atributos são públicos.
    

    def __init__(self, titular, saldo_inicial, senha):
       # Público: Pode ser acessado livremente.
        self.titular = titular
         # Protegido: não pode ser alterado diretamente.
        self._saldo = float(saldo_inicial)
       # Privado: não pode ser acessada diretamente
        self.__senha = str(senha)

    def ver_saldo(self, senha_digitada):
        # Verifica se a senha está correta.
        if str (senha_digitada) == self.__senha:
            print(f"Saldo de {self.titular}: R${self._saldo}")
        else:
            print("Senha incorreta! Acesso negado.")


# Teste
conta2 = ContaBancaria("Beatriz", 1000.00, "1234")

# Consulta com senha correta.
conta2.ver_saldo("1234")

# Tentando acessar protegido.
conta2._saldo = 50.00
conta2.ver_saldo("1234")

# Tentando acessar privado (não funciona)

try:
    print(conta2.titular)
except AttributeError:
    print("Atributos privados não pode ser acessados diretamente.")
