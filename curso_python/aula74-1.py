'''
Closure (fechamento) e funções que retornam outras funções.
'''

# A modificação feita faz o parâmetro "nome" ser adiado no código, fazendo com que agora não seja mais necessário salvar na memória o valor da
# variável "nome" quando ocorre o atraso proposital da execução da função "saudar()".

# Isso faz com que o código seja mais generalista, fazendo o parâmetro "nome" ser atribuído a valores dinâmicos.

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}";
    return saudar; 

saudacao_1 = criar_saudacao("Olá");
saudacao_2 = criar_saudacao("Tchau");
print("Sem closure:");
print(saudacao_1);
print(saudacao_2); 

print("Com closure:");
# Agora o argumento para o parâmetro "nome" é enviado aqui.
print(saudacao_1("Gabriel")); 
print(saudacao_2("Gabriel"));