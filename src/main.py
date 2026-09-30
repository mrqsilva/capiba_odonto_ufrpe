from cadastro import cadastrar_paciente, listar_pacientes

def menu_principal() -> int:
    print("\n=======================")
    print("===* CAPIBA ODONTO *===")
    print("=======================")

    print("\n===  MENU INICIAL  ===")
    print("1- Cadastrar Paciente")
    print("2- Listar Pacientes")
    print("0- Sair do sistema")

    opcao = input("Digite o número da opção correspondente: ")

    try:
        return int(opcao)
    except ValueError:
        return -1

if __name__ == "__main__":
    lista_pacientes = []

    while True:
        try:
            escolher_opcao = menu_principal()
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo do sistema...")
            break

        if escolher_opcao == 1:
            try:
                cadastrar_paciente(lista_pacientes)
            except (EOFError, KeyboardInterrupt):
                print("\nOperação cancelada.")
                break
        elif escolher_opcao == 2:
            listar_pacientes(lista_pacientes)
        elif escolher_opcao == 0:
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Escolha uma opção válida.")
    