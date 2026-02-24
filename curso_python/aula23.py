'''
Operadores lógicos:
and (e)
or (ou)
not (não)

not - Inverte expressões.

not True = False.
not False = True.

'''
senha = input('Senha: ');

if senha == '123456':
    print('Senha correta');
elif not senha:
    print('Você não digitou nada');

print(not True); # False.
print(not False); # True.
