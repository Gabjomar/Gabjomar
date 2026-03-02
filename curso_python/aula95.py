'''
isinstance() - "É instância de determinada classe?" - Para saber se o objeto é de determinado tipo.

Não é uma boa prática de programação ter uma lista mista, ou seja, com valores de diversos tipos, apesar de sabermos que haverá casos onde essa prática será inevitável. Mas de qualquer
forma, essa prática gera uma necessidade de utilizar alguma condição toda vez que for trabalhar com essa lista mista.
'''

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'},
];

for item in lista:
    if isinstance(item, set):
        item.add(5);
        print(item, isinstance(item, set));

    elif isinstance(item, str):
        # String é imutável, por isso precisa mudar a característica de item já quando for printar ele.
        print(item.upper(), isinstance(item, str));

    elif isinstance(item, (float, int)):
        print(item * 3);

    else:
        print('OUTRO');