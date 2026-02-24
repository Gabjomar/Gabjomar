'''
Escopo de funções em Python.
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
'''

# Call stack = Pilha de chamadas - Forma como o interpretador organiza o funcionamento de códigos com funções, criando diferentes locais na memória
# para atribuir os valores de diferentes escopos, sendo organizado de forma hierárquica, priorizando os escopos mais internos dos mais externos,
# empilhando por último os mais internos. Após isso, é necessário resolver esses escopos, precisando desempilhá-los retirando primeiro os últimos 
# que foram adicionados, como uma pilha de pratos.
# Com esse sistema de organização que é possível existir variáveis diferentes com o mesmo nome em escopos distintos no código sem ocorrer problemas
# de organização por parte do interpretador. 
# Esse sistema é utilizado na grande maioria das linguagens de progrmação.
# Possível perceber esse funcionamento com a ferramenta de debugger do Visual Studio Code.
