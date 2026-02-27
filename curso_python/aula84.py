'''
Exemplo de uso de sets (conjuntos).
'''

# Nesse caso, armazenar as letras no set irá economizar espaço na memória e tempo, pois não irá ficar adicionando valores repetidos nele, mesmo que
# o usuário fique digitando a mesma coisa sempre, evitando que tenha que criar um bloco de código auxiliar para excluir valores duplicados e que
# tenha que usar uma outra estrutura de dados mais pesada e desnecessariamente mais complexa, com índices, etc.

letras = set();

while True:
    letra = input("Digite: ");
    letras.add(letra.lower()); # Você ainda pode enxutar as possibilidades de letras enviadas pelo usuário tratando os dados que ele enviar, como 
                               # obrigando ele a digitar apenas 1 letra, transformando todos os valores em letras maiúsculas ou minúsculas, etc.

    if "l" in letras: # Vai jogando os valores dentro da "sacola" (set) e depois você busca o que deseja dentro dele. Esse é um dos principais usos
                      # desse tipo de estrutura de dado.
        print("Parabéns!!!");
        break;
    
    print(letras);
