'''
Operadores lógicos:
and (e)
or (ou)
not (não)

and - Todas as condições precisam ser verdadeiras. Se qualquer valor for considerado falso (falsy), a expressão inteira será avaliada naquele valor.

São considerados falsy (que você já viu):
0
0.0
''
False

Também existe o tipo None que é usado para representar um não valor (só serve para isso mesmo, para representar o "nada").

'''
'''
entrada = input('[E]ntrar [S]air: ');
senha_digitada = input('Senha: ');

senha_permitida = '12345';
if (entrada == 'E') and (senha_digitada == senha_permitida):
    print('Entrar');
else:
    print('Sair');
'''

# Avaliação de curto circuito para falso, checa só até onde ele precisa
print(True and False and True);

print(bool(0));     # False
print(bool(''));    # False
print(bool(' '));   # True