
def verificar_acesso(cargo, dia_semana):
    cargo = cargo.lower()
    dia_semana = dia_semana.lower()

    
    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]


    if cargo == "gerente":
        return True
    elif cargo == "analista":
        return dia_semana in dias_uteis
    elif cargo == "estagiário":
        return dia_semana in dias_uteis
    else:
        return False


cargo = input("Digite o cargo do funcionário: ")
dia_semana = input("Digite o dia da semana: ")


if verificar_acesso(cargo, dia_semana):
    print("✅ Acesso permitido ao escritório.")
else:
    print("❌ Acesso negado ao escritório.")
