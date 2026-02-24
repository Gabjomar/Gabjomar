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
    + - Concatena listas. -> Mais um caso de polimorfismo do caractere "+", ou seja, dependendo do tipo de dado, o "+" faz algo diferente.

Create Read Uptade Delete (CRUD)
Criar, ler, atualizar, apagar = lista[i] (CRUD)
'''
lista_a = [10, 20, 30, 40];
lista_b = [50, 60, 70, 80];

lista_c = lista_a + lista_b;
print(lista_c);

lista_d = lista_a.extend(lista_b);
print(lista_d); # Método extend não retorna nada, ele opera no objeto que ele está atrelado em si. Nesse exemplo, na "lista_a".
print(lista_a); # Um método ou função não retornar nada signfica que ele faz alguma coisa mas não te entrega nada.


