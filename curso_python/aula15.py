'''
O programa não finaliza enquanto o usuário não realiza alguma ação referente ao input(), fica paralisado na linha aonde está o input.

Input sempre interpreta os dados recebidos do usuário na forma de str.

Forma fácil de identificar de onde está vindo os dados nas f strings -> "{nome_da_variavel=}".

'''

#nome = input('Qual o seu nome? ');
#print(f'o sue nome é {nome=}');

numero_3 = input('Digite um número: ');
numero_4 = input('Digite outro número: ');

print(f'A soma dos números é: {numero_3 + numero_4}');

numero_1 = int(input('Digite um número: '));
numero_2 = int(input('Digite outro número: '));
# Fazer a mudança de tipo direto aqui é uma má prática de programação, pois se o usuário digitar alguma coisa que não pode ser convertida para o que você deseja,
# o programa já vai dar erro logo de cara e vai ser mais difícil de entender o que está acontecendo.

print(f'A soma dos números é: {numero_1 + numero_2}');

numero_5 = input('Digite um número: ');
numero_6 = input('Digite outro número: ');

int_numero_5 = input('Digite um número: ');
int_numero_6 = input('Digite outro número: ');
# Assim é uma forma mais adequada de fazer essa mudança de tipo, pois permite o programador fazer checagens com alguma estrutura condicional
# entre o input e a mudança de tipo, podendo assim, impedir do código quebrar nessas situações.

print(f'A soma dos números é: {int_numero_5 + int_numero_6}');

