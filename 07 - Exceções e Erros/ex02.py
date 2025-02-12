def abrir_arquivo():
    try:
        with open("arquivo.txt", "r") as arquivo:
            for nome in arquivo:
                print(nome)

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    
    except PermissionError:
        print("Erro: O Usuario não tem permissão para acessar o arquivo")
    
    finally:
        print(f"Encerrando o programa")
    
abrir_arquivo()