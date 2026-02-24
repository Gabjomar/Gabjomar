'''
enumerate - enumera iteráveis (índices).
'''

lista = ['Maria', 'Helena', 'Luiz'];
lista.append('João');

lista_enumerada = enumerate(lista);
print(lista_enumerada, type(lista_enumerada));
print(next(lista_enumerada), type(next(lista_enumerada))); 
# A função enumerate transforma cada valor presente no objeto iterável em uma tupla onde o primeiro valor dessa tupla é o índice enumerado do valor e o 
# segundo é o valor original propriamente dito.

# Acessando cada item/valor do objeto enumerado a partir do for.
for item in lista_enumerada:
    print(item);

for item in lista_enumerada: # Não existe mais valor no enumerador, depois de apresentar ele uma vez. É um comportamento estranho no python.
    print(item);

# Para contornar isso, podes não atribuir o enumerate a nenhuma variável, que dai sempre inicia uma nova enumeração que aparenta não se esgotar.

for item in enumerate(lista):
    print(item);

# Ou você pode fazer uma coerção na variável na qual o enumerate foi atribuído para conseguir usar o objeto enumerado várias vezes.

lista_enumerada_1 = list(enumerate(lista));

for item in lista_enumerada_1:
    print(item);
print("ABC");

for item in lista_enumerada_1:
    print(item);

# A função enumerate possibilita a adição de outros parâmetros para modificar o funcionamento dela.
lista_enumerada_errada = enumerate(lista, start=100);
for item in lista_enumerada_errada:
    print(item);

for item in enumerate(lista): # Desempacotando o objeto enumerado.
    indice, nome = item;
    print(indice, type(indice), nome, type(nome));

for indice, nome in enumerate(lista): # Mesma coisa, só que economiza uma linha de código.
    print(indice, type(indice), nome, type(nome));

for tupla_enumerada in enumerate(lista): # Acessando cada valor individualmente do objeto enumerado, que nesse caso é uma lista enumerada.
    print('FOR da tupla: ');
    for valor in tupla_enumerada:
        print(f'\t{valor}'); # "\t" é o tab.
