'''
Iterables e Iterators em Python.

Iterable (iterável) - Classe na qual você pode acessar valores sequencialmente. Tem a responsabilidade de manter os valores sequencialmente.
Iterator é uma classe que possui as seguintes características:
    - Precisa de um iterável para existir. Todo iterator é criado a partir de um iterável;
    - Possui a única responsabilidade de entregar apenas um valor por vez. Então ele só sabe qual é o próximo valor, não sabe mais nenhum valor além do próximo, não sabe nem o tamanho do 
    iterável;
    - Ele possui o "__iter__" e "__next__", diferente do iterable que só possui "__iter__";
    - Ele esgota os valores, ou seja, depois de passar por todos os valores, ele retorna um erro "StopIteration", como se fosse um ponteiro.
'''

iterable = ['Eu', 'Tenho', '__iter__'];

iterator = iterable.__iter__();
iterator_1 = iter(iterable); # Outro jeito de criar um iterator.

# print(iterator[1]); Dá erro: list_iterator' object is not subscriptable.
# print(len(iterator)); Dá erro: object of type 'list_iterator' has no len().

print(next(iterator)); # Só sabe isso, o próximo valor.
print(iterator.__next__()); # Outro jeito de chamar o próximo valor.
print(next(iterator)); # Só sabe isso, o próximo valor.

