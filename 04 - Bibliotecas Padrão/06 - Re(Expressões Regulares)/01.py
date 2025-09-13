import re

palavra = input("Digite uma palavra: ")

if re.match("a", palavra, re.IGNORECASE):
    print("A palavra começa com 'a'")
else:
    print("A palavra não começa com 'a'")