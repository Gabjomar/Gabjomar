'''
Listas em Python. Uma lista de coisas, não somente de strings. Um array do javascript ou uma matriz da matemática.
Tipo List -- Mutável.
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis: Índices e fatiamento.
Métodos úteis: append, insert, pop, del, clear, extend, +.

Create Read Uptade Delete (CRUD)
Criar, ler, atualizar, apagar = lista[i] (CRUD)
'''

#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres.

lista = []; # Uma lista vazia. É false, se converter para um tipo booleano.

print(lista, type(lista), bool(lista));

# Índices dos itens da lista:
#        +0    1       2            3     4(0)  4(1)
#        -5    -4     -3            -2    -1(-2) -1(-1) 
lista = [123, True, 'Luiz Otávio', 1.2, [123,'Luiz Otávio']];

print(lista);

print(lista[2], type(lista[2]));
print(lista[2].upper(), type(lista[2]));

# Por ser um tipo mutável, é possível fazer isso:
lista[2] = 123;

print(lista[2], type(lista[2]));



