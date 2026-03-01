'''
List comprehension em Python.
List comprehension com mais de um for.
'''

lista = [];

for x in range(3):
    for y in range(3):
        lista.append((x,y)); # Não é possível adicionar mais de um valor em um mesmo índice em um iterável, como essa lista, então nesses casos 
                             # precisa utilizar um tipo de valor que aceita mais de um valor dentro dele, como a tupla, que foi utilizada nesse 
                             # caso.

print(f'{lista=}');
print();

# Como fazer a lógica acima em list comprehension? Bem simples e lógico:

lista_1 = [
    (x,y)
    for x in range(3)
    for y in range(3)
];
print(f'{lista_1=}');
print();

lista_2 = [
    (x,y,z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
];
print(f'{lista_2=}');
print();

# Pode ser que você se depare com alguém fazendo algo desse tipo:

lista_3 = [
    [x for y in range(3)] # Isso é uma list comprehension dentro de um valor que será utilizado em outra list comprehension.
    for x in range(3)
];
print(f'{lista_3=}');
print();

lista_4 = [
    [(x, letra) for letra in 'Gustavo']
    for x in range(3)
];
print(f'{lista_4=}');
print();
