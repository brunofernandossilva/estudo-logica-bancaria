# Códigos de cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

menu = f"""
{BLUE}====================================
         BEM-VINDO AO BANCO
===================================={RESET}

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"
            print(f"{GREEN}✅ Depósito de R$ {valor:.2f} efetuado com sucesso!{RESET}")

        else:
            print(f"{RED}❌ Operação falhou! O valor informado é inválido.{RESET}")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"{RED}❌ Operação falhou! Você não tem saldo suficiente.{RESET}")

        elif excedeu_limite:
            print(f"{RED}❌ Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.{RESET}")

        elif excedeu_saques:
            print(f"{RED}❌ Operação falhou! Número máximo de saques diários excedido.{RESET}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"{GREEN}✅ Saque de R$ {valor:.2f} efetuado com sucesso!{RESET}")

        else:
            print(f"{RED}❌ Operação falhou! O valor informado é inválido.{RESET}")

    elif opcao == "3":
        print(f"{BLUE}============== EXTRATO BANCÁRIO =============={RESET}")
        print(f"{YELLOW}⚠️  Nenhuma movimentação realizada.{RESET}" if not extrato else extrato, end="")
        print(f"{GREEN}💰 Saldo disponível: R$ {saldo:.2f}{RESET}")
        print(f"{BLUE}=============================================={RESET}")

    elif opcao == "4":
        print(f"{YELLOW}👋 Obrigado por utilizar nossos serviços. Até mais!{RESET}")
        break

    else:
        print(f"{YELLOW}⚠️  Operação inválida, por favor selecione uma opção do menu.{RESET}")
