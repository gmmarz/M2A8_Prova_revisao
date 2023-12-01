from func_compra import adicionar_produtos, ver_lista_compra,calc_total_compra
from func_auxiliares import continuar_operacao

lst_compra = []

while True:
    lst_compra = adicionar_produtos(lst_compra)

    if not continuar_operacao():
        break


ver_lista_compra(lst_compra)
print(f'Total compra = {calc_total_compra(lst_compra)}')
