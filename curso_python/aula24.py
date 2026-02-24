'''
Operadores in ("entre" ou "está entre") e not in ("não entre" ou "não está entre")

Strings são iteráveis (valores que se pode navegar item por item):

 0 1 2 3 4 5 (índices positivos para navegar na string 'Otavio')
 O t a v i o
-6-5-4-3-2-1 (índices negativos para navegar na string 'Otavio')
'''
nome = 'Otavio';
indice = input('Digite o índice desejado: ');
indice_int = int(indice);
print(nome[indice_int]);
print(10 * '-');
print('a' in nome);
print('z' in nome);
print('zero' in nome);
print('banana' not in nome);
print(10 * '-');

nome_1 = input('Digite o seu nome: ');
encontrar = input('Digite o que deseja encontrar: ');

if encontrar in nome_1:
    print(f'{encontrar} está em {nome_1}');
else:
    print(f'{encontrar} não está em {nome_1}');
