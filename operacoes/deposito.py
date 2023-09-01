from banco import obterConta, banco

def depositar(conta: int, valor:float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] = cliente ['saldo'] + valor
        print('Deposito realizado')
    else:
        print('cliente não existe')

print(banco)


if __name__ == '__main__':
    depositar(1,300)
    print(banco)
