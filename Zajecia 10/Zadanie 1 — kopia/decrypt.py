from sys import argv
from RSA_Utils import RSA_Utils
from RSA_Core import RSA_Core

if __name__ == "__main__":

    argNum = len(argv) - 1  # liczba argumentów

    if argNum < 2:
        print("Usage: python decrypt.py [public key's filename] [file to be decrypted]")
        exit(1)

    priv_file = argv[1] # zserializowany klucz prywatny
    file = argv[2]      # plik do deszyfrowania

    if not ".encrypted" in file:
        print("Error: The specified file is invalid")
        exit(1)

    n, private_key, N = RSA_Core.deserialize(priv_file)
    
    result = RSA_Core.decrypt(file, n, private_key)
    new_filename = file.replace(".encrypted", "")
    success = RSA_Utils.write_bytes(new_filename, bytes(result))

    if success:
        print("File decrypted successfully as " + new_filename)
        exit(0)
    else:
        print("Error: Failed to decrypt the specified file")
        exit(1)
