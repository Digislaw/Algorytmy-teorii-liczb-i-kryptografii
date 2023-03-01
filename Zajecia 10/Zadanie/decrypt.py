from sys import argv
from RSA_Utils import RSA_Utils
from RSA_Core import RSA_Core

if __name__ == "__main__":

    argNum = len(argv) - 1  # liczba argumentów

    if argNum < 2:
        print("Usage: python decrypt.py [private key's filename] [file to be decrypted]")
        exit(1)
    elif argNum == 3 or argNum > 4:
        print("Usage: python decrypt.py -o [new file's name] [private key's filename] [file to be decrypted]")
        exit(1)

    new_filename = ""

    if argv[1][0] == "-" and "o" in argv[1]:
        new_filename = argv[2]
        priv_file = argv[3]     # zserializowany klucz prywatny
        file = argv[4]          # plik do deszyfrowania
    else:
        priv_file = argv[1]  # zserializowany klucz prywatny
        file = argv[2]       # plik do deszyfrowania

    if not ".encrypted" in file:
        print("Error: The specified file is invalid")
        exit(1)

    n, private_key, N = RSA_Core.deserialize(priv_file)
    
    result = RSA_Core.decrypt(file, n, private_key)
    new_filename = file.replace(".encrypted", "") if not new_filename else new_filename
    success = RSA_Utils.write_bytes(new_filename, bytes(result))

    if success:
        print("File decrypted successfully as " + new_filename)
        exit(0)
    else:
        print("Error: Failed to decrypt the specified file")
        exit(1)
