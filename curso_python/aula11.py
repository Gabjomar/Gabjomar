'''
Precedência entre os operadores aritméticos.

1º) "()"
2º) "**"
3º) "*", "/", "//", "%" 
4º) "+", "-"
'''
conta_0 = 1 + 1 ** 5 + 5;
print(conta_0);
conta_1 = (1 + 1) ** 5 + 5;
print(conta_1);
conta_2 = (1 + 1) ** (5 + 5);
print(conta_2);
