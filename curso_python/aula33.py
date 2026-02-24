'''
Documentação do python:
https://docs.python.org/pt-br/3/library/stdtypes.html

Tipos imutáveis que vimos: str, int, float, bool.
'''

string = 'darth Vader';

print(string[4]);

try:
    string[4] = 'ABC'; # Por ser uma str, um tipo imutável, isso não pode acontecer.
except:
    print('Tipo imutável');

# Como terias que fazer para conseguir fazer a "modificação" desejada:
outra_variavel = f'{string[:4]}ABC{string[5:]}'; 
print(outra_variavel);

# Exemplo de método somente existente do tipo str. Na documentação é apresentado diversos outros métodos para os diferentes tipos existentes no python, que pode ser útil em algum momento.
print(string.capitalize()); 
print(string.zfill(20));