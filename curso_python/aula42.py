'''
Qual letra mais apareceu na frase? Com while.
'''

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

print(frase.count('o'));
print(frase.lower().count('o'));

i = 0;

qtd_apareceu_mais_vezes = 0;
letra_apareceu_mais_vezes = '';

while i < len(frase):
    letra_atual = frase[i];

    if letra_atual == " ": # Outra forma de desconsiderar o espaço, sendo uma forma mais eficiente pois não gasta processamento de forma desnecessária.
        i += 1;
        continue;
    
    qtd_letra_aparece_atual = frase.count(letra_atual);
    
    if (qtd_apareceu_mais_vezes < qtd_letra_aparece_atual) and (letra_atual != " "):
        letra_apareceu_mais_vezes = letra_atual;
        qtd_apareceu_mais_vezes = qtd_letra_aparece_atual;

    i += 1;

print(letra_apareceu_mais_vezes, qtd_apareceu_mais_vezes);