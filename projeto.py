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

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    ...

def depositar(saldo, valor, extrato):
    ...

def extrato(saldo, extrato):
    ...

def cadastrar_usuario():
    ...

def cadastrar_cta_corrente():
    ...

def listar_contas():
    ...
