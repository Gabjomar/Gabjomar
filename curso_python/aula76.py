'''
Dicionários em Python (tipo dict).

Dicionários são estruturas de dados do tipo par de "chaves" e "valor".

Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.

Valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.

--- Lembrete ---
Imutáveis: str, int, float, bool, tuple.
Mutáveis: dict, list.
'''
pessoa = {
    'nome': 'Luiz', # Chave do tipo str e valor do tipo str.
    'sobrenome': 'Miguel',
    'idade': 26, # Chave do tipo str e valor do tipo int.
    'altura': 1.89, # Chave do tipo str e valor do tipo float.
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 42},
        {'rua': 'abc abc', 'número': 65}
    ] # Chave do tipo str e valor do tipo list com um valor do tipo dict dentro dele.
}

print(pessoa, type(pessoa));

print(pessoa['idade'], type(pessoa['idade']));

# Mostrando que é possível fazer essa varredura dos dados com loops iteráveis:
for chave in pessoa:
    print(chave);
    print(pessoa[chave]);


pessoa_1 = dict(); # "dict()" pode ser útil para quando queremos criar uma variável vazia do tipo dicionário, mas é pouco utilizado no geral.

print(pessoa_1, type(pessoa_1));



