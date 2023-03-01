from sys import argv
from RSA_Core import RSA_Core

if __name__ == "__main__":

    argNum = len(argv) - 1  # liczba argumentów

    if argNum < 2:
        print("Usage: python encrypt.py [public key's filename] [file to be encrypted]")
        exit(1)
    elif argNum == 3 or argNum > 4:
        print("Usage: python encrypt.py -o [new file's name] [public key's filename] [file to be encrypted]")
        exit(1)

    new_filename = ""
    
    if argv[1][0] == "-" and "o" in argv[1]:
        new_filename = argv[2]
        pub_file = argv[3]  # zserializowany klucz publiczny
        file = argv[4]      # plik do zaszyfrowania
    else:
        pub_file = argv[1]  # zserializowany klucz publiczny
        file = argv[2]      # plik do zaszyfrowania

    n, public_key, N = RSA_Core.deserialize(pub_file)
    
    data = RSA_Core.encrypt(file, N, n, public_key)
    new_filename = file + ".encrypted" if not new_filename else new_filename
    success = RSA_Core.serialize(data, new_filename)

    if success:
        print("File encrypted successfully as " + new_filename)
        exit(0)
    else:
        print("Error: Failed to encrypt the specified file")
        exit(1)
