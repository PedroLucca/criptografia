from Crypto.Hash import SHA1
from Crypto.Hash import SHA224
from Crypto.Hash import SHA256
from Crypto.Hash import SHA384
from Crypto.Hash import SHA512
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import base64
import pickle

from regex import P

class Funcoes:
    def __init__(self):
        self.geraKeys()

    def verifica(self, exported_key, mensagem, assinatura, tipoSHA):
        data = mensagem
        signature = assinatura
        key = RSA.importKey(exported_key)
        
        if tipoSHA == 1:
            h = SHA256.new(pickle.dumps(data))
        elif tipoSHA == 2:
            h = SHA1.new(pickle.dumps(data))
        elif tipoSHA == 3:
            h = SHA224.new(pickle.dumps(data))
        elif tipoSHA == 4:
            h = SHA384.new(pickle.dumps(data))
        elif tipoSHA == 5:
            h = SHA512.new(pickle.dumps(data))
        else:
            h = SHA256.new(pickle.dumps(data))

        return PKCS1_v1_5.new(key).verify(h, signature)

    def assinar(self, data, exported_key, tipoSHA):
        key = RSA.importKey(exported_key)
        signed_data = []
        signed_data.append(data)
        if tipoSHA == 1:
            signed_data.append(PKCS1_v1_5.new(key).sign(SHA256.new(pickle.dumps(data))))
        elif tipoSHA == 2:
            signed_data.append(PKCS1_v1_5.new(key).sign(SHA1.new(pickle.dumps(data))))
        elif tipoSHA == 3:
            signed_data.append(PKCS1_v1_5.new(key).sign(SHA224.new(pickle.dumps(data))))
        elif tipoSHA == 4:
            signed_data.append(PKCS1_v1_5.new(key).sign(SHA384.new(pickle.dumps(data))))
        elif tipoSHA == 5:
            signed_data.append(PKCS1_v1_5.new(key).sign(SHA512.new(pickle.dumps(data))))
        else:
            signed_data.append(PKCS1_v1_5.new(key).sign(SHA256.new(pickle.dumps(data))))
        with open("assinatura.txt", "wb") as f:
            f.write(base64.b64encode(signed_data[1]))
        return signed_data

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

    def assinaDocumento(self, mensagem, chave, tipoSHA=1):
        assinatura = self.assinar(mensagem, chave, tipoSHA)
        print("\nAssinatura: ", base64.b64encode(assinatura[1]).decode('utf-8'))

    def verificaAutenticidade(self, mensagem, publicKey, assinatura, tipoSHA=1):
        assinatura = base64.b64decode(assinatura)
        verified = self.verifica(publicKey, mensagem, assinatura, tipoSHA)
        print("\nVerificação da mensagem: ", verified)
