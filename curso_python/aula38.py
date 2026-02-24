'''
Repetições.
while dentro de while (laços internos).

'''

qtd_linhas = 5;
qtd_colunas = 9;

linha = 1;
coluna = 1;

while linha < qtd_linhas:
    linha += 1;
    while coluna <= qtd_colunas:
        coluna += 1;
        print('*', end='');
    print('*');
    coluna = 1;


