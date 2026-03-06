'''
try e except para tratar exceções.
'''
a = 3;
b = 0;

try:
    print("Aqui será executado, pois não ocorreu nenhum erro.");
    c = a / b; 
    print("Já aqui não será executado nunca quando ocorrer algum erro na linha anterior, pois quando ocorre o erro em alguma linha dentro do 'try', o código já pula para o 'except' " \
    "correspondente");
except ZeroDivisionError as e:
    print(e.__class__.__name__);
    print(e);
except (TypeError, IndexError) as error: # É possível criar uma variável para receber a instância do erro que ocorreu para usarmos no código de tratativa desse erro.
    print('TypeError + IndexError');
    print('MSG:', error); # Com a criação dessa variável, é possível identificar qual erro ocorreu nesse caso onde pode entrar nessa seção por conta de dois erros diferentes. A melhor prática é
                  # ter uma seção "except" individual para cada erro que poder ocorrer, mas aqui estamos mostrando as ferramentas existentes para fins didáticos.
    print('Nome:', error.__class__.__name__); # Com esse código meio específico ".__class__.__name__" você consegue pegar o nome do erro que ocorreu. Esse código pega o nome da instância
                                              # atribuída para a classe 'exception'.
except Exception:
    print('Erro desconhecido');