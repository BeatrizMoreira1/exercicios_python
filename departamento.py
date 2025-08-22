
def verificar_acesso(cargo, dia):
    
    cargo = cargo.lower()
    dia = dia.lower()

    
    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

    
    if cargo == "gerente":
        return True
    elif cargo in ["analista", "estagiário"]:
        return dia in dias_uteis
    else:
        return False


cargo = input("Digite o cargo do funcionário: ")
dia = input("Digite o dia da semana: ")


if verificar_acesso(cargo, dia):
    print("✅ Acesso permitido ao escritório.")
else:
    print("❌ Acesso negado ao escritório.")
