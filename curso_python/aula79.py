'''
Exercício - Sistema de perguntas e respostas.
'''

perguntas = [
    {
        'Pergunta': "Quanto é 2+2?",
        'Opções': ['1', '3', '4', '7'],
        'Resposta': '4',
    },
    {
        'Pergunta': "Quanto é 2+5?",
        'Opções': ['5', '9', '4', '7'],
        'Resposta': '7',
    },
    {
        'Pergunta': "Quanto é 1+1?",
        'Opções': ['1', '3', '4', '2'],
        'Resposta': '2',
    },
        {
        'Pergunta': "Quanto é 0+1?",
        'Opções': ['1', '3', '4', '2'],
        'Resposta': '1',
    },
];

quantidade_acertos = 0;

for pergunta in perguntas:
    print("Pergunta: ", pergunta['Pergunta']);
    print(); # Para dar um espaço

    numero_opcao = 0;
    for i in pergunta['Opções']: # Poderia ter utilizado "for i, opcao in enumerate(opcoes):", fica mais enxuto.
        print(f'{numero_opcao}) {i}');
        if (i) == (pergunta['Resposta']):
            opcao_correta = numero_opcao;   
        numero_opcao += 1;
    
    opcao_escolhida = input("Escolha uma opção: ");
    opcao_escolhida_int = int(opcao_escolhida);

    if opcao_escolhida_int == opcao_correta:
        print("Acertou!");
        quantidade_acertos += 1;
    else:  
        print ("Errou!");
    print(); # Para dar um espaço

print(f'Parabéns! Você acertou {quantidade_acertos} de {len(perguntas)} perguntas ');