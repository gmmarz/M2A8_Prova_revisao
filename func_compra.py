from func_auxiliares import (
    continuar_operacao,
    existe_produto_lista,
    pegar_produto_posicao_lista,
    aquisitar_numeros,
    calc_prod_total,
    calc_total_compra,
    imprimir_item
)

#Adcionar-ok
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
                if existe_produto_lista(prod_nome,lst_compra):
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

#ver list ok
def ver_lista_compra(lst_compra):
    print('-'*30)
    print('Itens compra')
    i = 1
    if len(lst_compra) ==0:
        print('Lista de compra está vazia')
    else:
        for item in lst_compra:
            print('*'*30)
            print(f'{i}º Item')    
            imprimir_item(item)
            i += 1

#atualizar ok
def atualizar_produtos(lst_compra:list)-> list:
    print('-'*30)
    print('Atualizar produtos')

    prod_dados = ['nome produto','valor','quantidade']
    prod_nome = ''
    flg_chg = True

    prod_nome = input('Digite nome produto para alterar: ')
    if existe_produto_lista(prod_nome, lst_compra):
        prod_pos = pegar_produto_posicao_lista(prod_nome,lst_compra)
        prod_inf = lst_compra[prod_pos].copy()
        i = 0
        while flg_chg:
            if i < 3:
                try:
                    flg_atualiza = int(input(f'Deseja atualizar {prod_dados[i]} (1)sim, (2)não , (3)abortar: '))
                    if flg_atualiza == 1:
                        match i:
                            case 0:
                                novo_nome = input('Digite o nome do produto: ').lower()
                                if len(novo_nome) < 1:
                                    print('Nome do produto deve ter mais que 1 caracter')
                            case 1:
                                novo_valor = aquisitar_numeros('Digite valor produto: ')
                                if novo_valor[0] == False:
                                    flg_atualiza = 3
                            case 2:
                                nova_qte = aquisitar_numeros('Digite a quantidade de produto: ')
                                if nova_qte[0] == False:
                                    flg_atualiza = 3
                        i +=1
                    elif flg_atualiza == 2:
                        match i:
                            case 0:
                                novo_nome = prod_nome
                            case 1:
                                novo_valor = prod_inf['valor']
                            case 2:
                                nova_qte = prod_inf['quantidade']
                        i +=1
                    elif flg_atualiza == 3:
                        print('Atualização de produto abortada')
                        flg_chg = False
                    else:
                        print('Digitar apenas (1)sim,(2)nâo e (3) para abortar')

                except ValueError:
                    print('Digite apenas 1 para sim\n 2 para não\n3 para abortar')

            else:
                flg_atualiza = 4 #Significa que a atualização foi concluida
                flg_chg = False
        if flg_atualiza == 4: #Alteração concluida
            novo_total = calc_prod_total(novo_valor[1],nova_qte[1])
            prod_inf.update({'produto': novo_nome,'valor':novo_valor[1],'quantidade':nova_qte[1],'total': novo_total})
            lst_compra[prod_pos] = prod_inf
            return lst_compra
    else:
        print('Produto desejado não existe na lista, escolha a opção adicionar')
        return lst_compra



