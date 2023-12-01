from func_auxiliares import *


def adicionar_produtos(lst_compra:list)->list:
    print('-'*30)
    print('Adicionar produto na lista')
    novo_produto = {}
    prod_nome = ''
    valor = 0.0
    qte = 0
    total = 0.0
    flg_nome = 0
    flg_valor = 0
    flg_qte = 0

    while True:
        if flg_nome == 0:
            prod_nome = input('Digite o nome do produto: ').lower()
            if len(prod_nome)<1:
                print('Nome deve conter mais de 1 letra')
                flg_nome = -1
            else:
                if exite_produto_lista(prod_nome,lst_compra):
                    print('Produto já existe na lista')
                    flg_nome = -1
                else:
                    flg_nome = 1
                    break
        else:
            if not continuar_operacao():
                flg_nome = -1
                break
            else:
                flg_nome = 0
    
    if flg_nome == 1:
        flg_valor, valor = aquisitar_numeros('Digite o valor do produto: ')

    if flg_valor == 1:
        flg_qte, qte = aquisitar_numeros('Digite a quantidade de produto: ')
    
    if  flg_nome == 1  and flg_valor == 1  and flg_qte == 1:
        total = calc_prod_total(valor,qte)
        novo_produto = {'produto':prod_nome , 'valor': valor, 'quantidade':qte, 'total':total}
        lst_compra.append(novo_produto)
    else:
        print('Operação abortada pelo usuário')
    return lst_compra


compra = []

compra = adicionar_produtos(compra)

print(compra)
print(f'Valor total compra:{calc_total_compra(compra)}')


