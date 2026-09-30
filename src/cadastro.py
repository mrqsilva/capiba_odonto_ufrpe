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

    ficha_paciente["anamnese"] = cadastrar_anamnese_inicial()

    ficha_paciente["assinatura_tcle"] = coletar_assinatura_tcle()

    lista_pacientes.append(ficha_paciente)

    return lista_pacientes

def cadastrar_anamnese_inicial() -> dict:
    anamnese = {}

    print("\n" + "="*42)
    print("FORMULÁRIO DE SAÚDE (ANAMNESE INICIAL)")
    print("="*42)

    alergias = input("Possui alguma alergia medicamentosa (s/n)? ").strip().lower()
    if alergias == "s":
        anamnese["alergia_medicamentosa"] = input("Informe o nome do fármaco: ").strip()
    else:
        anamnese["alergia_medicamentosa"] = "Não possui"

    cirurgias_previas = input("Já realizou alguma cirurgia (s/n)? ").strip().lower()
    if cirurgias_previas == "s":
        anamnese["cirurgias_previas"] = input("Informe o nome da cirurgia: ").strip()
    else: 
        anamnese["cirurgias_previas"] = "Não possui"

    medicamentos_continuos = input("Faz uso de alguma medicação contínua (s/n)? ").strip().lower()
    if medicamentos_continuos == "s":
        anamnese["medicamentos_continuos"] = input("Informe o nome do medicamento: ").strip()
    else:
        anamnese["medicamentos_continuos"] = "Não possui"

    return anamnese

def coletar_assinatura_tcle(ficha_paciente: dict | None = None) -> bool:
    print("\n" + "="*42)
    print("TERMO DE CONSENTIMENTO LIVRE E ESCLARECIDO (TCLE)")
    print("="*42)

    resposta = input("O paciente realizou a assinatura do termo de consentimento (TCLE) (s/n)? ").strip().lower()
    assinado = resposta in ("s", "sim")

    if ficha_paciente is not None:
        ficha_paciente["assinatura_tcle"] = assinado

    return assinado

def listar_pacientes(lista_pacientes: list) -> None:
    if not lista_pacientes:
        print("\nNenhum paciente cadastrado.")
        return

    print("\n" + "="*42)
    print("LISTA DE PACIENTES")
    print("="*42)
    for indice, paciente in enumerate(lista_pacientes, start=1):
        print(f"\n--- Paciente #{indice} ---")
        print(f"Nome: {paciente.get('nome_paciente')}")
        print(f"CPF: {paciente.get('cpf')}")
        print(f"Data de Nascimento: {paciente.get('data_nascimento')}")
        print(f"Contato: {paciente.get('contato_principal')}")
        print(f"Contato de Emergência: {paciente.get('contato_emergencia')}")

        anamnese = paciente.get("anamnese", {})
        if anamnese:
            print("Anamnese:")
            print(f"  - Alergia medicamentosa: {anamnese.get('alergia_medicamentosa', 'Não informado')}")
            print(f"  - Cirurgias prévias: {anamnese.get('cirurgias_previas', 'Não informado')}")
            print(f"  - Medicamentos contínuos: {anamnese.get('medicamentos_continuos', 'Não informado')}")
        else:
            print("Anamnese: Não informada")

        status_tcle = "Sim" if paciente.get("assinatura_tcle") else "Não"
        print(f"Assinatura do TCLE: {status_tcle} ({paciente.get('assinatura_tcle')})")
