# \r -> Return.
# \r\n -> CRLF (todos os windows).
# \n -> LF (linux, mac e windows 11).

# Python é case sensitive! Cuidado com as letras maiúsculas e minúsculas.

print(123, 34, sep='.', end="\r\n");
print(56, 789, sep="x", end="\n##\n");
print(56, 789, sep='');