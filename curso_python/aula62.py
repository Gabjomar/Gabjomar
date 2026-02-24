'''
Cálculo do segundo dígito verificador do CPF.
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DÍGITO VERIFICADOR, multiplicando cada um dos valores por uma contagem regressiva começando de 11.

Ex.: 746.824.890-70 (74682489070)
    11  10  9  8  7  6  5  4  3  2
*   7   4   6  8  2  4  8  9  0  7 <-- PRIMEIRO DÍGITO VERIFICADOR CALCULADO
    70  36 48 56 12 20 32 27  0  14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363.
Multiplicar o resultado anterior por 10:
363 * 10 = 3630.
Obter o resto da divisão da conta anterior por 11:
3630 % 11 = 0.
Se o resultado anterior for maior que 9:
    resultado é 0.
contrário disso:
    resultado é o valor da conta.

O primeiro dígito do CPF é 0.
'''
while True:
    cpf_enviado = input("Digite um CPF para ser verificado: ");

    if len(cpf_enviado) != 11:
        print("Digite um número de cpf completo sem pontos e traços.");
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
