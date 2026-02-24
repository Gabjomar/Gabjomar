'''
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10.

Ex.: 746.824.890-70 (74682489070)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301.
Multiplicar o resultado anterior por 10:
301 * 10 = 3010.
Obter o resto da divisão da conta anterior por 11:
3010 % 11 = 7.
Se o resultado anterior for maior que 9:
    resultado é 0.
contrário disso:
    resultado é o valor da conta.

O primeiro dígito do CPF é 7.
'''
while True:
    cpf = input("Digite um CPF para ser verificado: ");

    if len(cpf) != 11:
        print("Digite um número de cpf completo sem pontos e traços.");
        continue;
    
    i = 0;
    contador_regressivo_1 = 10;
    digito_verificador_1 = 0;
    while i < 9:
        try:
            numero_cpf_int = int(cpf[i]); 
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
    
    print(f"O primeiro digito verificador é {digito_verificador_1}");
