from classes.arvore_binaria import ArvoreBinaria  

def menu_geral(nome_tipo, classe):

    arvore = ArvoreBinaria()
    
    while True:
        print(f"\n--- MENU {nome_tipo.upper()} ---")
        print("1 - Cadastrar")
        print("2 - Listar todos")
        print("3 - Buscar por código")
        print("4 - Excluir por código")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Criar registro chamando o construtor
            atributos = []
            for arg in classe.__init__.__code__.co_varnames[1:]:  # ignora self
                valor = input(f"Informe {arg}: ")
                # tenta converter para float se for peso ou altura, senão mantém string
                if valor.replace('.', '', 1).isdigit():
                    if "peso" in arg.lower() or "altura" in arg.lower() or "valor" in arg.lower():
                        valor = float(valor)
                    else:
                        valor = int(valor)
                atributos.append(valor)
            registro = classe(*atributos)
            arvore.inserir(registro)
            print(f"{nome_tipo} cadastrado com sucesso!")
        
        elif opcao == "2":
            print(f"\n--- Lista de {nome_tipo}s ---")
            arvore.percorrer_em_ordem()
        
        elif opcao == "3":
            codigo = input("Informe o código para buscar: ")
            if codigo.isdigit():
                codigo = int(codigo)
            resultado = arvore.buscar(codigo)
            if resultado:
                print("Registro encontrado:")
                print(resultado)
            else:
                print("Registro não encontrado.")
        
        elif opcao == "4":
            codigo = input("Informe o código para excluir: ")
            if codigo.isdigit():
                codigo = int(codigo)
            arvore.excluir(codigo)
            print("Registro excluído, se existia.")
        
        elif opcao == "5":
            print(f"Saindo do menu {nome_tipo}...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

