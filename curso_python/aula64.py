'''
Gerador de CPFs. Para fazer, basta gerar 9 dígitos aleatórios e jogar no nosso algoritmo para gerar os dois dígitos verificadores do cpf.
'''
import re;
import random;
import sys;

for _ in range(10):
    nove_digitos = '';
    for i in range(9):
        nove_digitos += str(random.randint(0,9));

    #print(nove_digitos);

    nove_digitos = re.sub(r'[^0-9]','',nove_digitos); 

    if len(nove_digitos) != 9:
        print("Digite apenas um número de cpf completo");
        sys.exit();

    teste_repeticao = nove_digitos[0] * (len(nove_digitos));

    #print(teste_repeticao);

    # if nove_digitos == teste_repeticao:
    #     print("Digite um cpf válido e que não seja feito apenas de um número.");
    #     sys.exit();

    i = 0;
    contador_regressivo_1 = 10;
    digito_verificador_1 = 0;
    while i < 9:
        try:
            numero_cpf_int = int(nove_digitos[i]); 
            digito_verificador_1 += numero_cpf_int * contador_regressivo_1;
            i += 1;
            contador_regressivo_1 -= 1;
        except:
            print("Digite apenas números");
            i = 10;
            sys.exit();
    digito_verificador_1 = (digito_verificador_1 * 10) % 11;
    if i == 10:
        ...;

    digito_verificador_1 = digito_verificador_1 if digito_verificador_1 < 9 else 0;

    nove_digitos = nove_digitos + str(digito_verificador_1);

    #print(f"O primeiro dígito verificador é {digito_verificador_1}");

    i = 0;
    contador_regressivo_2 = 11;
    digito_verificador_2 = 0;
    while i < 10:
        numero_cpf_int = int(nove_digitos[i]); 
        digito_verificador_2 += numero_cpf_int * contador_regressivo_2; # Mesma coisa que resultado = resultado + (numero_cpf_int * contador_regressivo)
        i += 1;
        contador_regressivo_2 -= 1;
    digito_verificador_2 = (digito_verificador_2 * 10) % 11;
    if i == 11:
        ...;

    digito_verificador_2 = digito_verificador_2 if digito_verificador_2 < 9 else 0;

    #print(f"O segundo dígito verificador é {digito_verificador_2}");

    cpf_gerado_pelo_calculo = f'{nove_digitos[:9]}{digito_verificador_1}{digito_verificador_2}';
    print(f"CPF válido gerado: {cpf_gerado_pelo_calculo}");
