def continuar_operacao()-> bool:
    while True:
        flg_op = input(f'Deseja repetir a operação (s)sim, (n)não ? ').lower()
        match flg_op:
            case 's':
                return True
            case 'n':
                return False
            case _:
                print('Digite apenas "s" para sim ou "n" para não')

def exite_produto_lista(loc_prod:str, lst_compras:list)->bool:
    for item in lst_compras:
        if item['produto'] == loc_prod:
            return True
    return False   

'Recebe a pergunta para o usuário'
def aquisitar_numeros(pergunta:str):
    valor = 0.0
    flg = False
    while True:
        try:
            valor = float(input(f'{pergunta}'))
            flg = True
            break
        except ValueError:
            print('Digite apenas números')
            if not continuar_operacao():
                flg = False
                valor = 0.0
                break
    return flg,valor
 
def calc_prod_total(valor,qte):
    return valor*qte

def calc_total_compra(lst_compra:list)->float:
    total_compra = sum(item['total'] for item in lst_compra)
    return total_compra

def imprimir_item(item):
    print(f'Produto: {item["produto"]}')
    print(f'Valor: {item["valor"]}')
    print(f'Quantidade: {item["quantidade"]}')
    print(f'total: {item["total"]}')


if __name__ == '__main__':
    print('Este arquivo é um módulo e não deve ser executado diretamente')