'''
Interpolação básica de strings - Uma outra opção para utilizar ao invés de
f strings.
s - string.
d e i - int.
f - float.
x e X - Hexadecimal (ABCDEF0123456789).
x - gera um hexadecimal minúsculo.
X - gera um hexadecimal maiúsculo.
'''
nome = 'Gabriel';
preco = 35.244256;
variavel = '%s, o preço é R$%.2f' % (nome, preco);
variavel_1 = '%s, o preço é R$%.4f' % (nome, preco);
print(variavel);
print(variavel_1);

print('O hexadecimal de %d é %04X' % (250, 250));
print('O hexadecimal de %d é %X' % (250, 250));
