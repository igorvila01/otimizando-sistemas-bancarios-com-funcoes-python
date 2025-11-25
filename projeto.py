"""
Função de saque deve conter as seguintes regras:
- Essa função deve receber os argumentos keyword only ou seja saldo=<nome_variavel>
- conter os argumentos saldo, valor, extrato, limite, numero_saques, limite_saques
- deve retornar saldo e extrato 

Função de deposito deve conter as seguintes regras:
- Essa função deve receber argumentos posicionais
- conter os argumentos saldo, valor, extrato
- deve retornar saldo e extrato 

Função de extrato deve conter as seguintes regras:
- conter os argumentos saldo, extrato
- Essa função deve receber argumentos posicionais no argumento saldo e nomeado no extrato

Função de cadastro de usuario:
- Armazenar o usuario em uma lista e utilizar dicionarios 
- nome, data de nascimento, cpf e endereco (formato <logradouro, numero, bairro, cidade/sigla estado>)
- cpf deve ser armazenado somente numeros e nao podemos cadastrar 2 usuarios com o mesmo cpf (cpf é string)

Funcao de cadastrar conta corrente 
- Deve armazenar contas em uma lista 
- é composta por agencia, numero da conta e usuario 
- Numero da conta é sequencial e o numero da agencia é fixo "0001"
- O usuario pode ter mais de uma conta, mas uma conta pode pertencer a apenas um usuario 
- para vincular usuario a uma conta, filtre a lista de usuarios buscando pelo cpf informado para cada usuario da lista 
- Nao deixar criar conta sem vincular um usuario 
"""

import re

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}\n")
        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso.")
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("Valor inválido para depósito.")
    else:
        saldo += valor
        extrato.append(f"Depósito: +R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    return saldo, extrato


def extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print('Não foram realizadas movimentações.')
    else:
        for i in extrato:
            print(i)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(nome, dt_nasc, cpf, logradouro, numero, bairro, cidade_estado):
    usuario = {'nome': nome,
               'dt_nasc': dt_nasc, 
               'cpf': cpf,
               'endereco' : {
                            'logradouro' : logradouro,
                            'numero' : numero,
                            'bairro' : bairro,
                            'cidade_estado': cidade_estado
                            }
               }
    return usuario

def cadastrar_cta_corrente(cpf, cc):
    conta_corrente = {
        'ag' : '0001',
        'cc' : cc,
        'cpf' : cpf,
        'saldo' : 0.0,
        'extrato': [],
        'numero_saques': 0
    }
    return conta_corrente

def listar_contas():
    print("\n================ CONTAS CADASTRADAS ================")
    for i in range(len(contas)):
        print(f"Agência: {contas[i]['ag']}  |  Conta: {contas[i]['cc']}  |  CPF: {contas[i]['cpf']}")

    print("\n====================================================")

def filtrar_num_str(numeros):
    numeros = re.sub(r'[^0-9]','', numeros)
    return numeros


menu = """
[i] Cadastrar Usuario
[c] Cadastrar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar conta corrente
[q] Sair

=> """


limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "i":
        while True:
            cpf = filtrar_num_str(input('CPF do usuario: '))
            if len(cpf) != 11:
                print('CPF Invalido!')
                continue  

            cont_cpf = 0

            if len(usuarios) > 0:                
                for i in range(len(usuarios)):
                    if usuarios[i]['cpf'] == cpf:
                        cont_cpf += 1
                        break
            
            if cont_cpf > 0:
                print('CPF ja cadastrado!')   
                break                  
            
            nome = input('Nome do usuario: ')
            dt_nasc = input('Data de nascimento: ')
            logradouro = input('Logradouro: ')
            numero = input('Numero: ')
            bairro = input('Bairro: ')
            cidade = input('Cidade: ')
            sigla_estado = input('Sigla estado: ')

            cidade_estado = f'{cidade}/{sigla_estado}'

            usuarios.append(cadastrar_usuario(nome, dt_nasc, cpf, logradouro, numero, bairro, cidade_estado))
            break
    
    elif opcao == 'c':
        while True:
            cpf = filtrar_num_str(input('CPF do Usuario: '))

            if len(cpf) != 11:
                print('CPF Inválido! ')
                continue            
            
            contar = 0
            for i in range(len(usuarios)):
                cpf_atual = usuarios[i]['cpf']
                if cpf_atual == cpf:
                    contar +=1
            
            if contar > 0:
                cc = len(contas) + 1                
            else:
                print('Usuario nao possui cadastro, voltando ao menu anterior para efetuar cadastro!')
                break

            contas.append(cadastrar_cta_corrente(cpf, cc))
            print(f'Conta Corrente: {contas[cc-1]['cc']} \nAgencia: {contas[cc-1]['ag']}')
            break

    elif opcao == 'd':
        while True:
            conta_atual = int(input('Digite o numero da conta:'))
            
            conta_encontrada = None
            for verifica in contas:
                if verifica['cc']==conta_atual:
                    conta_encontrada = verifica
                    break
            
            if not conta_encontrada:
                print('Conta não encontrada!')
                continue

            break

        while True:
            try:
                valor = float(input("Informe o valor do depósito: "))
                break                    
            except ValueError:
                print('O Valor informado é inválido!')
                continue     

        saldo_conta = conta_encontrada['saldo']
        extrato_conta = conta_encontrada['extrato']

        saldo_atual, extrato_atual = depositar(saldo_conta, valor, extrato_conta)
        conta_encontrada['saldo'] = saldo_atual
        conta_encontrada['extrato'] = extrato_atual
   
    elif opcao == 'e':
        while True:
            conta_atual = int(input('Digite o numero da conta:'))
            
            conta_encontrada = None
            for verifica in contas:
                if verifica['cc']==conta_atual:
                    conta_encontrada = verifica
                    break
            
            if not conta_encontrada:
                print('Conta não encontrada!')
                continue

            break

        extrato(conta_encontrada['saldo'], extrato=conta_encontrada['extrato'])

    elif opcao == 'q':
        break

    elif opcao == 's':
        while True:
            conta_atual = int(input('Digite o numero da conta:'))
            
            conta_encontrada = None
            for verifica in contas:
                if verifica['cc']==conta_atual:
                    conta_encontrada = verifica
                    break
            
            if not conta_encontrada:
                print('Conta não encontrada!')
                continue

            break

        while True:
            try:
                valor = float(input("Informe o valor do Saque: "))
                break                    
            except ValueError:
                print('O Valor informado é inválido!')
                continue 

        saldo_conta = conta_encontrada['saldo']
        extrato_conta = conta_encontrada['extrato']
        saques_conta = conta_encontrada['numero_saques']

        saldo_atual, extrato_atual, saques_atual = sacar(saldo=saldo_conta, 
                                           valor=valor, 
                                           extrato=extrato_conta, 
                                           limite=limite, 
                                           numero_saques=saques_conta, 
                                           limite_saques=LIMITE_SAQUES )
        conta_encontrada['saldo'] = saldo_atual
        conta_encontrada['extrato'] = extrato_atual 
        conta_encontrada['numero_saques'] = saques_atual

    elif opcao == 'l':
        listar_contas()

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    
    
