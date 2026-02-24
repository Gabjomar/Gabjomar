'''
Exercício.

Exiba os índices da lista.
'''

lista = [1423, 1.4, "Maria"];
indice = 0;

for nome in lista:
    print(indice, nome, type(nome)); # Fazendo desse jeito é possível acessar o valor de cada elemento da lista.
    indice += 1;


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Gabarito (menos linhas de código):

lista = [1423, 1.4, "Maria"];
indices = range(len(lista));

for indice in indices:
    print(indice, lista[indice], type(lista[indice]));