'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''
import os;

lista_de_compras = [];

while True:
    escolha = input(f'Selecione uma opção\n[i]nserir [a]pagar [l]istar: ').lower();
    if escolha == "i":
        os.system('cls');
        valor_escolhido = input('Valor: ');
        lista_de_compras.append(valor_escolhido);
    elif escolha == "a":
        indice_escolhido = input('Escolha o índice para apagar: ');
        if indice_escolhido.isdigit():
            indice_escolhido_int = int(indice_escolhido);
            if indice_escolhido_int <= (len(lista_de_compras)):
                lista_de_compras.pop(indice_escolhido_int);
                print(f"Valor do índice {indice_escolhido_int} foi removido.");
            else:
                print("Não foi possível apagar este índice.");
        else:
            print("Você deve digitar um número válido!");
            continue;
    elif escolha == "l":
        os.system('cls');
        for indice, compra in enumerate(lista_de_compras):
            print(indice, compra);
    else:
        print('Digite uma das opções acima!');
        continue;