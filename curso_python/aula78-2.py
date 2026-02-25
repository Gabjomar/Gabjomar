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
    'sobrenome': 'Miguel',
    'idade': 26
}

print("get:");
print(pessoa.get("sobrenome"));
print(pessoa.get("Graduação")); # Quando não encontra a chave, por padrão retorna "None".
print(pessoa.get("Graduação", "Não existe"));

print("pop:");
print(pessoa.pop("sobrenome")); # Apaga a chave e valor especificado e retorna a chave apagada.
print(f"{pessoa=}");

print("popitem:");
ultima_chave_apagada = pessoa.popitem(); # Apaga a última chave e valor e retorna a chave apagada.
print(ultima_chave_apagada);
print(f"{pessoa=}");

print("update:"); # Adiciona/atualiza chaves e valores especificados sem modificar as chaves e valores existentes.
# Existem duas formas de estruturar os dados que desejas atualizar no método update:
# 1ª forma:
pessoa.update({
    'idade': 72,
});
print(f"{pessoa=}");

# 2ª forma:
pessoa.update(nome = 'Novo valor', idade = 29); # Perceba que você não precisa colocar as aspas para indicar nas chaves que é uma string e que é
                                                # utilizado o igual ao invés dos dois pontos.
print(f"{pessoa=}");

# Também é possível atualizar as chaves e valores com tuplas e listas. Precisam ser tuplas/listas com tuplas/listas dentro de cada valor da 
# tupla/lista, ou seja, uma variável do tipo iterável que está se comportando como um dicionário, possuindo a mesma estrutura que um dicionário, um
# iterável que tem dentro dele outro iterável que tem dois valores que se tornam a chave e o valor.
tupla = ('chave_genérica', 'valor_genérico'), ('chave_genérica_123', 'valor_genérico_123');
pessoa.update(tupla);
print(f"{pessoa=}");

tupla_1 = ('chave_genérica', True),; # Mesmo que queira atualizar apenas um par de chave e valor, precisa ter a vírgula para o Python
                                                 # entender que é uma tupla com tuplas dentro dela para que seja possível realizar o update dessa
                                                 # forma.
pessoa.update(tupla_1);
print(f"{pessoa=}");