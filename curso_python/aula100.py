'''
Introdução às Generator functions (funções geradores) em Python.

Generator functions são funções que pausam, não necessariamente precisam se encerrar totalmente. Para definir essa pausa, utiliza "yield", logo toda função que tem "yield" é uma generator 
function.
'''

def generator(n = 0):
    yield 1; # Pausar
    return 'ACABOU'; # Gera uma exceção, uma flag do tipo "StopIteration" com o valor definido no return.

gen = generator(n = 0);
print(next(gen));
# print(next(gen)); "StopIteration: ACABOU"

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def generator_1(n=0):
    yield 1;
    print('Continuando...');
    yield 2;
    print('Mais uma...');
    yield 3;
    print('Vou terminar...');
    return 'ACABOU';

gen_1 = generator_1(n = 0);
print(next(gen_1));
print(next(gen_1));
print(next(gen_1));
# print(next(gen_1));

# Generator function:
def generator_3(n = 0, maximum = 10):
    while True:
        yield n;
        n += 1;
        if n > maximum:
            return;

gen_3 = generator_3();
for n in gen_3:
    print(n);