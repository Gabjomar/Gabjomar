'''
Como o for funciona por baixo dos panos? 
Iterável -> str, range, etc.
Iterador -> Quem sabe entregar um valor por vez.
next -> me entregue o próximo valor.
iter -> me entregue seu iterador.

Iterável é um objeto que possui o método __iter__ (como se fosse o .inter()).
'''

#"__" (dois underscores/underlines seguidos) é chamado de "thunder".

texto = 'Luiz'.__iter__(); # Não é mais uma string, agora é um elemento que sabe entregar um valor, é um iterador.
print(texto);
texto = iter('Luiz'); # Essa função faz a mesma coisa que o ".__iter__()".
print(texto);

print(texto.__next__());
print(texto.__next__());
print(texto.__next__());
print(texto.__next__());
#print(texto.__next__()); # StopIteration - Pare a iteração.

texto = 'For_Raiz'; # Iterável.
iterador = iter(texto); # Iterador.

while True: # Como for funciona por baixo dos panos
    try:
        letra = (next(iterador));
        print(letra);
    except StopIteration: # Escolhe um erro específico para algo ser feito.
        break;