'''
Fatiamento de strings.
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] 
i - início;
f - fim;
p - passo (de quantos em quantos caracteres será pulado);

Obs.: A função len retorna a quantidade de caracteres da str.
'''

variavel = 'Olá mundo';
print(variavel[-4]);
print(variavel[5]);
print(variavel[4:]); # Omitir o final significa que você quer até o final.
print(variavel[:4]);
print(variavel[0:4]);
print(variavel[0:4]);
print(len(variavel));
print(len(variavel[3]));
# Contagem é diferente de índice! Contagem começa do 1, índice começa do 0.
print(variavel[::3]);
print(variavel[::-1]); # Inverte a string.
print(variavel[0:9:-1]); 
# Dá errado, pois está se baseando nos caracteres positivos. 
print(variavel[-1:-10:-1]); # Inverte a string.
print(variavel[0:len(variavel):1]);
