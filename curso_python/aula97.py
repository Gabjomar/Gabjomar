'''
dir, hasattr e getattr em Python.

Verificando o que é possível fazer.

dir() - Traz todos os atributos/nomes que estão definidos na sua classe.
hasattr - Verifica se determinada classe tem determinado atributo/nome.
getattr - Adicionar dinamicamente um atributo/nome a uma determinada classe.
'''

string = 'Luiz';

print(string, dir(string));

print(string, hasattr(string, 'upper')); # No "hasattr()", o atributo/nome sempre terá que ser atribuído à função como uma string.

metodo = 'upper';
print(getattr(string, metodo)());

metodo = 'lower';
print(getattr(string, metodo)());