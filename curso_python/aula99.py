'''
Generator expression, Iterables e Iterators em Python.

Generator expression (expressão gerador) - São basicamente funções/expressões que sabem pausar. Não salva todos os valores de cara na memória, ele só te entrega e 
salva um valor por vez, só sabe o próximo valor, por isso ele é um iterator, mas nem todo iterator é um generator. É útil quando você precisa navegar por valores um 
por um.

"Todo generator é um iterator, mas nem todo iterator é um generator."

Generator tem desvantagens, pois não tem diversos benefícios que as listas trazem, como por exemplo, conseguir acessar o valor de determinado índice específico, saber o tamanho do valor, 
etc.

Iterator vs Generator:

Iterator - Classe que trabalha com iterável e tem os métodos "__iter__" (iter()) e "__next__" (next()).

Generator - Função que pausa.
'''

import sys; # Importando esse módulo só para ver o tamanho de valores na memória.

iterable = ['Eu', 'Tenho', '__iter__'];
iterator = iter(iterable);

list_comprehension = [n for n in range(10)];
print(list_comprehension); # Nesse caso tem o problema de criar de cara a lista com todos os valores possíveis para a expressão digitada, gerando muitos valores, ocupando espaço na memória,
                           # e deixando o código ineficiente. Para esses momentos, utilizar o generator faz muito sentido.

generator = (n for n in range(10)); # Generator expression para criar um generator.
print(generator);
print();

print("Perceba a grande diferença de espaço ocupado na memória do generator para a lista nesse exemplo:")
print("generator", sys.getsizeof(generator));
print("list_comprehension", sys.getsizeof(list_comprehension));

print(next(generator));
print(next(generator));
print(next(generator));
print(next(generator));
print(next(generator));
print("generator", sys.getsizeof(generator));

for n in generator:
    print(n);

