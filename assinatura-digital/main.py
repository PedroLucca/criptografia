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
        print("\n--- Assinar Documento: Escolha o SHA ---\n")
    
        print("1 - SHA256")
        print("2 - SHA1")
        print("3 - SHA224")
        print("4 - SHA384")
        print("5 - SHA512")

        opcao2 = int(input("\nDigite uma opção: "))
        f = open("mensagem.txt", "r")
        mensagem = f.read()

        with open("privateKey.txt", "rb") as f:
            privateKey = f.read()

        #Função de assinatura recebe mensagem, a chave e tipo de SHA
        crypt.assinaDocumento(mensagem, privateKey, opcao2)

        print("\nAssinatura da mensagem também se encontra no arquivo assinatura.txt!")

    elif opcao == 2:
        f = open("mensagem.txt", "r")
        mensagem = f.read()

        with open("publicKey.txt", "rb") as f:
            publicKey = f.read()
        
        with open("assinatura.txt", "r") as f:
            assinatura = f.read()

        print("\n--- Verificar autenticidade: Escolha o SHA ---\n")
    
        print("1 - SHA256")
        print("2 - SHA1")
        print("3 - SHA224")
        print("4 - SHA384")
        print("5 - SHA512")

        opcao2 = int(input("\nDigite uma opção: "))

        crypt.verificaAutenticidade(mensagem, publicKey, assinatura, opcao2)

    elif opcao == 3:
        crypt.geraKeys()
        with open("privateKey.txt", "r") as f:
            privateKey = f.read()
        with open("publicKey.txt", "r") as f:
            publicKey = f.read()

        print("\nNovas chaves geradas: ", publicKey, privateKey)
        print("\n Chaves também se encontram nos respectivos arquivos txt!")
        

