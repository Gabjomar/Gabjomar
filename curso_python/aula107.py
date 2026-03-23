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

O seu primeiro módulo "__main__" é o ponto de entrada daquele código.
'''
import sys; # É uma boa prática separar a importação de módulos padrão do Python dos seus módulos.

# É possível importar dessa maneira pois é um módulo que está no mesmo caminho que esse módulo que está executando o código.
import aula107_m; # Quando o módulo é importado, o código nele já é executado.

print('Este módulo se chama', __name__);

print(*sys.path, sep='\n');

# É possível adicionar caminhos no computador que o Python passa a reconhecer e a obter os módulos presentes nesse caminho, por meio do comando:
sys.path.append('C:\Users\gabjo\OneDrive\Área de Trabalho')
# Porém não é uma forma comum de se fazer essa modularização do seu código, o mais comum e usual é você construir seu módulos ao redor e abaixo do primeiro módulo "__main__".


