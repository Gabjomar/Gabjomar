'''
Retorno de valores das funções (return).
'''

variavel1 = print("Ana");
print(f"{variavel1=}");

# Isso ocorre pois print é uma função usada para mostrar algo no terminal, não para gerar algum valor, por isso ela retorna None.

def soma(x,y):
    ...

variavel2 = soma(1,2);
print(f"{variavel2=}"); # Não definimos em nenhum momento que valor que queremos que a função retorne, por isso ela retorna None por padrão.

def soma1(x,y):
    z = x + y;
    return z;

variavel3 = soma1(3,4);
print(f"{variavel3=}");

# print(variavel2 + variavel3); # Error: Unsupported operand type(s) for +: 'NoneType' and 'int'. Ou seja, o valor retornado da função soma1 é do
# tipo int e o valor retornado da função soma, por padrão, é do tipo NoneType, que é o valor None.

def soma2(x,y):
    if (x + y) > 6:
        return 1000;
    elif x == 0:
        return (10,20);
    return x + y;

valor1 = soma2(2,2);
valor2 = soma2(3,4);
print(valor1 + valor2);

# Como percebemos, print != return, print é uma função que é utilizada para apresentar algo no terminal, enquanto return é uma ferramenta para
# definir que valor uma função irá retornar.

# Depois do return, qualquer código presente na função estará inalcançável, pois o return indica o encerramento da função, que depois de todo o
# código construído da função, a função irá retornar ... (return ...).

# É possível retornar qualquer tipo de dado em uma função, uma tupla, lista, etc.
