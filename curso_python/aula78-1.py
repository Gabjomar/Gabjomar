'''
Métodos úteis dos dicionários em Python.
len - quantas chaves; -> Não é um método, é um thunder (todo thunder começa e termina com dois underscores/underlines)
keys - iterável com as chaves;
values - iterável com os valores;
items - iterável com chaves e valores;
setdefault - adiciona valor se a chave não existe;
copy - retorna uma cópia rasa (shallow copy);
get - obtém uma chave;
pop - apaga um item com a chave especificada (del);
popitem - apaga o último item adicionado;
update - atualiza um dicionário com outro.
'''

dicionario1 = {
    'chave1': 'A',
    'chave2': 'B',
    'chave3': 'C',
}

print("copy:");

dicionario2 = dicionario1; # Cuidado com a cilada! Continue lendo para entender.

dicionario2["chave2"] = 1000; # Alterar um dicionário afeta o outro, pois tu referenciou que dicionario2 = dicionario1, logo eles são o mesmo
                              # dicionário presente na memória. Lembrete: Sempre tomar cuidado quando estiver trabalhando com valores mutáveis que
                              # você pode cair nessas ciladas sem perceber.

print(f"{dicionario1=} {dicionario2=}");

# Cópia rasa (shallow copy) é uma cópia que não afeta o valor que foi copiado, ou seja, a cópia ocupa um novo espaço na memória. Porém quando há
# valores mutáveis dentro do dicionário, ai a cópia rasa continuará apontando para o mesmo valor na memória, fazendo uma referenciação/atribuição de
# valor ao invés de uma cópia de valor, por isso se chama cópia rasa, pois não entra nos subníveis do dicionário.

# Esse conceito é muito importante entender, pois no Python, em muitas outras linguagens de programação e no consenso do que é programação, o
# conceito de igualdade é diferente de cópia. Duas cópias são iguais no momento em que ocorreu a cópia mas posteriormente elas se tornam 
# independentes, enquanto duas variáveis ditas iguais apontam para o mesmo valor na memória, fazendo com que se você alterar uma, você altera o 
# valor presente na memória, consequentemente alterando a outra variável.

# Acredita-se que a cópia rasa funciona assim por conta de processamento, para quando realizar a cópia de dicionários gigantes, não gere uma 
# duplicidade gigantesca de valores, por isso eles fazem só a cópia dos valores presentes no primeiro nível e linkam os valores dos níveis mais
# internos (subníveis). 

dicionario2 = dicionario1.copy();

dicionario2["chave1"] = True;

print(f"{dicionario1=} {dicionario2=}");

dicionario3 = {
    'chave1': 'A',
    'chave2': 'B',
    'chave3': [0,1,2],
}

dicionario4 = dicionario3.copy();

dicionario4["chave3"][1] = 99999;

print(f"{dicionario3=} {dicionario4=}");

# Para realizar a cópia "profunda" (deep copy) de todos os valores em todos os subníveis do dicionários, é necessário utilizar o módulo copy e a
# função "deepcopy()".

import copy;

dicionario4 = copy.deepcopy(dicionario3);

dicionario4["chave3"][1] = "ABC";

print(f"{dicionario3=} {dicionario4=}");

# A função "copy()" do módulo copy faz exatamente a mesma coisa que o método copy da mesma forma, é redundante, utilize o que preferir.


