import textwrap

# Códigos de cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def menu():
    menu = f"""
    {BLUE}====================================
         BEM-VINDO AO BANCO
    ===================================={RESET}

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair

    => """
    return input(textwrap.dedent(menu))

#Se o valor for maior ou igual a zero, soma saldo+valor e extrato computa a mensagem "depósito saldo+= valor" 
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print(f"\n{GREEN}=== DEPÓSITO REALIZADO COM SUCESSO! ==={RESET}")
    else:
        print(f"{RED}\n!!! OPERAÇÃO FALHOU! O VALOR INFORMADO É INVÁLIDO. !!!{RESET}")
    
    return saldo, extrato

#Neste caso os ifs tomaram decisões que negam o saque por falta de saldo, limite ou saques diarios. Foi definida as condições do "excedeu_..."
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"\n{RED}!!! OPERAÇÃO FALHOU! SALDO INSUFICIENTE. !!!{RESET}")
        
    elif excedeu_limite:
        print(f"\n{RED}!!! OPERAÇÃO FALHOU! LIMITE INSUFICIENTE. !!!{RESET}")

    elif excedeu_saques:
        print(f"\n{RED}!!! OPERAÇÃO FALHOU! LIMITE DE SAQUE DIÁRIO EXCEDIDO!!!{RESET}")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n{GREEN}=== SAQUE REALIZADO COM SUCESSO! ==={RESET}")
    else:
        print(f"\n{RED}!!! OPERAÇÃO FALHOU! O VALOR INFORMADO É INVÁLIDO!!!{RESET}")

#o que é alterado dentro de uma função permanece somente lá por meio de indentação, e o return seria para "atualizar os valores"
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"\n{YELLOW}================ EXTRATO ================\n{RESET}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(f"{YELLOW}=========================================={RESET}")

#é criado uma função chamada criar_usuario e vincula uma lista "usuarios" que é alimentada por meio do usuarios.append, que possui os inputs nome, data_nasimento e endereço.
def criar_usuario(usuarios):
    cpf = input('Informa o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{RED}@@@ Já existe usuário com esse CPF! @@@{RESET}")
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"{GREEN}=== USUÁRIO CRIADO COM SUCESSO ==={RESET}")

#filtrar_usuario recebe 2 parametros para ser analisados para cada usuario é verificado o CPF, se for igual, adiciona na lista de usuarios filtrados.
#Se a lista usuarios_filtrados não estiver vazia, retorna o primeiro item (ou seja, o usuário encontrado). Se se não, retorna "None"
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#a função criar_conta recebe os dados de agencia, numero_conta e usuarios, quando é colocado o CPF ele passa pelo filtro criado acima, se usuario == true responde "contra criada com sucesso" e no return armazena os dados, se não "usuario nao encontrado"
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{GREEN}=== CONTA CRIADA COM SUCESSO! ==={RESET}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print(f"\n{RED}!!! USUÁRIO NÃO ENCONTRADO, FLUXO DE CRIAÇÃO ENCERRADO !!!{RESET}")

#A função listar_contas(contas) recebe uma lista de contas e imprime as informações de cada uma de forma formatada e alinhada visualmente no terminal. O comando textwrap remove espaços em excesso no início das linhas, que aparecem por causa da indentação do código
def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(f'{YELLOW}{"=" * 100}{RESET}')
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

# Menu interativo rodando em loop infinito
# Cada opção executa uma parte do sistema bancário
# Usa funções para organizar o código e evitar repetições
# As variáveis como saldo, usuarios, contas vão sendo atualizadas conforme as operações
# Só encerra quando o usuário escolhe sair
    while True:
# Laço principal do sistema
        opcao = menu()
#o sistema pede o valor do deposito, no input o valor é digitado e o float leva para casas decimais. Chama a função "depositar passando 3 coisas (valor, saldo, extrato), "
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

#Você envia os valores atuais (saldo, extrato, etc.) para a função, ela processa e devolve os valores atualizados. Esses valores retornam e substituem os antigos no programa principal.       
        elif opcao == "2":
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print(f"{YELLOW}\n>>> Obrigado por usar o nosso sistema! <<<\n{RESET}")
            break
        
        else:
            print(f"{RED}Operação inválida, por favor selecione novamente a operação desejada.{RESET}")

main()
