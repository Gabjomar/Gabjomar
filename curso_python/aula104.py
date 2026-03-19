'''
try, except, else e finally.

Segue um link da documentação do python sobre os diferentes tipos de exceções existentes na linguagem, que permite você tratar cada uma dessas exceções/erros de forma específica:
https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

finally - Um bloco que sempre será executado no seu try / except, mesmo que ocorra um erro no bloco do try. Uma utilidade desse bloco é quando você quer tentar abrir um arquivo, fazer
alguma operação e sempre queres fechar esse arquivo, mesmo que ocorra um erro durante a operação, então podes utilizar o finally para garantir que o código irá sempre fechar o arquivo.

else - Um bloco que é executado quando o bloco do try é executado sem erros. Não tem muita utilidade prática, mas é importante saber que existe.

try não pode ficar sozinho, podem haver diversas combinações de blocos, como por exemplos:
try + except
try + finally
try + except + finally
try + else + finally
try + except + else + finally

Obs.: Podes ter quantos blocos de except você quiser.
'''

try:
    print('Abrir o arquivo');
    8/0;
except ZeroDivisionError:
    print('Dividiu por zero');
else:
    print('Não deu erro');
finally:
    print('Fechar o arquivo'); # Perceba que quando você não trata explicitamente o erro específico que ocorreu no bloco do try, as informações do erro no terminal só aparecem depois do 
                               # bloco do finally ter sido executado.