'''
Listas em Python. Uma lista de coisas, não somente de strings. Um array do javascript ou uma matriz da matemática.
Tipo List -- Mutável.
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis: Índices e fatiamento.
Métodos úteis: append, insert, pop, del, clear, extend, +.

Create Read Uptade Delete (CRUD)
Criar, ler, atualizar, apagar = lista[i] (CRUD)
'''
lista = [10, 20, 30, 40];
lista[2] = 300;
print(lista);
del lista[2];
print(lista);
print(lista[2]); # Depois de deletar, a lista se reorganiza, juntamente com os seus índices. 
# Cuidado! Evite deletar elementos de listas muito grandes, para não fazer o python ter que mover muitos índices após um delete, usando muito processamento.
# É mais interessante adicionar e retirar elementos no final de uma lista, evitando esse cálculo pesado de rearranjo de índices.

lista.append(50);
print(lista);
lista.pop(); # Remove o último elemento da minha lista.
lista.append("60");
print(lista);
ultimo_valor = lista.pop() # Ele remove e retorna o último elemento da lista, pode ser útil saber disso.
print(lista, type(lista), ultimo_valor, type(ultimo_valor));

valor_x = lista.pop(1); # Remove e retorna o elemento presente no índice 1 da lista. 
# Novamente, cautela na hora de remover elementos no meio de uma lista gigante, para não travar o python.
print(lista, valor_x);

