'''
Cuidados com dados mutáveis.
"=" -> Copiado o valor (imutáveis);
"=" -> Aponta para o mesmo valor na memória (mutáveis).
'''

nome = "Luiz";
noutra_variavel = nome; # Copiou o valor presente na variável "nome" para a variável "noutra_variavel".
nome = "Abc";
print(nome);
print(noutra_variavel); # Perceba que, por ser dados imutáveis, o código teve o comportamento "esperado".

lista_a = ['Luiz', 'Maria'];
lista_b = lista_a; # Não estou copiando o valor da "lista_a" na "lista_b", estou fazendo a "lista_b" apontar para o mesmo valor na memória que a "lista_a".

lista_a[0] = 'Qualquer coisa'; 
print(lista_a, lista_b);
# Por conta dessa diferença na forma como os dados mutáveis e imutáveis funcionam, quando eu mudar qualquer coisa no valor da memória, mudará o valor apresentado
# pelas duas variáveis.

lista_b = lista_a.copy(); # Para copiar os valores de uma lista em outra variável, precisa utilizar o método copy.
lista_a[0] = 'ABCDARIO'; 
print(lista_a, lista_b);