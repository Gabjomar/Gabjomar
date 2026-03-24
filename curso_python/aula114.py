'''
Variáveis livres + nonlocal.

Variáveis livres (free variables) - Variáveis que não são definidas dentro do escopo da função onde ela é utilizada.

Existem as funções "locals" e "globals" que mostra quais variáveis são locais e quais são globais.
'''

def fora(x):
    a = x; # Essa é uma variável livre pois não está definida dentro do escopo da função onde ela é utilizada.

    def dentro():
        print(locals());
        # print(dentro.__code__.co_freevars); # Outra forma de verificar as variáveis livres de determinada função.
        return a;
    return dentro;

dentro_0 = fora(10);
dentro_1 = fora(20);

print(dentro_0());
print(dentro_1());

### ---------- ###

# Essa função não é nada eficiente, ela foi construída dessa maneira para ser didática com o conteúdo que se deseja apresentar.
def concatenar(string_inicial):
    valor_final = string_inicial;

    def interna(valor_a_concatenar):
        # Fazer isso sem utilizar o "nonlocal" gerará um erro "UnboundLocalError: cannot access local variable 'valor_final' where it is not associated with a value", pois "valor_final" é 
        # uma variável livre que a função "interna()" não pode alterar, só pode visualizar/consultar o seu valor.

        nonlocal valor_final; # O "nonlocal" indica para o Python que é necessário buscar no escopo acima a variável informada para realizar alterações no valor dessa váriavel, não se
                              # tratando nem de uma variável global nem local, se tratando de uma variável "nonlocal".
        valor_final += valor_a_concatenar; 
        return valor_final;
    return interna;

funcao_0 = concatenar('a');

print(funcao_0('b'));
print(funcao_0('c'));
print(funcao_0('d'));

