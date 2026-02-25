'''
Métodos úteis dos dicionários em Python.
len - quantas chaves; -> Não é um método, é um thunder (todo thunder começa e termina com dois underscores/underlines)
keys - iterável com as chaves;
values - iterável com os valores;
items - iterável com chaves e valores;
setdefault - adiciona valor se a chave não existe;
copy - retorna uma cópia rasa (shallow copy);
get - obtém uma chave;
pop - apaga um item com a chave especificada (del);
popitem - apaga o último item adicionado;
update - atualiza um dicionário com outro.
'''

pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Adolf',
    'sobrenome': 'Miguel',  # Quando se cria chaves com nomes iguais, o que será considerada será a última chave com nome igual apresentada, pois o 
                            # interpretador vai sobrescrevendo o valor presente naquela chave nesse caso, a chave sobrenome com valor "Miguel". 
                            # O interpretador nem considera as outras chaves com nomes iguais, como podemos ver na função len().
    'idade': 26
}

print("len:");
print(pessoa.__len__());
print(len(pessoa)); # Função que faz a mesma coisa que esse thunder, só que é mais simples de usar e escrever.

print("keys:");
print(pessoa.keys(), type(pessoa.keys()));
print(list(pessoa.keys())); # Geralmente você irá querer fazer uma coerção de tipos quando utilizar esse método, pois o tipo de valor que vem padrão
                            # não é muito utilizado.

print("values:");
print(pessoa.values(), type(pessoa.values()));
# Geralmente você irá querer fazer uma coerção de tipos quando utilizar esse método, pois o tipo de valor que vem padrão não é muito utilizado.
print(list(pessoa.values()));

# Uma das utilidades:
for valor in pessoa.values():
    print(valor);

print("items:");
print(pessoa.items(), type(pessoa.items()));
print(list(pessoa.items())); # Gera uma lista com cada valor da lista sendo uma tupla contendo a chave e o valor do dicionário.
# Geralmente você irá querer fazer uma coerção de tipos quando utilizar esse método, pois o tipo de valor que vem padrão não é muito utilizado.

print("setdefault:");
pessoa.setdefault("Altura", "Não informada");
print(pessoa);


