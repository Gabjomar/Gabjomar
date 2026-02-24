'''
Introdução ao empacotamento e desempacotamento.

Pode realizar empacotamento e desempacotamento com qualquer tipo iterável.
'''

nomes = ['Maria', 'Helena', 'Luiz'];

nome1, nome2, nome3 = nomes; # Desempacotamento.
print(nome2);

nome_1, nome_2, nome_3 = ['Maria', 'Helena', 'Luiz']; # Mesma coisa.
print(nome_2);

#nome1, nome2 = ['Maria', 'Helena', 'Luiz']; # Erro: "Too many values to unpack".
#nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz']; # Erro: "Not enough values to unpack".

# Para fazer o desempacotamento dessa maneira precisa ter a mesma quantidade de valores e de variáveis.

# Para pegar apenas o primeiro valor:

nome1, *resto = ['Maria', 'Helena', 'Luiz']; # Não é legal ficar criando variável que não vai usar, por isso existe uma convenção para usar o "_" nesses casos.

print(nome1, type(nome1), resto, type(resto));


nome1, *_ = ['Maria', 'Helena', 'Luiz']; # Continua sendo uma variável, só que por convenção sabemos que ela não será utilizada futuramente.

print(nome1, type(nome1), _, type(_));

# Para pegar o segundo valor:

_, nome2, *_ = ['Maria', 'Helena', 'Luiz'];

print(nome2, type(nome2));

# Para pegar o terceiro valor:

_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz']; # Perceba que não dá erro, é atribuído para "*_" uma lista vazia, pois acabou os valores da lista. 

print(nome3, type(nome3), _, type(_));