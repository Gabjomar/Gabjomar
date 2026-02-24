'''
while/else.

'''

string = input("Digite um valor qualquer: ");

i = 0;

while i < len(string):
    letra = string[i];

    if letra == " ":
        break;
    print(letra);
    i += 1;
else:
    print("Depois de executado o while, é executado o else do while.");
print("Depois de executado todo o bloco do while e else do while, é executado o que vem a seguir.")

# Se ocorrer um break durante o while, NÃO é executado o else do while.
