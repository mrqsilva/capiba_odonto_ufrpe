def menu_principal() -> int:
    print("=======================")
    print("===* CAPIBA ODONTO *===")
    print("=======================")

    print("\n===  MENU INICIAL  ===")
    print("1- Cadastrar Paciente")
    print("2- Listar Pacientes")
    print("0- Sair do sistema")

    opcao = input("Digite o número da opção correspondente: ")

    return int(opcao)

def cadastrar_paciente(lista_pacientes: list) -> list[dict]:
    ficha_paciente = {}

    print("="*42)
    print("\nCADASTRO DE PACIENTE")
    nome_paciente = input("Nome do paciente: ")
    ficha_paciente["nome_paciente"] = nome_paciente

    cpf_paciente = input("Número de CPF: ")
    ficha_paciente["cpf"] = cpf_paciente

    data_nascimento = input("Informe data de nascimento (XX/XX/XXXX): ")
    ficha_paciente["data_nascimento"] = data_nascimento

    contato_principal = input("Número celular com DDD: ")
    ficha_paciente["contato_principal"] = contato_principal

    contato_emergencia = input("Contato de emergência (nome/grau/contato): ")
    ficha_paciente["contato_emergencia"] = contato_emergencia

    lista_pacientes.append(ficha_paciente)

    return lista_pacientes

# def cadastrar_anamnese_inicial():
#     print("Formulário de saúde")
#     alergias = input("Possui alguma alergia medicamentosa (s/n)? ")
#     if alergias == "s":
#         input("Informe o nome do fármaco: ") 
#     else:
#         pass

#     cirurgias_previas = input("Já realizou alguma cirurgia (s/n)? ")
#     if cirurgias_previas == "s":
#         nome_cirurgia = input("Informe o nome da cirurgia: ")
#     else: 
#         pass

#     medicamentos_continuos = input("Faz uso de alguma medicação contínua (s/n)? ")

#     if medicamentos_continuos == "s":
#         nome_medicamento_continuo = input("Informe o nome do medicamento: ")
#     else:
#         pass

# def listar_pacientes(lista_pacientes):
#     for paciente in lista_pacientes: 
#         ...

if __name__ == "__main__":
    escolher_opcao = menu_principal()

    lista_pacientes = []

    if escolher_opcao == 1:
        cadastro = cadastrar_paciente(lista_pacientes)

    