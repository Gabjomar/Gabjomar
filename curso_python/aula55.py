'''
Imprecisão de ponto flutuante.

Double-precision floating-point format IEEE 754.
'''

numero_1 = 0.1;
numero_2 = 0.7;
numero_3 = numero_1 + numero_2;
print(numero_3); 
print(f'{numero_3:.2f}', type(f'{numero_3:.2f}')); # Uma solução para contornar a imprecisão, mas que faz o valor se tornar uma string, precisando possivelmente ter que converter depois.
print(round(numero_3,1));
print(round(numero_3, 3), type(round(numero_3, 3))); # Segunda solução, onde a função round deixa o valor no mesmo tipo que foi atribuido a ela.

import decimal; # Terceira solução, para casos onde é necessária uma grande precisão para números de ponto flutuante.

numero_4 = decimal.Decimal(0.1);
numero_5 = decimal.Decimal(0.7);
numero_6 = numero_4 + numero_5;
print(numero_6);
print(round(numero_6, 0));
print(round(numero_6, 1));
