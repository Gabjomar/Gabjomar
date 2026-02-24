'''
Formatação básica de strings.
s - string.
d - int.
f - float.
.<número de dígitos depois da vírgula>f.
x ou X - Hexadecimal minúsculo ou maiúsculo.
(Caractere)(<>^)(quantidade).
> - Esquerda.
< - Direita.
^ - Centro.
= - Força o sinal a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
!r - Chama o método __repr__
!s - Chama o método __str__
!a - Chama o método __asc__ (ascii)
'''

variavel = 'ABC';
print(f'{variavel}');
print(f'{variavel: >10}');
print(f'{variavel: <10}.');
print(f'{variavel:_^10}');

print(f'{1002.3523912372672:.1f}');
print(f'{1002.3523912372672:,.1f}');
print(f'{-1002.3523912372672:,.1f}');
print(f'{1002.3523912372672:+,.1f}');
print(f'{1002.3523912372672:0>+10,.1f}');
print(f'{1002.3523912372672:0=+10,.1f}');
# Não é preciso saber faszer isso, é desnecessariamente complexo.

print(f'O hexadecimal de 1500 é {1500:08x}');
print(f'O hexadecimal de 1500 é {1500:08X}');

print(f'{variavel!a}');