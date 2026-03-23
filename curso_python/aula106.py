'''
Módulos padrão do Python (import, from, as e *).
https://docs.python.org/3/py-modindex.html

inteiro - import nome_modulo
Vantagens: Você tem o namespace do módulo.
Desvantagens: Nomes grandes.
'''

import sys; # <- Esse é o namespace do módulo.

platform = 'A MINHA';
print(sys.platform);
print(f'{platform=}');

'''
partes - from nome_modulo import objeto1, objeto2
Vantagens: Nomes pequenos.
Desvantagens: Sem o namespace do módulo.
'''

from sys import exit, platform; 

print(f'{platform=}'); # Não precisa mais escrever o namespace do módulo.
platform = 'A MINHA';
print(f'{platform=}'); # Perceba que agora precisa ter cuidado com os nomes escolhidos, pois você pode sobrescrever eles, visto que não tens a proteção de ter importado o namespace do módulo.

'''
alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import objeto as apelido
Vantagens: Você pode reservar nomes para o seu código.
Desvantagens: Pode ficar fora do padrão da linguagem.
'''

import sys as sistema;
sys = 'Alguma coisa';
print(sys.upper()) # "sys" agora é uma string e não o namespace de um módulo. Se não tivesse utilizado importado com alias, o namespace do módulo teria sido sobrescrito e você perderia
                      # o acesso a ele. Então esse é um exemplo de utilização dessa forma de importar módulos, quando você deseja utilizar o nome do namespace do módulo para outra coisa.

from sys import platform as pf;
from sys import exit as ex;

print(f'{pf=}');

'''
Má prática - from nome_modulo import *
Vantagens: Importa tudo de um módulo.
Desvantagens: Importa tudo de um módulo.

"*" -> Significa "all" (tudo);

É possível definir no módulo com a variável "__all__" o que vai ser importado quando for feito um "import *", sendo uma medida para contornar essa má prática.
'''

from sys import *; # Faz o código ficar obscuro, tem diversos nomes que fazem ações que não estão claramente definidas e também gera o risco de nomes utilizados no módulo serem sobrescritos
                   # sem ninguém perceber.

print(f'{platform=}');
