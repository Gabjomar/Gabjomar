'''
Funções lambda mais complexas no Python.

Uma boa prática que irás perceber é utilizar parâmetros com nomes pequenos nas funções, de preferência com um único caractere, pois como são
funções que devem ter apenas uma linha/expressão, essa prática ajuda na legibilidade do código.

Dica: Se você está escrevendo o seu código e está complicado de entender, não estás construindo ele da melhor maneira, mude a forma como estás 
escrevendo e utilize mais variáveis, pois variáveis são ferramentas essenciais para deixar um código mais legível e fácil de se entender. Lembre-se
que quando estamos escrevendo um código, estás escrevendo para outras pessoas conseguir ler e entender ele, pois o computador vai conseguir
interpretar de qualquer maneira.
'''

# Mostrando como fazer as funções abaixo com o tipo lambda:

def executa(funcao, *args):
    return funcao(*args);

def soma(x,y):
    return x + y;

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador;
    return multiplica;

### - ### - ### - ### - ### - ### - ### - ###

# Não é uma boa prática utilizar funções lambda dessa forma direta, é considerada uma má prática de programação, é recomendável utilizar uma função
# que executa funções, nesse caso, funções lambda, por isso existe a função executa() aqui.
funcao = lambda parametro: parametro;

print("Função soma():");

print(
    executa(
        lambda x, y: x + y, 2, 3 # Funções lambda não tem nome nem parênteses e o "lambda" é o equivalente a "def".
    )
);

# Mesma coisa que a função lambda faz
print(
    executa(
        soma, 2, 3
    )
);

print("Função cria_multiplicador():");

#duplica = cria_multiplicador(2); # Assim seria com a função normal
triplica = executa(
    lambda m: lambda n: n*m, 
    3 # Argumento para conseguir chamar a função, está definindo que será uma função que multiplica por 3 o argumento que enviar para ela.
);

print(triplica(21));

print("Usando *args nas funções lambda:");

print(
    executa(
        lambda *args: sum(args),
        2, 6, 10, 20 # Argumentos para conseguir chamar a função com parâmetro "*args".
    )
)