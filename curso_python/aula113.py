'''
Exercício - Adiando execução de funções.
'''

def soma(x, y): # Toda essa linha aqui é chamada de "assinatura da função" ou "método da função".
    return (x + y);

def multiplica(x, y):
    return (x * y);

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y); # Faz o closure para salvar informações na memória que serão utilizadas posteriormente.
    return interna;

soma_com_cinco = criar_funcao(soma, 5);
multiplica_por_dez = criar_funcao(multiplica, 10);

print(soma_com_cinco(10));
print(multiplica_por_dez(10));