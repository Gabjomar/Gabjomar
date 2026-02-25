'''
Manipulando chaves (keywords) e valores (values) em dicionários.
'''
pessoa = {};

print(pessoa);

# Pode ir adicionando ou modificando as chaves e valores presentes em um dicionário existente.

pessoa['nome'] = 'Gabriel';

print(pessoa);

# A diferença entre índice de uma lista e chave é que índice é sempre um número crescente, enquanto chave é qualquer tipo imutável sem ordem 
# definida.



chave = 'idade'; # É possível criar chaves dinâmicas
pessoa[chave] = 20;

print(pessoa, pessoa[chave]);

# É possível substituir o valor:

pessoa['nome'] = "Guilherme";

print(pessoa, pessoa["nome"]);

# É possível apagar chaves e valores:

del pessoa["nome"];
print(pessoa);

# É possível verificar a existência de chaves e valores com o método "get":

print(pessoa.get(chave));
print(pessoa.get("nome")); # Por padrão, quando tenta pegar o valor de uma chave que não existe, ele retorna "None".
print(pessoa.get("nome", None));

if pessoa.get("nome") is None:
    print("Não existe");
else:
    print(pessoa("nome"));


