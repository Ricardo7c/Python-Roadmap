cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto']

while True:
    cor_remover = input("Digite uma cor para remover (ou 'sair' para encerrar): ")
    
    if cor_remover.lower() == 'sair':
        break
    
    if cor_remover in cores:
        cores.remove(cor_remover)
    

print("Lista final:", cores)