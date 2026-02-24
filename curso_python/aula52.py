'''
Tipo tupla - Uma lista imutável.

A tupla é um pouco mais eficiente do que a lista, então é uma boa prática de programação utilizar tuplas ao invés de listas quando você sabe que não irás precisar
modificar os valores.
'''

nomes = 'Maria', 'Helena', "Luiz"; # Primeiro jeito de criar uma tupla.
letras = ('A', 'B', "C"); # Outra forma de criar uma tupla.

# nomes[1] = "ABC" # Erro: 'tuple' object does not support item assignment.
print(nomes, type(nomes));
print(letras[-1], type(letras));

# É possível converter, fazer uma coerção, de uma lista para uma tupla e vice-versa.

valores = ['1', 2, 4.3];
print(valores, type(valores));

valores[1] = "ABC";

valores = tuple(valores);
print(valores, type(valores));

valores = list(valores);

print(valores, type(valores));

valores[-1] = True;
print(valores, type(valores));

valores = tuple(valores);
print(valores, type(valores));
