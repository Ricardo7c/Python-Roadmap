lista = [1, 2, 3]

print(f"Lista original: {lista}")

dobra = lambda x: x * 2

print(f"Lista dobrada: {list(map(dobra, lista))}")