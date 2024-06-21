# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Número sequencial de contas
numero_conta_sequencial = 1

def menu_principal():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar Usuário
    [a] Criar Conta
    [q] Sair

    => """
    return input(menu).strip().lower()

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário com este CPF.")
            return
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta(cpf):
    global numero_conta_sequencial
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            contas.append({
                'agencia': '0001',
                'numero_conta': numero_conta_sequencial,
                'usuario': usuario
            })
            numero_conta_sequencial += 1
            print("Conta criada com sucesso!")
            return
    print("Erro: Usuário não encontrado.")

# Variáveis globais para controle da conta corrente
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu_principal()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, valor=valor, extrato=extrato,
            limite=limite, numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, nro, bairro, cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "a":
        cpf = input("CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

