'''
split e join com list e str.
split - divide uma string.
join - une uma string.
'''

frase = 'Olha só que coisa interessante.    zxc zxc';
lista_palavras = frase.split();
print(lista_palavras);
lista_palavras = frase.split("."); # O argumento do método define o que será utilizado como indicação para realizar a divisão.
print(lista_palavras);

for i, palavra in enumerate(lista_palavras):
    print(lista_palavras[i].strip());

lista_palavras_corrigida = []; # Boa prática é não utilizar o valor de um objeto mutável para modificar o próprio valor. Até para casos onde você deseje reutilizar os valores originais
# posteriormente.

for i, palavra in enumerate(lista_palavras):
    lista_palavras_corrigida[i] = lista_palavras[i].strip(); # Lista é um tipo mutável.

print(lista_palavras_corrigida);

palavras_unidas = '-'.join('abc');
print(palavras_unidas);
palavras_unidas = '-'.join(lista_palavras_corrigida);
print(palavras_unidas);
