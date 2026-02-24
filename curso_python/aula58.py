'''
Interpretador do python.

python mod.py (executa o mod)
python -u (unbuffered) -> Evita o python de salvar o que é impresso quando executa um código/arquivo.
python -m mod (lib mod como script) -> Cria um ambiente virtual. Veremos mais para frente no curso.
python -c 'cmd' (comando) -> Faz o python executar o código posterior ao "-c".
python -i mod.py (interativo com mod) -> Executa algum código/arquivo entrando no modo interativo do python. Útil para fazer alguns testes rápidos e executar o arquivo rapidamente.
python --help -> Para mais informações.

(python -c 'import this')
The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor do que complexo.
Plano é melhor que aglomerado (aninhado, com muita identação).
Esparso é melhor do que denso (muito código em uma linha só).
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras. Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente, a não ser que explicitamente silenciados. 

-> Passar silenciosamente é usar:
try:
    print("Código qualquer");
except: 
    ...
(desse jeito, quando executar esse código, o python nunca mais apresentará um erro, os erros estarão passando silenciosamente)

Diante da ambiguidade, recuse a tentação de advinhar.
Deve haver uma -- e preferencialmente apenas uma -- forma óbvia de fazer isso.
Apesar que essa forma pode não ser óbvia de primeira a não ser que você seja holandês.
Agora é melhor do que nunca. Apesar de que nunca é normalmente melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma ideia ruim.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Os namespaces são uma ideia genial -- vamos fazer mais disso!
'''

print(1+1);print(2+2);