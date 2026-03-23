'''
"Packages" (pacotes) no Python são pastas que contém "modules" (módulos) Python dentro delas.

A melhor forma de se organizar um programa Python que será modularizado é ter um arquivo/módulo que será o primeiro a ser executado, ou seja, será o seu "__main__", 
como porta de entrada, estando devidamente localizado em um caminho acima ou adjacente aos outros "modules"/"packages" que você precisará importar.

Quando é feita a importação de algo em um módulo no Pyhon, esse algo também fica disponível para ser exportado por meio desse módulo.

Dica para não se incomodar com problemas de escopo de importação: 
Quando for criar um programa, faça todas as importações desse programa estarem relacionadas a partir do ponto de vista do seu arquivo/módulo "__main__", ou seja, 
faça a importação de módulos em outros módulos que não são o seu "__main__" serem descritivas o suficiente para o Python conseguir realizar a importação do ponto de 
vista do seu "__main__".
'''

from sys import path;
import aula110_package; # Importar o package não faz nada, não tem o que fazer.

# É possível realizar a importação do módulo de todas as maneiras que vimos anteriormente na aula 106.
import aula110_package.modulo; # Assim para utilizar o que desejas precisa digitar bastante.
from aula110_package import modulo; # Assim para utilizar o que desejas precisa digitar menos.
from aula110_package.modulo import soma_0; # Assim para utilizar o que desejas precisa digitar bem pouco.

# print(*path, sep='\n');
print(aula110_package.modulo.soma_1(3, 10, 50));
print(modulo.subtracao_0(10,3,5));
print(soma_0(3, 7));

