'''
"__init__.py" é um arquivo/módulo de inicialização dos packages em Python.

"thunder" = "__".
'''

import aula110_package;
# Como vimos antes, a princípio não acontece nada. Porém se for criado o arquivo "__init__.py" dentro desse package, dai o código presente nesse arquivo/módulo será 
# executado toda vez que qualquer coisa for importada nesse package, incluindo os módulos dentro desse package e o próprio package.

# A criação desse arquivo "__init__.py" dentro de um package faz o package acabar se comportando como um módulo com o código que está dentro desse arquivo 
# "__init__.py", enganando o Python.

print(aula110_package.dobra(4));

# O princípio de você importar algo em um módulo fazer esse algo ficar disponível para ser exportado a partir desse módulo continua sendo válido para esse módulo
# "__init__.py", ou seja, você pode fazer importações nesse arquivo para disponibilizar tudo que desejares por meio somente da importação de um package.
print(aula110_package.subtracao_0(10,5,10));