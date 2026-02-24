'''
Introdução às funções (def) em Python.
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''

# def Print(a, b, c):
#     print('várias1');
#     print('várias2');

def imprimir(a, b, c): # Parâmetro -> "Variável" que será utilizada dentro da função.
    print(c, c, b, a, b);

imprimir(1, 2, 3); # Argumento -> Valor que é atribuido nas variáveis que serão usadas na função quando a função é chamada.
imprimir(4, 5, 6);

# Agora foi atribuído um valor padrão para o argumento da função, assim, mesmo se não for definido nenhum argumento na hora de chamar a função, 
# a função executará utilizado o valor padrão.
def saudacao(nome = "Sem nome"): 
    print(f"Olá, {nome}!");

saudacao("Gabriel");
saudacao("Maria");
saudacao(); # Função sendo executada com o argumento padrão.

def multiplo_de(numero, multiplo):
    resultado = (numero % multiplo) == 0;
    print(f'{numero} é múltiplo de {multiplo}?', end=' ');
    print(resultado);
 
 
multiplo_de(16, 8);
multiplo_de(15, 3);
multiplo_de(10, 2);