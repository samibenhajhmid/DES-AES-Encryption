from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Cipher import DES


def aes_encryption(password, choice_operation):
   print("hello des")
   hash_object = SHA256.new(password.encode('utf-8'))
   hash_key = hash_object.digest()
   print("le clé haché")
   print(hash_key)
   print("le longueur de clé haché :")
   print(len(hash_key))
   print("le type de clé haché:")
   print(type(hash_key))
   BLOCK_SIZE = 16
   PADDING_UNIT = "{"
   padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING_UNIT
   cipher = AES.new(hash_key, AES.MODE_ECB)
   result_chiffrement = cipher.encrypt(padding(password).encode('utf-8'))
   if(choice_operation=="1"):
       print("le message chiffré :")
       print(result_chiffrement)
   else:
       resultat_dechiffrement=cipher.decrypt(password).decode('utf-8')
       padding_index=resultat_dechiffrement.find(PADDING_UNIT)
       resultat_dechiffrement_final =resultat_dechiffrement[:padding_index]
       print(resultat_dechiffrement_final)



def des_encryption(password, choice_operation):

    def pad(text):
        n = len(text) % 8
        return text + (b' ' * n)

    key = b'hello123'
    text1 = bytes(password, 'utf-8')

    des = DES.new(key, DES.MODE_ECB)

    padded_text = pad(text1)
    encrypted_text = des.encrypt(padded_text)

    print("message chiffré est :\n")
    print(encrypted_text)
    print("message original :\n")
    print(des.decrypt(encrypted_text))



def to_16_bytes_multiply_length(message):
    return message + (16 - len(message) % 16) * "{"


def user_input():
    choice_operation = input("veuillez choisir le type d'opération ? :\n1 chiffrer \n2 déchiffrer\n")
    while(choice_operation not in ["1","2"]):
        choice_operation = input("veuillez choisir le type d'opération ? :\n1 chiffrer \n2 déchiffrer\n")

    if(choice_operation =="1"):
        password = input("veuillez donner le texte a chiffrer\n")
    else:
        password = input("veuillez donner le texte a déchiffrer\n")

    choice=""
    while(choice not in ["DES", "AES", "aes", "des"] ):
        choice = input("veuillez choisir le type de chiffrement : DES ou AES")
    if choice in ["AES", "aes"]:
        aes_encryption(password, choice_operation)
    else:
        des_encryption(password, choice_operation)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(to_16_bytes_multiply_length("sami"))
    user_input()

