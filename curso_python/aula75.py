'''
Exercícios:

Crie funções que duplicam, triplicam, quadriplicam o número recebido como parâmetro.
'''

def criar_multiplicador(quantidade_de_duplicacao):
    def multiplicar(numero_a_ser_duplicado):
        return numero_a_ser_duplicado * quantidade_de_duplicacao;
    return multiplicar;

# Reduz uma quantidade enorme de linhas quando aplicado a funções complexas com lógicas semelhantes, que tem partes do algoritmo que se repetem, 
# fazendo com que se consiga aproveitar um código base e adaptar essa base para uma função específica em uma única linha, como mostrado abaixo:
duplica = criar_multiplicador(2);
triplica = criar_multiplicador(3);
quadruplica = criar_multiplicador(4);

print(duplica(2));
print(triplica(2));
print(quadruplica(2));

print(duplica(12));
print(triplica(12));
print(quadruplica(12));