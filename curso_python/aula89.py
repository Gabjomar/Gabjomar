'''
Empacotamento e desempacotamento de dicionários + *args e **kwargs.

args - já vimos.
kwargs - Keyword arguments (argumentos nomeados).
'''

# Relembrando:
a, b = 1, 2;
a, b = b, a;

print(a, b);

pessoa = {
    'nome': 'Alice',
    'sobrenome': 'Miranda',
};

print();
print("Sem método:");
c, d = pessoa; # Sem o método values por padrão o desempacotamento irá entregar as chaves do dict.
print(f'{c=}, {d=}');

print();
print("values:");
a, b = pessoa.values();
print(f'{a=}, {b=}');

print();
print("items:"); # Entrega cada um dos pares de chave e valor como tuplas. 
a, b = pessoa.items();
print(f'{a=}, {b=}');
(a1, a2), b = pessoa.items(); # O interessante é que é possível fazer empacotamento e desempacotamento interno.
print(f'{a1=}, {a2=}, {b=}');
(a1, a2), (b1, b2) = pessoa.items();
print(f'{a1=}, {a2=}, {b1=}, {b2=}');

print();
for chave, valor in pessoa.items():
    print(chave, valor);

### - ### - ### - ### - ### - ###
# *args e **kwargs

pessoa = {
    'nome': 'Alice',
    'sobrenome': 'Miranda',
};

dados_pessoa = {
    'idade': 20,
    'altura': 1.90,
}

print();
print(f"{pessoa=}, {dados_pessoa=}");

pessoa_completa = {**pessoa, **dados_pessoa, 'nova_chave': 1,}; 
# Desempacotamento de dicionários ocorre com "**". Aqui ocorre o desempacotamento de outros dicionários e a adição de novas chaves e valores para 
# criar um novo dicionário.
print(f'{pessoa_completa=}');

# Sempre que trabalhar com kwargs, é necessário utilizar "**".
def mostro_argumentos_nomeados(*args, **kwargs):
    print(f'{kwargs=}');

mostro_argumentos_nomeados(nome = "Joana", qualquer = 123);

print();
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Argumentos não nomeados serão atribuídos ao parâmetro "args" por conta do "*":', args)
    for chave, valor in kwargs.items():
        print(f'{chave=}, {valor=}');

mostro_argumentos_nomeados("Argumento_não_nomeado", nome = "Felipe", qualquer = False);

# Utilizando essa estruturação dos parâmetros, os argumentos não nomeados são atribuídos aos parâmetros "args", por conta do asterisco simples "*" e 
# os argumentos nomeados são atribuídos aos parâmetros "kwargs" por conta do duplo asterisco "**".

print("Desempacotando por meio de kwargs:");
print();
mostro_argumentos_nomeados(**pessoa_completa); 
# Desempacotando uma chamada de função passando os argumentos, útil em casos onde você tem que chamar uma função com muitos argumentos e você não 
# quer escrever na unha em cada chamada da função cada um dos argumentos, dai você pode criar um dicionário com os argumentos que você deseja 
# utilizar nas suas funções. Segue um exemplo:

configuracoes = {
    'arg_1': 1,
    'arg_2': False,
    'arg_3': 3.2,
    'arg_4': "Everaldo",
};
print();
print("Configurações:");
mostro_argumentos_nomeados(**configuracoes);