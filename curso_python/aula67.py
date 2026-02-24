'''
Valores padrão para parâmetros.
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro quando a função for chamada, o valor 
padrão será usado para executar a função.

Refatorar = Editar o seu código.

"Um código nunca está pronto, sempre é possível realizar uma atualização para melhorá-lo."
'''

def soma(x, y, z = 0): # 0 é considerado um valor False.
    if z:
        print(f"{x=} {y=} {z=}", x + y + z);
    else:
        print(f"{x=} {y=}", x + y);

soma(1,3);
soma(1,3,0); # Atribuiu um argumento na função porém 0 é considerado um valor False (interpretado como False ou invés de True no tipo boolean).


# Quando usa None, passamos a ter uma verificação se o valor foi enviado ou não, pois quando um valor qualquer é enviado, seja 0, False, a função
# não interpretará ele como None.
# Obs.: É possível fazer essa mesma lógica para qualquer outro valor padrão diferente de None, basta usar "if ... is not ...".
def soma1(x, y, z = None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z);
    else:
        print(f"{x=} {y=}", x + y);

soma1(1,3);
soma1(1,3,0); # Agora o z aparece, ou seja, o uso de valor padrão None é útil para os casos onde você deseja saber se algum argumento não foi
              # enviado quando determinada função foi chamada.

# Como vimos, não pode usar parâmetro posicional após usar parâmetro nomeado, precisará ser parâmetro nomeado.
# def soma2(x, z = None, y):