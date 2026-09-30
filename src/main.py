from cadastro import cadastrar_paciente

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

if __name__ == "__main__":
    escolher_opcao = menu_principal()

    lista_pacientes = []

    if escolher_opcao == 1:
        cadastro = cadastrar_paciente(lista_pacientes)

    print(lista_pacientes)

    