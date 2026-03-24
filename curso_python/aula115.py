'''
Funções decoradoras (decoretors) e decoradores no Python.

Decorar = Adicionar / Remover / Restringir / Alterar. Envolve o uso de closure.

Funções decoradoras são funções que decoram outras funções.

Funções decoradores são usadas para fazer o Python usar as funções decoradoras em outras funções. São @syntax_sugar "syntax sugar" (açúcar sintático) no Python, ou seja, o Python possui 
recursos que facilitam o uso das funções decoradoras, sem precisar escrever tanto código, um facilitador.
'''

# O tema dessa aula é muito utilizado pois existe na programação o princípio da responsabilidade única, onde fala que cada objeto deve fazer uma única função e que se você está com
# dificuldade para nomear o objeto de acordo com a função que ele faz, é certo que esse objeto está fazendo mais ações do que deveria e é necessário dividir esse objeto em mais objetos
# para cada objeto fazer uma única função separadamente.

# Essa é uma função decoradora:
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar');
        for arg in args:
            is_string(arg);
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}');
        print('Ok, agora você foi decorada');
        return resultado;
    return interna;

# Modo de se utilizar as funções decoradores (@syntax_sugar):

# Aqui o Python está automaticamente assumindo que você irá informar o nome da função decoradora que desejas utilizar, que irás entregar para ele uma função que você deseja decorar e a 
# função decoradora que você informou para ele precisa retornar uma função para o Python poder utilizar, ou seja, nesse caso a função "inverte_string()" some e o Python automaticamente a 
# substituisse pela função "interna()".
@criar_funcao 
def inverte_string(string):
    print(f'Para o Python, o nome da função "inverte_string()" agora é "{inverte_string.__name__}()"');
    return string[::-1];

def is_string(p):
    if not isinstance(p, str):
        raise TypeError('p deve ser uma string');

# Com as funções decoradores, você não precisa criar nenhum malabarismo no código, pode ir direto ao ponto:

invertida_0 = inverte_string("123");

# Sem as funções decoradores, você precisa criar esse malabarismo no código para conseguir usar a função decoradora:

# inverte_string_checando_parametro = criar_funcao(inverte_string);
# invertida_0 = inverte_string_checando_parametro('Gabriel');

print(invertida_0);