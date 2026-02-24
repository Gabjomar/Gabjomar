'''
Jogo da palavra secreta.

Faça um jogo para o usuário advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
'''

# -=-=-=- GABARITO -=-=-=-~

# Importando o módulo OS para limpar o terminal quando o jogador ganha o jogo e deseja jogar novamente.
import os;

palavra_secreta = 'arroz';
letras_acertadas = '';
numero_tentativas = 0;

while True:
    numero_tentativas += 1;
    letra_digitada = input('Digite uma letra: ');

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!');
        continue;
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada;

    # Para aparecer a palavra secreta na mesma linha, de uma vez só. Outra sacada simples e muito inteligente para não ter quebras indesejadas de linha.
    palavra_formada = ''; # A atribuição inicial dessa variável está dentro do loop pois ela precisa ser resetada toda vez o loop ocorre.

    # A sacada que eu não consegui pensar, muito simples e super inteligente!
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            #print(letra_secreta);
            palavra_formada += letra_secreta;
        else:
            #print("*");
            palavra_formada += "*";
    print(palavra_formada);

    if (palavra_formada == palavra_secreta):
        # limpando o terminal antes de apresentar o texto da vitória.
        os.system('cls');

        print('Você Ganhou! Parabéns!');
        print(f'A palavra secreta era {palavra_secreta}');
        print(f'Número de tentativas foi: {numero_tentativas}');

        # Resetando o jogo.
        letras_acertadas = '';
        numero_tentativas = 0;
        


