'''
3 Exercícios:
'''

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
] 

# O professor criou um package chamado "dados.py" com um módulo contendo essa lista e com o módulo "__init__.py" que importa essa lista de produtos, para deixar esse código mais 
# modularizado e conseguir realizar o import só do package e já conseguir acessar a lista de produtos..

'''
Aumente os preços dos produtos a seguir em 10%.
Gere novos_produtos por deep copy (cópia profunda). Dica: Utilize o módulo "copy"
'''
from copy import deepcopy; 

novos_produtos = deepcopy(produtos);

def aumentar_preco_10_por_cento(lista):
    for dicionario in lista:
        dicionario['preco'] = round(dicionario['preco'] * 1.10,2);

print(aumentar_preco_10_por_cento(novos_produtos));

print(f'{novos_produtos=}');
print();


#--------- Outra forma de fazer ---------#

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in deepcopy(produtos)
];

print(*produtos, sep='\n');
print();
print(*novos_produtos, sep='\n');

'''
Ordene os produtos por nome decrescente (do maior para o menor).
Gere produtos_ordenados_por_nome por deep copy (cópia profunda). Dica: Utilize "sorted" ou "nome_da_lista.sort".
'''

def ordena_nome(item):
    return item['nome'];

produtos_ordenados_por_nome = sorted(deepcopy(produtos),key=ordena_nome,reverse= True);
print(f'{produtos_ordenados_por_nome=}');

#--------- Outra forma de fazer ---------#

produtos_ordenados_por_nome = sorted(
    deepcopy(produtos),
    key=lambda p: p['nome'], reverse= True
);

print(*produtos, sep='\n');
print();
print(*produtos_ordenados_por_nome, sep='\n');

'''
Ordene os produtos por preço crescente (do menor para o maior).
Gere produtos_ordenados_por_preco por deep copy (cópia profunda).
'''

def ordena_nome(item):
    return item['preco'];

produtos_ordenados_por_preco = sorted(deepcopy(produtos),key=ordena_nome,reverse= False);
print(f'{produtos_ordenados_por_preco=}');

#--------- Outra forma de fazer ---------#

produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key=lambda p: p['preco'], reverse= False
);

print(*produtos, sep='\n');
print();
print(*produtos_ordenados_por_preco, sep='\n');
