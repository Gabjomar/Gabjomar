'''
Closure (fechamento) e funções que retornam outras funções.
'''

# Com isso, estamos criando uma função que cria outras funções.

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}";
    return saudar; 

falar_ola = criar_saudacao("Olá");
falar_tchau = criar_saudacao("Tchau");

print(falar_ola("Gabriel")); 
print(falar_tchau("Gabriel"));

for nome in ['Maria', 'Vanessa', 'Gustavo']:
    print(falar_ola(nome));

# Muito massa!!! Genial!!!