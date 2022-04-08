from Crypto.Hash import SHA1
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.PublicKey import RSA

class Funcoes:
    def __init__(self):
        self.publicKey = ''
        self.privateKey = ''
        self.assinatura = ''
        self.geraKeys()

    def pkcs5_pad(self, s, BLOCK_SIZE=16):   
        print(s)                                                                                                                                                           
        return (s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(                                                                                                                                     
            BLOCK_SIZE - len(s) % BLOCK_SIZE                                                                                                                                                      
            )).encode('utf-8')

    def geraKeys(self):
        #Gera as chaves
        tam_key = 2048
        rand = Random.new().read
        key = RSA.generate(tam_key, rand)

        private_key = key.exportKey()
        with open("privateKey.txt", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().exportKey()
        with open("publicKey.txt", "wb") as f:
            f.write(public_key)

        self.privateKey = key


    def assinaDocumento(self, mensagem, tipoSHA=0):
        if tipoSHA == 0:
            hash = SHA256.new(self.pkcs5_pad(mensagem)).digest()
            self.assinatura = self.privateKey.sign(hash, '')

    def verificaAutenticidade(self):
        result = self.privateKey.publickey().verify(hash, self.assinatura)
        print(result)
