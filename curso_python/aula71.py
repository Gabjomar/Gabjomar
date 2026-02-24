'''
args - Argumentos não nomeados.
* - *args (empacotamento e desempacotamento)
'''

# Lembrete de desempacotamento:
x, y, *resto = 1, 2, 3, 4, 5;
print(f'{x=} {y=} {resto=}');

# Empacotamento dos argumentos recebidos quando a função é chamada. É utilizado essa ferramenta para a função print(). É utilizado "*args" com 
# "args" por convenção. Essa ferramenta realizar o empacotamento dos dados agrupando em uma tupla.
def soma(*args): 
    print(args, type(args));

soma(1,2,3,4,5,6);

def soma1(*args):
    total = 0; # Variável para acumular valores.
    # Como o empacotamento dos n argumentos recebidos são agrupados em uma tupla, para realizar a soma de argumento por
    # argumento, é necessário utilizar "for ... in args:".
    for numero in args:
        print(total);
        total += numero;
        print(total);
        

#soma1(1,2,3,4,5,6);

# Função que soma uma quantidade indefinida de valores:
def soma2(*args):
    total = 0; # Variável para acumular valores.
    for numero in args:
        total += numero;
    return total;

soma_1_2_3_4_5 = soma2(1,2,3,4,5);
print(soma_1_2_3_4_5);

# Existe uma função pronta no python que faz esse processo:
# print(sum(1,2,3,4,5));

# Relembrando desempacotamento de dados:
numeros = 1, 7, 54, 20, 40, 3, 9;
print(numeros);
print(*numeros);

# Sem realizar o desempacotamento dos argumentos, da forma como essa função está construída, ocorrerá um erro na hora de somar diferentes tipos
# de dados ("unsupported operand type(s) for +=: 'int' and 'tuple'").

# outra_soma = soma2(numeros); 
# print(outra_soma);

outra_soma_1 = soma2(*numeros);
print(outra_soma_1);
