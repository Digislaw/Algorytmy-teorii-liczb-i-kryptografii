from sys import argv
from RSA_Core import RSA_Core

if __name__ == "__main__":
    argNum = len(argv) - 1  # liczba argumentów

    if argNum < 1:
        print("Usage: python keygen.py [N]")
        exit(1)

    N = int(argv[1]) # liczba bajtów w bloku

    if N % 2:
        print("Error: Bytes number must be a power of 2")
        exit(1)    

    n, public, private = RSA_Core.keygen(N)
    data = (n, public, private, N)

    print(data)
    success = RSA_Core.serialize(data, RSA_Core.KEYS_NAME)

    if success:
        print("Keys generated successfully")
        print("Public key:", public)
        print("Private key:", private)

    # d = RSA_Core.deserialize(RSA_Core.KEYS_NAME)
    # print(d)

    exit(0)