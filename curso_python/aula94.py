'''
Dictionary comprehension e set comprehension.

Tudo que vimos em list comprehension se aplica para dictionary comprehension e set comprehension.
'''

produto = {
    'nome': 'Caneta',
    'cor': 'Azul',
    'preco': 2.5,
    'categoria': 'escritório',
};

# Dictionary comprehension - Cuidado para não acabar criando um set comprehension quando for escrever o código.
dictionary_comprehension = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # Irá colocar o valor em letra maiúscula se o valor for uma string. No "isinstance", se quiseres verificar mais de um tipo, use uma tupla.
    for chave, valor
    in produto.items()
    if chave != 'categoria'
};

print(f'{dictionary_comprehension=}');

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
];

dictionary_comprehension_1 = {
    chave: valor
    for chave, valor in lista
}; # Criando um dicionário a partir de uma lista que parece/está estruturada como um dicionário.

print(f'{dictionary_comprehension_1=}');


#-#-#-#-#-#-#-#-#-#-#-#-#-#-

set_comprehension = {i ** 2 for i in range(15)};

print(f'{set_comprehension=}', type(set_comprehension));
