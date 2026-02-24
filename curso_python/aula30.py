'''
Constante = "Variáveis" que não vão mudar.
No python não existe tecnicamente constantes, como em outras linguagens 
de programação "const xxx", porém existe uma convenção de que variáveis 
com letras maiúsculas são constantes, para indicar para as outras pessoas
que aquilo não deve ter o seu valor alterado.

Lembre-se: "Você está escrevendo o seu código para ser legível para outras
pessoas entenderem, ou você do futuro".
Algumas boas práticas de programação:
    Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) - Muito tab dentro de tab.
"Simples é melhor do que complexo".
"Explícito é melhor do que implícito".
'''

velocidade = 61; # Velocidade atual do carro.
local_carro = 101 # Local em que o carro está na estrada.

RADAR_1 = 60 # Velocidade máxima do radar 1.
LOCAL_1 = 100 # Local onde o radar 1 está.
RADAR_RANGE = 1 # A distância onde o radar pega.

velocidade_carro_passou_radar_1 = velocidade > RADAR_1;
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1;

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do limite do radar 1');

if carro_multado_radar_1:
    print('Carro multado em radar 1');
