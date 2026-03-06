'''
Try, except, else e finally.

Exceção = Erro. Exceção é uma classe. A padronização dos nomes de classe deve ser de acordo com o "Pascal case", toda palavra deve ter letra maiúscula, como "ZeroDivisionError", apesar 
disso, existem algumas nomes de classe que não seguem esse padrão '-'.
'''

a = 18;
b = 0;

# c = a / b; # Esse código pode gerar um erro, como b = 0.

# Aqui tem uma má prática de programação, pois aqui estamos silenciando um erro e não estava fazendo nada com esse erro. Na verdade, qualquer outro erro que acontecer nessa linha de código
# foi silenciada e não será feito nada, como "a" ser uma string, etc.

# try:
#     print("Aqui será executado, pois não ocorreu nenhum erro.");
#     c = a / b; 
#     print("Já aqui não será executado nunca quando ocorrer algum erro na linha anterior, pois quando ocorre o erro em alguma linha dentro do 'try', o código já pula para o 'except'");
# except: # Aqui será tratado o erro apresentado dentro do try, seja inserir as informações em um log, solicitar alterações para o usuário, etc.
#     print('Dividiu por zero.'); 

try:
    print("Aqui será executado, pois não ocorreu nenhum erro.");
    c = a / b; 
    print("Já aqui não será executado nunca quando ocorrer algum erro na linha anterior, pois quando ocorre o erro em alguma linha dentro do 'try', o código já pula para o 'except'");
except ZeroDivisionError: # Aqui será tratado o erro apresentado dentro do try, seja inserir as informações em um log, solicitar alterações para o usuário, etc.
    print('Dividiu por zero.'); 
except NameError: # Agora estamos tratando dois erros específicos de maneiras distintas (poderíamos tratar de maneiras distintas).
    print('Variável a e/ou b não estão definidas.'); 
except (TypeError, IndexError): # É possível adicionar uma tupla para utilizar uma mesma tratativa para duas ou mais exceções diferentes.
    print('TypeError + IndexError');
except Exception: # Essa é a maior classe de erro/exceção do Python, acima dela não tem nenhum outro erro. Ou seja, o código a seguir é para tratar qualquer outro erro diferente dos 
                  # especificados nas linhas anteriores.
    print('Erro desconhecido');

