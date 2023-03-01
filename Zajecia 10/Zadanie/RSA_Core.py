from random import randint
from secrets import randbits
import pickle
from RSA_Utils import RSA_Utils

class RSA_Core:
    """Klasa zawiera podstawowe metody dotyczące RSA"""

    @staticmethod
    def keygen(N: int):
        """Generowanie klucza publicznego i prywatnego"""
        while True:
            p = 16**N + 2 * randbits(4*N - 1)+1
            if all(RSA_Utils.miller_rabin(p) for _ in range(10)):
                break
        while True:
            q = 16**N + 2 * randbits(4*N - 1)+1
            if all(RSA_Utils.miller_rabin(q) for _ in range(10)):
                break
        n = p * q
        phi=(p-1)*(q-1)

        while (ex := RSA_Utils.nwd(phi, e:= randint(2,phi-1)))[0]!=1:
            pass

        d = ex[2] % phi
        return (n, d, e)

    @staticmethod
    def serialize(data, filename: str):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def deserialize(filename: str):
        try:
            with open(filename, 'rb') as file:
                data: tuple = pickle.load(file)
                return data
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def encrypt(filename: str, N: int, n: int, public_key: int):
        blocks = [b for b in RSA_Utils.read_bytes(filename, N)]
        data = [pow(i, public_key, n) for i in blocks]
        
        return data

    @staticmethod
    def decrypt(filename: str, n: int, private_key: int):
        data = RSA_Core.deserialize(filename)
        result = [pow(x, private_key, n) for x in data]

        return result