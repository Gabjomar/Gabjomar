'''
Calculadora com while.

'''

while True:
    primeiro_numero = input("Primeiro número: ");
    segundo_numero = input("Segundo número: ");
    operador = input("Operador (+-/*): ");

    numeros_validos = None;
    primeiro_numero_float = 0; # Definindo varíavel fora do bloco. Boa prática de programação quando se deseja utilizar a variável posteriormente.
    segundo_numero_numero_float = 0;

    try:
        primeiro_numero_float = float(primeiro_numero);
        segundo_numero_numero_float = float(segundo_numero);
        numeros_validos = True;
    except:
        ...

    if numeros_validos is None:
        print("Um ou ambos os números digitados não são válidos.");
        continue;
    
    operadores_permitidos = '+-/*';

    if (operador not in operadores_permitidos) or (len(operador) > 1):
        print("Operador inválido.");
        continue;
    
    if operador == '+':
        resultado = primeiro_numero_float + segundo_numero_numero_float;
    elif operador == '-':
        resultado = primeiro_numero_float - segundo_numero_numero_float;
    elif operador == '*':
        resultado = primeiro_numero_float * segundo_numero_numero_float;        
    elif operador == '/':
        resultado = primeiro_numero_float / segundo_numero_numero_float;    

    print(f"Resultado: {resultado}");

    sair = input("Quer sair? [s]im: ").lower().startswith('s');
    if sair:
        break;

    
