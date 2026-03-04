'''
Yield from - Conecta yields de diferentes geradores, permitindo dar continuidade a um generator a partir de outro generator.
'''

def generator_1():
    print('Começou generator_1');
    yield 1;
    yield 2;
    yield 3;
    print('Acabou generator_1');


def generator_2():
    print('Começou generator_2'); # Perceba que o que vem antés de "yield from" é executado antes do que virá do "yield from", por isso "Começou generator_2" aparece antes de
                                  # "Começou generator_1".
    yield from generator_1();
    yield 4;
    yield 5;
    yield 6;
    print('Acabou generator_2');


gen = generator_2();
for n in gen:
    print(n);