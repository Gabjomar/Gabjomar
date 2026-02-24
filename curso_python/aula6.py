'''
Conversão de tipos, coerção, type convertion, typecasting, coercion
-> É o ato de converter um tipo em outro

Tipos imutáveis e primitivos: str, int, float, bool.
'''

print(1 + 1);
print("figu" + "eira"); # Isso funciona pois o python é uma linguagem de programação com tipagem dinâmica.

"""
Pelo phyton ser de tipagem forte, ele não vai tentar converter o tipo de algum dos valores para fazer o código rodar sem erros, como aconteceria em linguagens com tipagem fraca,
ele vai conversar os tipos dos valores e apresentará um erro no código. Ex.: print(1 + "1"); 

""" 

print('1', type('1'));
print(int('1'), type(int('1')));
print(int('1') + 1);
print(float('1.7') + 1); # Olha que legal
print(bool('')); # Str vazia -> bool False
print(bool('#')); # Str não vazia -> bool True
print(str(3) + '5', type(str(3) + '5'));