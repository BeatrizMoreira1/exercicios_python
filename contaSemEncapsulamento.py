class ContaSemEncapsulamento:
    '''
    Classe que representa uma conta bancária sem encapsulamento.
    Todos os atributos são públicos.
    '''

    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def ver_saldo(self, senha_digitada):
        # Verifica se a senha está correta
        if senha_digitada == self.senha:
            print(f"Saldo de {self.titular}: R${self.saldo:.2f}")
        else:
            print("Senha incorreta! Acesso negado.")


# Teste
conta1 = ContaSemEncapsulamento("Sara", 1000.00, "1234")

# Consulta com senha correta
conta1.ver_saldo("1234")

# Alterando dados diretamente (problemas)
conta1.saldo = 999_999.99
conta1.senha = "0000"
conta1.titular = "Novo Titular"

# Consulta com a senha alterada indevidamente
conta1.ver_saldo("0000")
