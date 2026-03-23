'''
raise - Lançando/relançando exceções (erros).
https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

"Os programadores amam erros. Os erros são legais."

"O erro acontece quando o python não sabe o que fazer naquela situação, precisa retornar alguma coisa mas não pode assumir nada.
'''

# print(123);
# raise ValueError('Deu erro');
# print(456);

def dividir_0(n, d):
    try:
        return (n / d);
    except ZeroDivisionError:
        print('____');
        raise;

# Isso é um exemplo de má prática de programação, pois a sua função está fazendo mais coisas do que o nome dela descreve, no caso, ela está também tratando erros, então é sempre importante
# separar essas ações entre diferentes partes/funções do código. A dica de ouro é: "Se está difícil nomear a sua função com a ação que ela faz, é porque ela está fazendo muita coisa e 
# precisa ser fragmentada".

def dividir_1(n, d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero');
    return (n / d);

# print(dividir_1(8,0));

# Maneira mais interessante de programar esse código:

def dividir_2(n, d):
    não_aceito_zero(d);
    deve_ser_int_ou_float(n);
    deve_ser_int_ou_float(d);
    return (n / d);

def não_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero');

def deve_ser_int_ou_float(a):
    tipo_a = type(a);
    if not isinstance(a, (float,int)):
        raise TypeError(f'"{a}" deve ser int ou float \n' f'"{tipo_a.__name__}" enviado');
    return True;

print(dividir_2("b", 6));

