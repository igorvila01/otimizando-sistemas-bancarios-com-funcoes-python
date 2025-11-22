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
- Numero da conta é sequncial e o numero da agencia é fixo "0001"
- O usuario pode ter mais de uma conta, mas uma conta pode pertencer a apenas um usuario 
- para vincular usuario a uma conta, filtre a lista de usuarios buscando pelo cpf informado para cada usuario da lista 
- Nao deixar criar conta sem vincular um usuario 
"""

import re

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    ...

def depositar(saldo, valor, extrato):
    ...

def extrato(saldo, extrato):
    ...

def cadastrar_usuario(nome, dt_nasc, cpf, endereco):
    usuario = {'nome': nome,
               'dt_nasc': dt_nasc, 
               'cpf': cpf,
               'endereco': endereco
               }
    return usuario

def cadastrar_cta_corrente():
    ...

def listar_contas():
    ...

def filtrar_num_str(numeros):
    numeros = re.sub(r'[^0-9]','', numeros)
    return numeros


menu = """
[i] Cadastrar Usuario
[c] Cadastrar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
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

            endereco = {
                'logradouro' : logradouro,
                'numero' : numero,
                'bairro' : bairro,
                'cidade_estado': cidade_estado
            }
            usuarios.append(cadastrar_usuario(nome, dt_nasc, cpf, endereco))
            break
    
    print(usuarios)




            
            


    