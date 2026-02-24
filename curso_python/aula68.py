'''
Escopo de funções em Python.
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

"Geralmente, o que eu faço dentro da função, fica dentro da função, não afeta o que está fora da função.".

Posso acessar variáveis de escopos mais externos, porém não consigo acessar de escopos mais internos.
'''
def escopo():
    x = 1; # Variável x está definida no escopo dentro da função, escopo local.
    print(x);
    def outra_funcao():
        print(x*2);
    outra_funcao();

escopo();

#print(x); # x não está definido no escopo global do código.

# Variável y está sendo definida no escopo global porém somente após a função que utiliza ela ser chamada, fazendo o interpretador definir que 
# a variável não está definida.
# def escopo1():
#     print(y);

# escopo1();

# y = 1;

x = 1; # Variável definida no escopo global, escopo desse módulo "aula68.py".

def escopo2():
    x = 10;
    print(f'{x=}');

# O valor de x no escopo local da função continua protegido do escopo mais externo, fazendo com que, mesmo após executar a função, o valor de x
# é aquele definido no escopo em que esse valor será utilizado. A variável com nome "x" definida no escopo global é uma variável diferente da 
# variável com nome x definida no escopo local da função. 
print(f'{x=}');
escopo2();
print(f'{x=}');

# Caso desejado, é possível manipular as variáveis de um escopo mais externo em um escopo mais interno, porém não é uma boa prática de programação.

def escopo3():
    global x; # Definindo que o x que será manipulado nesse escopo local da função é o x do escopo global.
    x = 10;
    print(f'{x=}');

print(f'{x=}');
escopo3();
print(f'{x=}'); # Perceba que agora o valor do x no escopo global realmente alterou a partir da manipulação no escopo local da função.

