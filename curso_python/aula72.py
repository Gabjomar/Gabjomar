'''
Exercícios com funções.

1º) Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o total para uma variável e mostre o valor da variável.

2º) Crie uma função que fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.
'''

# 1º)

def multiplica(*args):
    total = 1;
    for i in args:
        total *= i;
    return total;

resultado_primeira_funcao = multiplica(3,6,10,10,10,10);
print(resultado_primeira_funcao);

# ------ # ------ # ------ # ------ # ------ # ------

# 2º)

def par_ou_impar(numero_avaliado):
    if (numero_avaliado % 2) == 0:
        return f"{numero_avaliado} é par";

    # Esse else é redundante nesse caso, onde a lógica dessa função é mais simples, pois quando um return é executado, ele encerra a lógica da
    # função que ele está retornando um determinado valor e retorna esse valor com base nessa lógica executada pela função.
    # else:
    #     return f"{numero_avaliado} é ímpar";

    # Fica um código mais enxuto:
    return f"{numero_avaliado} é ímpar";

resultado_segunda_funcao = par_ou_impar(7);
print(resultado_segunda_funcao);