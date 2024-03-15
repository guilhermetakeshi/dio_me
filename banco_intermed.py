def menu():
    options = """
    [c] Criar usuário
    [f] Filtrar usuário
    [a] Criar conta
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return options.strip()

def depositar(saldo, valor, extrato, **kwargs):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Novo saldo: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, numero_saques, **kwargs):
    limite = kwargs.get('limite', 500)
    LIMITE_SAQUES = kwargs.get('LIMITE_SAQUES', 3)
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Novo saldo: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato, **kwargs):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def criar_usuario(usuarios, **kwargs):
    # TODO: Adicionar lógica para criar um usuário
    novo_usuario = kwargs  # Adiciona o novo usuário com os dados fornecidos
    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista de usuários
    print("Usuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios, **kwargs):
    # TODO: Adicionar lógica para filtrar um usuário
    for usuario in usuarios:
        if usuario.get('cpf') == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, **kwargs):
    # TODO: Adicionar lógica para criar uma conta
    novo_conta = {'agencia': agencia, 'numero_conta': numero_conta}
    for usuario in usuarios:
        if usuario.get('cpf') == kwargs.get('cpf'):
            usuario.setdefault('contas', []).append(novo_conta)
            print("Conta criada com sucesso.")
            return
    print("Usuário não encontrado.")

def listar_contas(contas, **kwargs):
    # TODO: Adicionar lógica para listar contas
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print("Agência:", conta['agencia'], "- Número da conta:", conta['numero_conta'])

# As funções depositar, sacar e exibir_extrato permanecem as mesmas

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []  # TODO: Adicionar lógica para inicializar os usuários
    contas = []  # TODO: Adicionar lógica para inicializar as contas
    while True:
        opcao = input(menu())
        if opcao == "c":
            # TODO: Adicionar lógica para criar um usuário
            nome = input("Nome do usuário: ")
            cpf = input("CPF do usuário: ")
            criar_usuario(usuarios, nome=nome, cpf=cpf)
        elif opcao == "f":
            # TODO: Adicionar lógica para filtrar um usuário
            cpf = input("Informe o CPF do usuário que deseja filtrar: ")
            usuario_filtrado = filtrar_usuario(cpf, usuarios)
            if usuario_filtrado:
                print("Usuário encontrado:")
                print(usuario_filtrado)
            else:
                print("Usuário não encontrado.")
        elif opcao == "a":
            # TODO: Adicionar lógica para criar uma conta
            cpf = input("CPF do usuário para o qual deseja criar a conta: ")
            agencia = input("Agência da conta: ")
            numero_conta = input("Número da conta: ")
            criar_conta(agencia, numero_conta, usuarios, cpf=cpf)
        elif opcao == "l":
            # TODO: Adicionar lógica para listar contas
            listar_contas(contas)
        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite=limite)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    while True:
        opcao = input(menu())
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite=limite)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
