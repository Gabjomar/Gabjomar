'''
Argumentos nomeados e não nomeados em funções Python.
Argumento nomeado tem nome com sinal de igual.
Argumento não nomeado, também chamado de argumento posicional (depende da posição ), recebe apenas o argumento (valor).
'''

def soma(x, y, z): # Parâmetros x e y da função soma.
    print(x + y + z);


print(soma);
print(soma(1, 2)); # Funções em python por padrão retornam não, por isso está aparecendo o "None" quando faz um print de uma função que não tem
# um valor de retorno definido.

def soma1(x, y):
    print(f'{x=} y={y}', '|', 'x+y=', x + y); # Aqui é apresentado duas formas de apresentar o nome de uma varíavel e o seu valor em um print,
# sendo uma maneira mais direta e outra mais clara. 

soma1(1,3);
soma1(3,1);
soma1(y=3,x=1); # Argumento nomeado retira o problema de errar a ordem desejada dos argumentos da função.

print(1,2,3, sep='-'); # "sep" é um argumento nomeado da função print(), que só é atribuído um outro valor para ele por meio de argumento nomeado.

#soma(1, y = 3, 3) # Depois de usar argumento nomeado, todos os próximos argumentos precisarão ser nomeados, se não ocorrerá um erro, via de regra.
# ^         ^
# |         |
# |         |
# Nome da   Execução da 
# função.   função.
