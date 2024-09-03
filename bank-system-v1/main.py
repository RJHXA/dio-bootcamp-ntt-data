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


menu = '''
    [s] - saque
    [d] - depositar
    [e] - extrato
    [q] - exit

'''
LIMIT = 3
balance = 500
count_withdrawl = 0
extract_list = []

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

    elif option == 'q':
        break

    else:
        print("Operação Inválido!")