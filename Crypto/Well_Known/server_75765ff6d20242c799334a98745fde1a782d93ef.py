import hashlib
import sys
import random
from Crypto.Util.number import *
from socketserver import ThreadingTCPServer, BaseRequestHandler
from flag import FLAG

class Signer:
    def __init__(self, L, N):
        self.q = getPrime(N)
        while True:
            self.p = self.q * random.getrandbits(L - N) + 1
            if isPrime(self.p):
                break

        self.g = pow(2, (self.p - 1) // self.q, self.p)

        self.x = bytes_to_long(FLAG)
        self.y = pow(self.g, self.x, self.p)
        assert(self.x < self.q)

    def sign(self, m, k):
        r = pow(self.g, k, self.p) % self.q
        s = inverse(k, self.q) * (m + self.x * r) % self.q

        if s == 0:
            raise ValueError

        return (r, s)

class Handler(BaseRequestHandler):
    def handle(self):
        key = Signer(2048, 256)
        rnd = random.getrandbits(64)

        self.request.sendall(bytes('p = {:d}\n'.format(key.p), 'ascii'))
        self.request.sendall(bytes('q = {:d}\n'.format(key.q), 'ascii'))
        self.request.sendall(bytes('g = {:d}\n'.format(key.g), 'ascii'))

        try:
            for i in range(3):
                self.request.sendall(b'Input your data (in hex):\n')
                data = long_to_bytes(int(self.request.recv(4096), 16))

                k = pow(int(hashlib.sha1(data).hexdigest(), 16), rnd, key.q)
                h = int(hashlib.sha256(data).hexdigest(), 16)
                r, s = key.sign(h, k)

                self.request.sendall(bytes('r = {:d}\n'.format(r), 'ascii'))
                self.request.sendall(bytes('s = {:d}\n'.format(s), 'ascii'))
        except ValueError as e:
            self.request.sendall(bytes('Invalid value\n', 'ascii'))
        else:
            self.request.sendall(b'Bye.\n')



if __name__ == '__main__':
    host = 'localhost'
    port = 31337
    if len(sys.argv) >= 3:
        host = sys.argv[1]
        port = int(sys.argv[2])

    s = ThreadingTCPServer((host, port), Handler)

    print('Listening at {}:{:d}'.format(host, port))
    s.serve_forever()
