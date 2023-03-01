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
    pub_key = (n, public, N)
    priv_key = (n, private, N)

    pub_success = RSA_Core.serialize(pub_key, "public.key")
    priv_success = RSA_Core.serialize(priv_key, "private.key")

    if pub_success and priv_success:
        print("Keys generated successfully")
        exit(0)
    else:
        print("Error: Failed to create keys")
        exit(1)

    # d = RSA_Core.deserialize("public.key")
    # print(d)