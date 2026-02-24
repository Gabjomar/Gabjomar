'''
Operação ternária (condicional de uma linha).
<valor> if <condição> else <outro valor>.

Útil para quando precisa fazer um if curto, de apenas uma linha, deixando o código mais enxuto.
'''
print('Valor' if True else 'Outro valor');
print('Valor' if False else 'Outro valor');

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor';
print(variavel);

digito = int(input("Digito: "));
novo_digito = digito if digito <= 9 else 0;
print(novo_digito);

condicao_1 = False

aglomerado = 'Valor' if condicao else 'Outro valor' if condicao_1 else 'Fim'; # Pode ir acrescentando a operação ternária, porém é uma má prática de programação.

print(f'aglomerado: {aglomerado}');