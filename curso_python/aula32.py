'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
numero = input('Digite um número inteiro: ');

try:
    numero_int = int(numero);
    if (numero_int % 2) == 0:
        print('Este número é par');
    elif (numero_int % 2) != 0:
        print('Este número não é par');
except:
    print("Este número não é inteiro");

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
hora = input('Que horas são? ');

try:
    hora_int = int(hora);
    if (hora_int >= 0) and (hora_int <= 11):
        print('Bom dia!');
    elif (hora_int >= 12) and (hora_int <= 17):
        print('Boa tarde!');
    elif (hora_int >= 18) and (hora_int <= 23):
        print('Boa noite!');
    else:
        print('Não conheço essa hora.');
except:
    print('Digite apenas números inteiros.');

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4
letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

primeiro_nome = input('Digite o seu primeiro nome: ');
tamanho_primeiro_nome = len(primeiro_nome);

if primeiro_nome:
    if tamanho_primeiro_nome <= 4:
        print('Seu nome é curto');
    elif (tamanho_primeiro_nome >= 5) and (tamanho_primeiro_nome <= 6):
        print('Seu nome é normal');
    elif tamanho_primeiro_nome > 6:
        print('Seu nome é muito grande');
else:
    print('Por favor, digite alguma coisa.');