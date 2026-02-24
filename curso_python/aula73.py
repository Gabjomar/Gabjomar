'''
Higher Order Functions / First-Class Functions.
Funções de primeira classe.

"As funções no Python podem ser tratadas como qualquer outro tipo de dado".
"As funções no Python são da mesma classe que qualquer outra variável".

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções.

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...).

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
'''

def saudacao(msg):
    return msg;

print(saudacao("Hello World!"));

v = saudacao("Hello World!");
print(v);

saudacao_2 = saudacao; # Referenciando uma outra função para ter o mesmo funcionamento de uma função já existente, se tornando a mesma função na
# memória do computador.

print(saudacao_2("Eita!"));

def executa(funcao, msg):
    return funcao(msg);

# Obs.: Não é uma boa prática de programação ficar abreviando os nomes de variáveis e funções, deixa o código mais difícil de ser interpretado.
v = executa(saudacao_2, "Eita!!!");
print(v);

def saudacao_final(msg, nome):
    return f"{msg}, {nome}!";

def executa_final(funcao, *args):
    return funcao(*args);

v = executa_final(saudacao_final, "Eae", "Júnior");
print(v);