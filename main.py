from operacoes import consulta,saque,deposito,transferencia
from banco import *

def menu():
    while True:
        print("---- BEM VINDO AO MENU ----")
        print("1 - adicionar conta")
        print("2 -editar nome")
        print("3 - excluir conta")
        print("4 - consultar conta")
        print("5 - listar todas as contas")
        print("6 - consultar saldo ")
        print("7 - fazer deposito ")
        print("8 - fazer saque")
        print("9 - transferencia")
        print("10 - sair")
        opcao = int(input("selecione uma opção: "))
        if opcao == 1:
            nome = input("digite o nome do cliente:")
            saldo = float(input("digite o saldo:"))
            adicionarConta(nome,saldo)
        elif opcao ==2:
            nome = str(input("digite o novo nome: "))
            conta = int(input("digite o numero da conta: "))
            editarNome(nome,conta)
        elif opcao ==3:
            conta = int(input("digite o numero da conta: "))
            deletarConta(conta)
        elif opcao ==4:
            conta = int(input("Digite o numero da conta: "))
            consultarCliente(conta)
        elif opcao ==5:
            listarTodasContas()
        elif opcao ==6:
            conta = int(input("Digite o numero da conta: "))
            consulta.consultarSaldo(conta)
        elif opcao == 7:
            conta = int(input("Digite o numero da conta: "))
            valor = int(input("digite o valor: "))
            deposito.depositar(conta,valor)
        elif opcao ==8:
            conta = int(input("Digite o numero da conta: "))
            valor = int(input("digite o valor: "))
            saque.sacar(conta,valor)
        elif opcao == 9:
            contaOrig = int(input("Digite o numero da conta de origem: "))
            contaDest = int(input("Digite o numero da conta de destino: "))
            valor = int(input("digite o valor: "))
            transferencia.transferir(contaOrig,contaDest,valor)
        elif opcao == 10:
            print("---- VOCÊ SAIU DO PROGRAMA ----")
            break
menu()


