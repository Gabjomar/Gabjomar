'''
Jogo da palavra secreta.

Faça um jogo para o usuário advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
'''
palavra_secreta = "arroz";
qtd_tentativas = 1;
palavra_montada = "";
palavra_montada_passada = "";
letra_achada = None;

while True:
    tentativa_usuário = input('Digite uma letra que você ache que tem na palavra secreta: ');
    tamanho_tentativa_usuário = len(tentativa_usuário);
    if (tamanho_tentativa_usuário == 1) and (not(tentativa_usuário.isdigit())):
        for i in palavra_secreta:
            if i == tentativa_usuário:
                palavra_montada += i;
                letra_achada = True;
            else:
                palavra_montada += "*";
        letra_achada = False;
                
        print(palavra_montada);
        qtd_tentativas += 1;
    else:
        print('Digite apenas uma letra.');
        continue;
    print("");
    if letra_achada:
        palavra_montada_passada = palavra_montada;
    else:
        palavra_montada = "";

    quer_parar = input('Quer parar? [s]im: ').lower();

    if quer_parar == "s":
        break;