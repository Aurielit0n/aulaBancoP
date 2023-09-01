from banco import obterConta, banco

def transferir(contaOri:int,contaDes:int,valor:float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -=valor
            contaDestino['saldo'] +=valor
            print('transferencia realizada com sucesso!')
        else:
            print('saldo insuficiente')
    else:
        print('uma oumais contas não existem!')