'''
Iterando strings com while.

'''
#       0123456
nome = 'Gabriel' # Iteráveis.
tamanho_nome = len(nome);
i = 0;

while i < tamanho_nome:
    letra = nome[i]; # Adaptação para conseguir fazer o código, pois atribuir direto "nome[i] = xxx" resulta em erro, não pode, pois como vimos, string é um tipo imutável.
    letra = '*' + nome[i];
    print(letra, end='');
    i += 1;