'''
Valores Truthy e Falsy, Tipos Mutáveis e Imutávels.

Valores específicos de determinados tipos de dados que serão considerados True ou False quando forem transformados no tipo bool. 

Tipos Mutáveis: [] {} set().
Tipos Imutáveis: () "" 0 0.0 None False range(0, 10).
'''

# Todos esses valores são Falsy (False) - Tudo que houver um valor dentro ou for diferente disso, será Truthy (True).
lista = [];
dicionario = {};
tupla = ();
conjunto = set();
string = '';
inteiro = 0;
flutuante = 0.0;
nada = None; # Não tem inverso de None, ao contrário de False <-> True.
falso = False;
intervalo = range(0);
lista_0 = [0];

def falsy(valor):
    return 'falsy' if not valor else 'truthy';

print(f'TESTE', falsy('TESTE'));
print(f'{lista=}', falsy(lista));
print(f'{dicionario=}', falsy(dicionario));
print(f'{tupla=}', falsy(tupla));
print(f'{conjunto=}', falsy(conjunto));
print(f'{string=}', falsy(string));
print(f'{inteiro=}', falsy(inteiro));
print(f'{flutuante=}', falsy(flutuante));
print(f'{nada=}', falsy(nada));
print(f'{falso=}', falsy(falso));
print(f'{intervalo=}', falsy(intervalo));
print(f'{lista_0=}', falsy(lista_0));