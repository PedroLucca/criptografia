from funcoes import Funcoes

crypt = Funcoes()

while True:
    print("\nTrabalho de Segurança - Assinatura Digital")
    print("Alunos: Daniel Évani, Manassés Silva e Pedro Lucca\n")

    print("--- MENU PRINCIPAL ---\n")
    
    print("1 - Assinar mensagem")
    print("2 - Verificar assinatura")
    print("3 - Gerar novas chaves")
    print("0 - Sair\n")

    opcao = int(input("Digite uma opção: "))

    if opcao == 0:
        print("\nPrograma finalizado...")
        break
    elif opcao == 1:
        f = open("mensagem.txt", "r")
        mensagem = f.read()

        crypt.assinaDocumento(mensagem)
        print(crypt.assinatura)
    elif opcao == 2:
        crypt.verificaAutenticidade()
    elif opcao == 3:
        crypt.geraKeys()
        print("\n Chaves também se encontram nos respectivos arquivos txt!")
        

        """ 
        
        print(crypt.assinatura)
        crypt.verificaAutenticidade() """

