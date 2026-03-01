'''
List comprehension em Python.
Mapeamento de dados em list comprehension (map).

Já fizemos mapeamento de dados. Relembrando:
Mapear é pegar os dados de um iterável, processar/trabalhar com esses dados e sair com um novo iterável que possui o mesmo tamanho do primeiro
iterável.
'''

lista = [];
for numero in range(10):
    lista.append(numero);

print(f'{lista=}');

lista = [
    numero * 2
    for numero in range(10)
];

print(f'{lista=}');
print();
#  Acabou de ocorrer um mapeamento de dados.

# Mapeamento de dados em list comprehension:

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
];

novos_produtos = [produto for produto in produtos]; # Isso já é um mapeamento de dados, porém sem nenhuma modificação.
print(f'{novos_produtos=}');
print(*novos_produtos, sep='\n');
print();

novos_produtos = [produto['nome'] for produto in produtos];
print(f'{novos_produtos=}');
print(*novos_produtos, sep='\n');
print();

print("Aumentando o preço de cada produto em 10%:");
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.10}
    for produto in produtos
];
print(f'{novos_produtos=}');
print(*novos_produtos, sep='\n');

print();
print("Só irá aumentar em 15% os valores abaixo de 20:");
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.15}
    if produto['preço'] < 20 else {**produto} # Essa condicional para mapeamento de dados em list comprehension sempre será 
                                              # ternário, if-else, e antes do for.
    for produto in produtos
]; # Essa estrutura lógica do funcionamento da list comprehension pode parecer esquisita, mas se baseia no conceito básico e imutável de que o novo 
   # iterável terá o mesmo tamanho que o antigo, fazendo modificações apenas nos seus valores.
print(f'{novos_produtos=}');
print(*novos_produtos, sep='\n');

 # Se a partir da lógica do list comprehension o novo iterável, nesse caso a nova lista, não possuir o mesmo tamanho do iterável antigo, o código 
 # falha e ocasiona um erro, por conta do conceito básico de mapeamento de dados, por isso tem o "else {**produto}".