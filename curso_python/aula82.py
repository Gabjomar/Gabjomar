'''
Sets (Conjuntos) - Conjuntos em Python (tipo set).

Métodos úteis:
add
update
clear
discard
'''

print("add:"); # Não aceita mais de um argumento, tem que ir adicionando de um em um.
s1 = set();
s1.add('Luiz');
s1.add(3);
print(f'{s1=}');

print('update:'); # Faz basicamente a mesma coisa que o método add, só que consegue passar mais de um valor por vez, utilizando valores iteráveis.
s1.update('Olá mundo!'); # Se fizer uma adição dessa forma, irá iterar a string ou algum outro valor passado, fazendo ficar dividido em caractere 
                         # por caractere e de maneira desorganizada no set.
print(f'{s1=}');
# Para fazer a adição de forma unificada, é necessário adicionar o valor como um iterável em si, como adicionando o valor do tipo tupla.
s1.update(('Olá mundo',3));
print(f'{s1=}');
# Porém note que continua não garantindo a ordem.

print('discard:') # Apaga o valor especificado.
s1.discard(3);
print(f'{s1=}');

print('clear:') # Apaga todos os valores presentes no set.
s1.clear();
print(f'{s1=}');