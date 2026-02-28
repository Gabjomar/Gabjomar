'''
List comprehension em Python.
List comprehension é uma forma rápida para criar listas a partir de iteráveis.
'''

print(list(range(10))); # Vamos fazer um exemplo básico para pegar a ideia onde o resultado será a mesma coisa que essa linha de código entrega.

lista = [];

for numero in range(10):
    lista.append(numero);

print(f'{lista}');

# Agora iremos utilizar list comprehension para fazer a mesma coisa que fizemos acima, só que de forma mais enxuta.

# O detalhe para fazer o list comprehension funcionar é que precisa colocar à esquerda do for o que você deseja adicionar com cada número/iterável 
# no range(10).
lista_1 = [1 for numero in range(10)]; # Isso é list comprehension, adicionar código dentro da lista para com esse código adicionar valores à lista.
print(f'{lista_1}');

lista_2 = [numero for numero in range(10)]; 
print(f'{lista_2}');

lista_3 = [
    numero*2 for numero in range(10)
    ]; 
print(f'{lista_3}');

# Exemplo básico de como você pode ir adicionando lógica e complexidade às ferramentas apresentadas:
lista_4 = [
    numero % 2 
    for numero 
    in range(10)
    ]; 
print(f'{lista_4}');