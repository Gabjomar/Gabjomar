'''
List comprehension em Python.
Filtro de dados em list comprehension (filter).
Filtro de dados é criar um iterável novo a partir de um iterável existente escolhendo os valores que deseja incluir nesse novo iterável.

Obs.: É possível realizar um mapeamento e um filtro de dados de maneira simultânea, se desejado.
'''

import pprint; # Iremos utilizar esse módulo que juntamente com a criação de uma função irá facilitar a nossa vida nessa 
               # aula, porém haverão ainda aulas falando sobre import.

def p(v):
    pprint.pprint(v, sort_dicts=False, width=50); # pprint = prettier print

# O condicional relacionado com filtro de dados em list comprehension sempre aparece depois do for e é sempre somente um if, 
# sem else, diferente do bloco condicional relacionado com o mapeamento de dados em list comprehension que vimos na aula
# anterior.

p("Filtro de dados:");
lista = [
    n 
    for n in range(10)
    if n < 6 # Condicional relacionado com filtro de dados em list comprehension.
];
print(lista);

# Lembrando: No list comprehension, o que vem à esquerda do for é mapeamento de dados e o que vem à direita do for é filtro
# de dados.

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
];

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.15}
    if produto['preço'] < 20 else {**produto} # Até aqui é mapeamento de dados.
    for produto in produtos
    if (produto['preço'] * 1.05) < 20 # A partir daqui é filtro de dados.
];
p(novos_produtos);

# Obs.: Fazer list comprehension complexa não é uma boa prática de programação, não é porque está sendo apresentado nessas aulas que deve ser 
# utilizado em todos os casos, list comprehension é extremamente útil quando precisamos utilizar lógicas simples e desejamos ter um código mais 
# eficiente.