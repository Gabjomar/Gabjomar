nome = 'Maico Miranda';
peso = 75;
altura = 1.8;
imc = peso / (altura*2);

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos, e seu IMC é', imc, sep=' ');

print(f'{nome} tem {altura:.2f} de altura, pesa {peso:.2f} quilos, e seu IMC é {imc:.5f}');

linha_1 = f'{nome} tem {altura:.2f} de altura,';
linha_2 = f'pesa {peso:.2f} quilos,';
linha_3 = f'e seu IMC é {imc:.5f}';

print(linha_1);
print(linha_2);
print(linha_3);