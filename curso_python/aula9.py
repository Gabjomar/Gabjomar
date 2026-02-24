'''
Operadores aritméticos

Operadores aritméticos resultam em um valor com base no tipo utilizado na conta, ou seja, se houver um int + float, retornará um valor float, por exemplo.
'''
adicao = 10 + 5;
print('adição', adicao);

subtracao = adicao - 3;
print('subtracao', subtracao);

multiplicacao = adicao * subtracao;
print('multiplicacao', multiplicacao);

divisao = adicao / multiplicacao; # Sempre retorna float.
print('divisao', divisao, type(divisao));

divisao_inteira = adicao // multiplicacao; # Sempre retorna o valor int ou um float com zeros depois da vírgula/ponto.
print('divisao_inteira', divisao_inteira, type(divisao_inteira));

exponenciacao = 2 ** subtracao;
print('exponenciacao', exponenciacao);

modulo_1 = exponenciacao % adicao; # Resto da divisão.
modulo_2 = 64 % 4; # Resto da divisão.
print('modulo_1', modulo_1);
print('modulo_2', modulo_2);

print((10 % 8) == 0); # 10 não é divisível por 8!
print((10 % 2) == 0); # 10 é par!