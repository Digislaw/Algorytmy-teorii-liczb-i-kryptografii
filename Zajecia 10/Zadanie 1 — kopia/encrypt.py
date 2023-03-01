from sys import argv
from RSA_Core import RSA_Core

if __name__ == "__main__":

    argNum = len(argv) - 1  # liczba argumentów

    if argNum < 2:
        print("Usage: python encrypt.py [public key's filename] [file to be encrypted]")
        exit(1)

    pub_file = argv[1]  # zserializowany klucz publiczny
    file = argv[2]      # plik do zaszyfrowania

    n, public_key, N = RSA_Core.deserialize(pub_file)
    
    data = RSA_Core.encrypt(file, N, n, public_key)
    new_filename = file + ".encrypted"
    success = RSA_Core.serialize(data, new_filename)

    if success:
        print("File encrypted successfully as " + new_filename)
        exit(0)
    else:
        print("Error: Failed to encrypt the specified file")
        exit(1)