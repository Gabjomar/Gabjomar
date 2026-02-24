'''
Introdução ao try/except.
try - Tentar executar o código.
except - Ocorreu algum erro, que não de sintaxe, de erro de digitação 
no código, ao tentar executar.

"Estourar uma exceção", "Aparecer uma exceção" ou "Levantar uma exceção"
é quando ocorre um erro.
'''
# input() sempre retorna uma string.
numero_str = input("Vou dobrar o número que você digitar: ");

# Sempre que o usuário te mandar um valor, você precisa tratar esse valor.

# Verifica se é APENAS NÚMEROS
#print(numero_str.isdigit());

if numero_str.isdigit():
    numero_float = float(numero_str);
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}');
else:
    print('Isso não é um número');


# if checa uma condição e muda o fluxo do código. Não evita erros/exceções.
# try/except evita erros/exceções.

try:
    print('STR:', numero_str);
    numero_float = float(numero_str);
    print('FLOAT:', numero_float); # Perceba que ele pulou para o except quando ocorre uma exceção.
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}');
except:
    print('Isso não é um número');