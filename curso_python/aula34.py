'''
Repetições.
while (enquanto).
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
'''

i = 0;

while i < 5:
    print(i);
    i = i + 1;

condicao = True;

while condicao:
    nome = input('Digite o seu nome: ');
    print(f'Seu nome é {nome}');
    if nome == 'sair':
        break;
print('acabou');

# "break" busca o laço mais próximo para encerrar.