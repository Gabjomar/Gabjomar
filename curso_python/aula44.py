'''
Função range -> range(start, stop, step).

Muito útil juntar for + range.
'''
numeros = range(10);

for i in numeros:
    print(i); # São números! Não são índices, é um intervalo, um range, de números.
print('');

numeros = range(4,10);

for i in numeros:
    print(i); # São números! Não são índices, é um intervalo, um range, de números.
print('');

numeros = range(4, 10, 2);

for i in numeros:
    print(i); # São números! Não são índices, é um intervalo, um range, de números.
print('');

numeros = range(0, -10, -2);

for i in numeros:
    print(i); # São números! Não são índices, é um intervalo, um range, de números.
print(''); 

numeros = range(0, 100, 8);

for i in numeros: # Vai entregar os números múltiplos de 8 de 0 a 100.
    print(i); # São números! Não são índices, é um intervalo, um range, de números.
print(''); 