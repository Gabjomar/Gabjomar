'''
Sets (Conjuntos) - Conjuntos em Python (tipo set).

Operadores úteis:
união "|" (union) - Une os dois conjuntos, mantendo a característica do conjunto de não ter valores duplicados.

intersecção "&" (intersection) - Itens presentes em ambos os sets.

diferença "-" (difference) - Itens presentes apenas no conjunto da esquerda sem estarem presentes no conjunto da direita.

diferença simétrica "^" (symmetric_difference) - Itens que estão presentes em apenas um dos dois sets.

Obs.: Pode utilizar essas funções prontas como métodos, como "s1.union()", mas aqui iremos abordar elas como operadores.

É literalmente os mesmos conceitos presentes nos conjuntos matemáticos, só que aplicado no contexto da programação.
'''

s1 = {1, 2, 3};
s2 = {2, 3, 4};
exemplo_union = s1 | s2;
exemplo_intersection = s1 & s2;
exemplo_difference_1 = s1 - s2;
exemplo_difference_2 = s2 - s1;
exemplo_symmetric_difference = s1 ^ s2;
print(f'{exemplo_union=}'); # Lembre-se que não haverá valores duplicados, por isso é excluído automaticamente o valor 2 e 3 repetidos.
print(f'{exemplo_intersection=}');
print(f'{exemplo_difference_1=}');
print(f'{exemplo_difference_2=}');
print(f'{exemplo_symmetric_difference=}');