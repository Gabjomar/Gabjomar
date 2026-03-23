'''
Modularização de códigos no Python.

Pacotes são pastas que contém módulos Python dentro delas.
Pacotes e módulos servem para para organizar o seu código, tornar ele mais fácil de entender e utilizar diferentes partes dele posteriormente.

Todo módulo python tem a extensão ".py". Tome cuidado para não nomear os seus módulos com nomes que são utilizados para os módulos padrão do Python, como por exemplo, o módulo "sys".

Entendendo os seus próprios módulos Python.
O primeiro módulo executado no Python chama-se __main__. Os módulos seguintes serão chamados pelos nomes dos módulos.
Você pode importar outro módulo inteiro ou parte do módulo.
O Python conhece a pasta onde o __main__ está e as pastas abaixo dele. Ele não reconhece opastas e módulos acima do __main__ por padrão.
O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path.
'''
# Todas as formas de importações vistas na aula 106 continuam funcionando:
import aula107_m;
from aula107_m import variavel_modulo_1, soma_0; # É possível importar classes, funções, variáveis, etc.

print(aula107_m.variavel_modulo_0);
print(variavel_modulo_1);

print(aula107_m.soma_1(2,3,7));
print(soma_0(23,1));