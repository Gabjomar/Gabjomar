'''
for loop -> Mais usado quando sabemos quando o laço irá acabar.
while loop -> Mais usado quando não sabemos quando o laço irá acabar.
'''

senha_salva = '12345';
senha_digitada = '';
repetições = 0;

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repetições}x): ');
    repetições += 1;

print(repetições);
print('Aquele laço acima pode ter repetições infinitas');

texto = 'Python';
novo_texto = '';


for letra in texto: # "Para cada letra (variável que estou criando) no texto (em um objeto interável), faça:"
    novo_texto += f'*{letra}';
    print(letra);
print(novo_texto + "*");