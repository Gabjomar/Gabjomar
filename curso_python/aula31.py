'''
Flag (Bandeira) - Marcar um local.
None = Não valor.
is e is not = "é" ou "não é" (tipo, valor, identidade).
id = Identidade.
'''

v1 = 'a';
v2 = 'a';
print(id(v1));
print(id(v2));
# As duas variáveis apontam para o mesmo valor da memória, pois possuem o
# mesmo id (mesma identidade).

condicao = False;
passou_no_if = None; # Definindo a bandeira.

# Verificar se o interpretador passou por determinado caminho.
# O "passou_no_if" é a flag (bandeira).

if condicao:
    passou_no_if = True; # Demarcando determinado local, no caso o if.
    print('Faça algo');
else:
    print('Não faça algo');

print(passou_no_if, passou_no_if is None);
print(passou_no_if, passou_no_if is not None);
print(passou_no_if, passou_no_if == None);

# É mais utilizado "is" e "is not" para trabalhar com "None", ao invés de
# "==" e "!=".

if passou_no_if is None:
    print('Não passou no if');

if passou_no_if is not None:
    print('Passou no if');