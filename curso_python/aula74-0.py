'''
Closure (fechamento) e funções que retornam outras funções.
'''

def criar_saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}";
    return saudar; # Colocar a função sem parênteses é uma tática para atrasar a execução da função, forçando o interpretador a salvar a função
# com os seus argumentos específicos daquela execução para o interpretador conseguir resolver a função posteriormente, se necessário. Basicamente,
# por ser uma função dentro de outra função, como o interpretador precisa resolver a função mais externa e o retorno dessa função mais externa é
# uma função que não foi resolvida pois não foi chamada com parâmetros, foi indicada apenas a sua estrutura/lógica, obriga o interpretador a salvar
# toda a informação com contexto da função mais interna na memória para conseguir resolver a função mais externa e possibilitar a função mais
# interna ser resolvida posteriormente (ser fechada posteriormente)

# Desse jeito, o que retorna pela função criar_saudacao é o endereço na memória onde essa função está armazenada com o contexto dos argumentos
# adicionados quando a função foi chamada (com o escopo da função), por isso o endereço da memória é diferente entre duas funções iguais, mas com 
# argumentos distintos.

# <function criar_saudacao.<locals>.saudar at 0x0000020C7D753690>
# <function criar_saudacao.<locals>.saudar at 0x0000020C7D753740>

saudacao_1 = criar_saudacao("Olá", "Gabriel");
saudacao_2 = criar_saudacao("Tchau", "Gabriel");
print("Sem closure:");
print(saudacao_1);
print(saudacao_2); 

print("Com closure:");
print(saudacao_1());
print(saudacao_2());