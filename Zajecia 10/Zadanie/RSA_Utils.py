from random import randint

class RSA_Utils:
    """Klasa zawiera metody pomocnicze"""

    @staticmethod
    def miller_rabin(n,a=None):
        """Test Millera-Rabina"""
        a = a if a else randint(2,n-2)
        r = n-1
        q = 0
        while r & 1 == 0:
            r >>= 1
            q+=1
        x = pow(a,r,n)
        if x==1:
            return True
        for _ in range(q-1):
            x = pow(x,2,n)
            if x == n-1:
                return True		# liczba pierwsza lub pseudopierwsza
            if x == 1:
                return False	# liczba złożona
        x=pow(x,2,n)
        return False

    @staticmethod
    def nwd(a,b,xa=1,ya=0,xb=0,yb=1):
        if b>a:
            a,b = b,a
        return RSA_Utils.nwd(b, (d:=divmod(a,b))[1], xb, yb, xa-d[0]*xb, ya-d[0]*yb) if b else (a, xa, ya)

    @staticmethod
    def read_bytes(filename: str, size: int):
        """Generator do czytania bloków"""
        with open(filename, "rb") as file:
            while True:
                block = file.read(size)
                if block:
                    yield from block
                else:
                    break

    @staticmethod
    def write_bytes(filename: str, data):
        try:
            with open(filename, "wb") as file:
                file.write(data)
            return True
        except Exception as e:
            print(e)
            return False
