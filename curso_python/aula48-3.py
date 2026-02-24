'''
Listas em Python. Uma lista de coisas, não somente de strings. Um array do javascript ou uma matriz da matemática.
Tipo List -- Mutável.
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis: Índices e fatiamento.
Métodos úteis: 
    append - Adiciona um item ao final;
    insert - Adiciona um item no índice escolhido;
    pop -  Remove do final ou do índice escolhido;
    del - Apaga um índice;
    clear - Limpa a lista;
    extend - Estende a lista;
    + - Concatena listas.

Create Read Uptade Delete (CRUD)
Criar, ler, atualizar, apagar = lista[i] (CRUD)
'''
lista = [10, 20, 30, 40];

print(lista, lista.pop(), lista);

del lista[-1]; # Índice "-1" garante que sempre será o último item da lista. 

lista.insert(0, 5); # Entra o 5 no índice 0, logo o 5 fica no lugar do 10 e o 10 fica no lugar do 20 e por aí vai.
# Cuidado! Vale a mesma coisa do que o método pop, se fazer uma mudança no início em uma lista muito grande, pode deixar o código lento.
print(lista);
lista.insert(-1, 100);
print(lista);


