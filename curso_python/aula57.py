'''
Lista de listas e seus índices.
Podem ser listas dentro de tuplas, tuplas dentro de listas e por aí vai.
'''

salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', (0, 4, 6, 194)],
]

# Buscando valores específicos a partir dos índices, como uma matriz na matemática.

print(f'salas[0]: {salas[0]}');
print(f'salas[1]: {salas[1]}');
print(f'salas[2]: {salas[2]}');

print(f'salas[0][0]: {salas[0][0]}');
print(f'salas[2][0]: {salas[2][0]}');
print(f'salas[2][2]: {salas[2][2]}');

print(f'salas[2][3][1]: {salas[2][3][1]}');

for sala in salas:
    print(sala);
    for aluno in sala:
        print(aluno);