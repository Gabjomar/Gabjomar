'''
Por tudo no python ser um objeto, o objeto geralmente tem métodos dentro dele e esses métodos são basicamente funções que podem executar algumas ações 
colocando um "." depois dele. É isso que faremos aqui com o "format".

Quando uma função está dentro de um objeto, ela é chamada de "método".

'''

a = 'AAA';
b = 'B';
c = 1.1;
formato = 'a={} b={} c={}'.format(a, b, c); # Pega os argumentos de "format()" em ordem, da esquerda para a direita.
string_1 = 'a={} b={} c={}';
formato_1 = string_1.format(a, b, c); 
string_2 = 'b={1} b={2:.2f} c={0}';
formato_2 = string_2.format(nome1 = a, nome2 = b, nome3 = c); # Os índices começam do 0, então o índice de a é 0, de b é 1 e de c é 2.

print(formato);
print(formato_1);
print(formato_2);

# "Out of range" -> Erro que signifia que você está buscando por algo que já acabou.