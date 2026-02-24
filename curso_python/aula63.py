'''
Possíveis problemas e soluções para o algoritmo verificador de cpf.
'''
import re;

while True:
    #cpf_enviado = input("Digite um CPF para ser verificado: ").replace(".","").replace("-",""); # Fica possível do usuário enviar o cpf com ponto e traço.
    # Outra forma de resolver o problema, só que mais abrangente e que irá apagar qualquer outro caractere que não seja um número.
    cpf_enviado = input("Digite um CPF para ser verificado: "); 

    cpf_enviado = re.sub(r'[^0-9]','',cpf_enviado); # Tudo que não for um caractere de 0 a 9 será substituído por "" (nada), será vazio.
    print(cpf_enviado);

    # Com essa expressões regulares (regular expression - re) é possível até escrever um textinho antes do cpf que ainda será possível fazer o cálculo.

    if len(cpf_enviado) != 11:
        print("Digite apenas um número de cpf completo");
        continue;
    
    # Pelo cálculo, um cpf 111.111.111-11, qualquer número repetido, é válido, só que na prática não deve ser, então precisamos verificar se o cpf enviado
    # é completo por números repetidos. Uma forma fácil de fazer isso é verificar se o valor recebido do usuário em formato de string pelo input é igual
    # a uma string que possui o mesmo tamanho do valor recebido onde todos os caracteres dessa string são o primeiro caractere do valor recebido.

    # string
    # ssssss

    # Se a string == ssssss, significa que toda a string é um único caractere repetidas vezes.

    teste_repeticao = cpf_enviado[0] * (len(cpf_enviado));
    
    print(teste_repeticao);

    if cpf_enviado == teste_repeticao:
        print("Digite um cpf válido e que não seja feito apenas de um número.");
        continue;

    i = 0;
    contador_regressivo_1 = 10;
    digito_verificador_1 = 0;
    while i < 9:
        try:
            numero_cpf_int = int(cpf_enviado[i]); 
            digito_verificador_1 += numero_cpf_int * contador_regressivo_1; # Mesma coisa que resultado = resultado + (numero_cpf_int * contador_regressivo)
            i += 1;
            contador_regressivo_1 -= 1;
        except:
            print("Digite apenas números");
            i = 10;
            continue;
    digito_verificador_1 = (digito_verificador_1 * 10) % 11;
    if i == 10:
        ...;
    
    digito_verificador_1 = digito_verificador_1 if digito_verificador_1 < 9 else 0;
    
    print(f"O primeiro dígito verificador é {digito_verificador_1}");
 
    i = 0;
    contador_regressivo_2 = 11;
    digito_verificador_2 = 0;
    while i < 10:
        numero_cpf_int = int(cpf_enviado[i]); 
        digito_verificador_2 += numero_cpf_int * contador_regressivo_2; # Mesma coisa que resultado = resultado + (numero_cpf_int * contador_regressivo)
        i += 1;
        contador_regressivo_2 -= 1;
    digito_verificador_2 = (digito_verificador_2 * 10) % 11;
    if i == 11:
        ...;
    
    digito_verificador_2 = digito_verificador_2 if digito_verificador_2 < 9 else 0;
    
    print(f"O segundo dígito verificador é {digito_verificador_2}");

    cpf_gerado_pelo_calculo = f'{cpf_enviado[:9]}{digito_verificador_1}{digito_verificador_2}';
    if cpf_gerado_pelo_calculo == cpf_enviado:
        print("O CPF enviado pelo usuário é válido");
    else:
        print("O CPF enviado pelo usuário é INVÁLIDO!");
