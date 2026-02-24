'''
Operadores lógicos:
and (e)
or (ou)
not (não)

or - Qualquer condição verdadeira avalia toda a expressão como verdadeira. Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada
naquele valor (avaliação de curto circuito para verdadeiro).

São considerados falsy (que você já viu):
0
0.0
''
False

Também existe o tipo None que é usado para representar um não valor (só serve para isso mesmo, para representar o "nada").

'''


entrada = input('[E]ntrar [S]air: ');
senha_digitada = input('Senha: ') or 'Sem senha';

senha_permitida = '12345';
if ((entrada == 'E') or (entrada == 'e')) and (senha_digitada == senha_permitida):
    print('Entrar');
else:
    print('Sair');



print(True or False or 0 or 'abc');