'''
Sets (Conjuntos) - Conjuntos em Python (tipo set).

Conjuntos são ensinados em matemática. Representados graficamente pelo diagraman de Venn.

Sets em Python são mutáveis, porém  aceitam apenas tipos imutáveis como valor interno.
'''

# Duas formas de criar um set:
# set(iterável) ou {1, 2, 3}
# Pode parecer um dicionário, mas diferente do dicionário que possui par de chave e valor, o conjunto só possui o valor.

conjunto_1 = set();
conjunto_2 = {1,2,3}; # Se você deixar só {} vazio, o Python interpreta que é um valor do tipo dict e não set.

print(conjunto_1, type(conjunto_1));
print(conjunto_2, type(conjunto_2));

conjunto_3 = set("Guilherme");
print(conjunto_3); # Não garante a ordem do que foi adicionado no set.

