'''
Repetições.

'''

contador = 0;

while contador <= 20:
    contador += 1;

    if contador == 6:
        print('Pulo o 6');
        continue; # Tudo até o continue executou normal, depois do continue, ele finaliza a repetição atual do laço e inicia a próxima, se a condição for True.
    
    if (contador >= 9) and (contador <= 14):
        print(f'Não vou mostrar o {contador}');
        continue;
    
    print(contador);

    if contador == 18:
        break;

print('Acabou');