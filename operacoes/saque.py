from banco import obterConta, banco

def sacar(conta:int, valor: float):
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >=valor:
            cliente['saldo'] = cliente['saldo'] - valor
            print('saque realizado!')
        else:
            print('sem saldo')
    else:
        print('cliente n existe')

if __name__ == '__main__':
    sacar(1,150)
    print(banco)