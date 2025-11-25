🏦 Sistema Bancário em Python
Este projeto implementa um sistema bancário simples em Python, com funcionalidades de cadastro de usuários, abertura de contas correntes e operações financeiras básicas (depósitos, saques e extratos).
✨ Funcionalidades
- Cadastro de Usuário
- Armazena usuários em uma lista utilizando dicionários.
- Campos: nome, data de nascimento, CPF e endereço (logradouro, número, bairro, cidade/estado).
- O CPF é armazenado apenas com números e não permite duplicidade.
- Cadastro de Conta Corrente
- Armazena contas em uma lista.
- Cada conta possui: agência fixa (0001), número sequencial e CPF do usuário vinculado.
- Um usuário pode ter várias contas, mas cada conta pertence a apenas um usuário.
- Não é possível criar conta sem vincular a um usuário existente.
- Depósito
- Função recebe argumentos posicionais (saldo, valor, extrato).
- Atualiza saldo e extrato da conta.
- Apenas valores positivos são aceitos.
- Saque
- Função recebe argumentos nomeados (saldo=..., valor=..., extrato=..., limite=..., numero_saques=..., limite_saques=...).
- Regras:
- Não permite saque maior que o saldo.
- Não permite saque maior que o limite definido.
- Respeita o número máximo de saques por conta.
- Retorna saldo atualizado, extrato e número de saques.
- Extrato
- Exibe todas as movimentações da conta.
- Argumentos: saldo (posicional) e extrato (nomeado).
- Mostra saldo final e histórico de operações.
- Listagem de Contas
- Exibe todas as contas cadastradas com agência, número e CPF vinculado.
📋 Menu de Operações
O sistema é interativo e apresenta o seguinte menu:
[i] Cadastrar Usuário
[c] Cadastrar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Contas Correntes
[q] Sair


🚀 Como Executar
- Clone este repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
- Acesse a pasta do projeto:
cd seu-repositorio
- Execute o script:
python banco.py




