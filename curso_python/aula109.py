'''
Recarregando módulos, importlib e singleton.

Módulos no Python são "singletons".
'''


import aula109_m;

print(aula109_m.variavel_modulo_0);

# Perceba que a importação só acontece uma única vez, pois o "import" é um "single", ou seja, só pode existir uma instância desse "import" em toda a execução do programa. O Python salvou
# esse "import" na memória, e toda vez que você solicitar o "import" desse módulo, ele não irá importar de novo o módulo por questão de eficiência, as informações presentes naquele módulo
# importado já estarão disponíveis para serem utilizadas. Essa característica ocorre pois os módulos no Python são "singletons".
for i in range(5):
    print(i);
    import aula109_m; 

print('Fim do primeiro for');
print();

# Não é muito comum, mas se você realmente precisar que o código funcione da maneira como foi esperada no for acima, é possível utilizar a seguinte biblioteca:
import importlib;

for i in range(5):
    print(i);
    importlib.reload(aula109_m); 
    # Com essa função, o Python irá recarregar o módulo inteiro, gerando o comportamento que era esperado inicialmente, sendo feito dessa maneira mais específica, pois se trata de um 
    # processo mais ineficiente do Python executar esse código.

print('Fim do segundo for');

