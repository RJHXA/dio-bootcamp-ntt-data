def withdrawal(balance, x):
    if balance - x > 0 and x > 0:
        return balance - x
    else:
        print(f'Saque Inválido, seu saldo R$ {balance:.2f}. Tente Novamente com outro valor!')


def deposit(balance, x, list):
    if x > 0:
        list.append(f'Depósito de {value:.2f}')
        return balance + x
    else:
        print("Você não pode depositar número igual ou abaixo de 0!")


def extract(balance, list):
    print("==== EXTRATO ====")
    for operation in list:
        print(operation)
    print(f'Saldo: R$ {balance:.2f}')


def create_user(users):
    cpf = input("Informe o CPF do usuário a ser criado: ")
    user = check_users(cpf, users)

    if user is None:
        name = input("Digite o nome do novo usuário: ")
        birthday = input("Digite a data de nascimentp do novo usuário (dd-mm-aaaa): ")
        address = input("Informe o endereço do novo usuário (rua, cidade, CEP): ")

        user_dict = {
            "nome": name,
            "data_nascimento": birthday,
            "cpf": cpf,
            "endereco": address
        }

        users.append(user_dict)
        print("Usuário criado com sucesso!")
    print("CPF ja cadastrado!")


def check_users(cpf, users):
    for user in users:
        if cpf == user.get("cpf", None):
            return user
    return None


def create_account(AGENCIA, num_account, users, accounts):
    cpf = input("Informe o CPF do usuário: ")
    user = check_users(cpf, users)

    if user:
        if check_accounts(cpf, user, accounts) is None:
            print("Conta criada com sucesso!")

            account_dict = {
                "agencia": AGENCIA,
                "numero_conta": num_account,
                "usuario": user
            }

            return account_dict
        else:
            print("Conta já cadastrada")

    print("Usuário não encontrado!")
    return None


def check_accounts(cpf, user, accounts):
    for account in accounts:
        if cpf == account.get("usuario", None).get("cpf", None):
            return account
    return None


def list_users(users):
    for user in users:
        print(f'| Nome: {user["nome"]} | Data Nascimento: {user["data_nascimento"]} | CPF: {user["cpf"]} | Endereço: {user["endereco"]} |')


def list_accounts(accounts):
    for account in accounts:
        print(f'| Agência: {account["agencia"]} | Número da Conta: {account["numero_conta"]} | Usuário: {account["usuario"]} |')


menu = '''
    [s] - saque
    [d] - depositar
    [e] - extrato
    [nu] - novo usuário
    [nc] - nova conta
    [lu] - listar usuários
    [lc] - listar contas
    [q] - exit

'''
LIMIT = 3
AGENCIA = "0001"

balance = 500
count_withdrawl = 0

extract_list = []
users = []
accounts = []

while True:

    option = input(menu)

    if option == 's':
        try:
            value = float(input("Saque!\nInforme quanto você quer sacar: "))
        except ValueError:
            value = -1

        if count_withdrawl < LIMIT and value < 500 and value > 0:
            result = withdrawal(balance, value)

            if result is not None:
                balance = result
                count_withdrawl += 1
                extract_list.append(f'Saque de {value:.2f}')
        else:
            print("Limite de Saque Exercido ou valor inválido (>0 & <500)")

    elif option == 'd':
        try:
            value = float(input("Depósito!\nInforme quanto você quer depositar: "))
        except ValueError:
            value = -1

        result = deposit(balance, value, extract_list)
        if result is not None:
            balance = result

    elif option == 'e':
        extract(balance, extract_list)

    elif option == 'nu':
        create_user(users)

    elif option == 'nc':
        num_account = len(accounts) + 1
        account = create_account(AGENCIA, num_account, users, accounts)

        if account:
            accounts.append(account)

    elif option == 'lu':
        list_users(users)

    elif option == 'lc':
        list_accounts(accounts)

    elif option == 'q':
        break

    else:
        print("Operação Inválido!")
