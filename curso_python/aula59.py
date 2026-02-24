'''
 Desempacotamento em chamadas de métodos e funções.
'''

string = 'ABCD';
lista = ['Maria', 'Helena', 1, 4, 7, 'Eduarda'];
tupla = 'Python', 'é', 'legal';
salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', (0, 4, 6, 194)],
]

primeira, segunda, *_, antepenultima, ultima = lista;
print(primeira, segunda, antepenultima, ultima);

for nome in lista:
    print(nome, end=' ', sep=' ');

print(*lista); # Faz a mesma coisa que o código com o for acima.
print(*tupla); # Faz a mesma coisa que o código com o for acima.
print(*salas);
print(*salas, sep="\n"); # Fica mais visual dessa maneira, para listas/tuplas com listas/tuplas dentro delas.
