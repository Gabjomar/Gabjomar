'''
Função lambda no Python + método sort e função sorted para listas.

A função lambda é uma função como qualquer outra em Python, porém são funções anônimas (sem definir nome) que contém apenas uma linha. Ou seja,
tudo deve ser contido dentro de uma única expressão.

Obs.: A ordenação do Python é feito com base na tabela unicode, para conseguir ordenar caracteres especiais, números, letras maiúsculas, letras
minúsculas, etc.
'''

print("Função sorted()");

lista_0 = [4, 32, 1, 34, 5, 6, 6, 21, ];

lista_ordenada_crescente = sorted(lista_0); # Função sorted() faz uma cópia rasa do valor enviado para ela.
lista_ordenada_decrescente = sorted(lista_0, reverse=True);

print(f"{lista_ordenada_crescente=}");
print(f"{lista_ordenada_decrescente=}");

lista_0.sort();
print(f"{lista_0=} Modificada para ficar em ordem crescente via método sort");

lista_0.sort(reverse=True);
print(f"{lista_0=} Modificada para ficar em ordem decrescente via método sort");

lista_1 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
];

# Agora fazer a ordenação de uma lista com dicionários é difícil, pois o Python não vai conseguir definir uma regra para fazer a ordenação, por
# isso que em casos como esse você pode adicionar uma função lambda dentro de um método/função para definir como o método/função deve funcionar.
# No caso será enviado item por item como argumento para a sua função lambda.

# Forma de fazer sem função lambda, utilizando funções tradicionais:

def ordena(item): 
    return item['nome']; # Agora a ordenação está se baseando nos valores da chave 'nome' em cada dicionário.

lista_1.sort(key=ordena);
print(f"{lista_1=}");

def ordena(item): 
    return item['sobrenome']; # Agora a ordenação está se baseando nos valores da chave 'sobrenome' em cada dicionário.

lista_1.sort(key=ordena);
print(f"{lista_1=}");

# Forma de fazer com função lambda, sendo mais enxuto e eficiente:

lista_1.sort(key=lambda item: item['nome']); # Não coloca o nome da função nem parênteses, "lambda" é o equivalente ao "def" e já define direto os
                                             # parâmetros da função e, por definição, depois dos ":" já irá retornar o que estiver apresentado no
                                             # código sem precisar usar "return". É a mesma ideia de fazer uma função tradicional, só que com regras
                                             # de escrita específicas para deixar mais enxuto, possibilitando escrever tudo em uma única linha 
                                             # e expressão.
print(f"{lista_1=}");

lista_1_ordenada_descrescente_por_sobrenome = sorted(lista_1,key=lambda item: item['sobre   nome']);
print(f"{lista_1_ordenada_descrescente_por_sobrenome=}");
