from Crypto.Hash import SHA1
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import base64
import pickle

class Funcoes:
    def __init__(self):
        self.publicKey = ''
        self.privateKey = ''
        self.assinatura = ''
        self.geraKeys()

    def verifica(self, exported_key):
        data = self.assinatura[0]
        signature = self.assinatura[1]
        key = RSA.importKey(exported_key)
        h = SHA256.new(pickle.dumps(data))
        return PKCS1_v1_5.new(key).verify(h, signature)

    def assinar(self, data, exported_key):
        key = RSA.importKey(exported_key)
        signed_data = []
        signed_data.append(data)
        signed_data.append(PKCS1_v1_5.new(key).sign(SHA256.new(pickle.dumps(data))))
        with open("assinatura.txt", "wb") as f:
            f.write(b"--- ASSINATURA BASE64 ---\n")
            f.write(base64.b64encode(signed_data[1]))
        return signed_data

    def geraKeys(self):
        #Gera as chaves
        tam_key = 2048
        rand = Random.new().read
        key = RSA.generate(tam_key, rand)

        private_key = key.exportKey()
        self.privateKey = private_key
        with open("privateKey.txt", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().exportKey()
        self.public_key = public_key
        with open("publicKey.txt", "wb") as f:
            f.write(public_key)

        self.privateKey = key


    def assinaDocumento(self, mensagem, tipoSHA=0):
        if tipoSHA == 0:
            #hash = SHA256.new(mensagem.encode("utf-8")).digest()
            privateKey = self.privateKey.exportKey()
            self.assinatura = self.assinar(mensagem, privateKey)

    def verificaAutenticidade(self):
        #self.assinatura[0] = 'Some dataaaaaaaa'             # Succeeds
        self.assinatura[0] = 'Testando a criptogfia dessa mensagem que diz muita coisa'        # Fails
        keyPub = self.privateKey.publickey().exportKey()
        verified = self.verifica(keyPub)
        print(verified)
