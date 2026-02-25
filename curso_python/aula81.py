'''
Sets (Conjuntos) - Conjuntos em Python (tipo set).

Sets são eficientes para remover valores duplicados de iteráveis.
    - Não aceitam valores mutáveis;
    - Seus valores serão sempre únicos;
    - Não tem índexes;
    - Não garantem a ordem;
    - São iteráveis (for, in, not in).
'''

s1 = {1, 2, 3, 3, 3, 3, 1}; # Naturalmente os sets eliminam valores duplicados de forma muito eficiente.
print(s1);

# Uma utilidade de set é ser uma forma eficiente de remover duplicadas de algum valor do tipo iterável (tupla, lista, etc) por meio de 
# type coercion.
l1 = [1, 2, 3, 3, 3, 3, 1];
s2 = set(l1);
l1 = list(s2);
print(l1);

# set é tipo uma "sacola" do Python, tu vai jogando as coisas dentro, garantindo que não vai haver duplicadas, e sabe que vai ficar fora da ordem
# e que depois tu vai ter que procurar, só que essas limitações do set cria a vantagem dele ser extremamente eficiente, sendo menos pesado para o
# programa rodar.

print(3 in l1); # Buscando determinado valor dentro de um set.
print(3 not in l1); # Buscando determinado valor dentro de um set.

for numero in l1: # sets são iteráveis.
    print(numero);

