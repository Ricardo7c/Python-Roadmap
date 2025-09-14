from traceback import print_tb


num_linhas = num_palavras = num_caracteres = 0

with open('origem.txt', 'r') as arquivo:
    for linhas in arquivo:
        num_linhas += 1
        num_caracteres += len(linhas)
        palavras = linhas.split()
        num_caracteres += len(palavras)

print(num_linhas)
print(num_linhas)
print(num_caracteres)