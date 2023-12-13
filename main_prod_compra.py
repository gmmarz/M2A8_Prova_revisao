from func_compra import(
    adicionar_produtos,
    ver_lista_compra,
    atualizar_produtos,
    remover_produto
)

from func_auxiliares import calc_total_compra

def init():
    lst_compra = []
    flg_prog = True
    flg_oper = 0

    while flg_prog:
        print('-'*30)    
        try:
            print(
                'Digite a operação desejada:\
                \n1:Adicionar produto\
                \n2:Listar itens compra\
                \n3:Alterar produto\
                \n4:Remover produto\
                \n5:Finalizar programa'
                )
            flg_oper = int(input('Digite sua opção: '))
        except ValueError:
            print('Digitar apenas uma das opções indicadas')
            flg_oper = 0
        match flg_oper:
            case 1:
                lst_compra = adicionar_produtos(lst_compra)
            case 2:
                ver_lista_compra(lst_compra)
                print('='*10)
                print(f'Total compra = {calc_total_compra(lst_compra)}')
            case 3:
                lst_compra = atualizar_produtos(lst_compra)
            case 4:
                lst_compra = remover_produto(lst_compra)
            case 5:
                print('Lista compra finalizada\n')
                flg_prog = False

    if len(lst_compra) == 0:
        print("Programa abortado")
    else:
        ver_lista_compra(lst_compra)
        print('='*10)
        print(f'Total compra = {calc_total_compra(lst_compra)}')

if __name__ == "__main__":
    init()

