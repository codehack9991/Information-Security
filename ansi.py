import sys
from itertools import islice
from Crypto.Cipher import DES3
from Crypto.Util.strxor import strxor
from time import time
import struct


def test(seed=b'01234567', key=b'0123456789abcdef', limit=300):
    def ansi_x9_17(V, key):
        '''
        Generator for ansi_x9_17 PRNG
        V: seed. It should be a string of length 8
        key: concat of keys K1 & K2. It should be a string of length 16'''
        des3 = DES3.new(key, DES3.MODE_ECB)
        while True:
            EDT = des3.encrypt(hex(int(time() * 10**6))[-8:])
            R = des3.encrypt(strxor(V, EDT))
            V = des3.encrypt(strxor(R, EDT))
            #print(len(R))
            yield R[0]
    terms = []

    # each char in a string = 1 byte
    #seed = '01234567'
    #key = '0123456789abcdef'
    #limit = 5
    #print(seed, "||", key)
    #print ('\n'.join([str(i) for i in islice(ansi_x9_17(seed, key), limit)]))
    # print(sys.maxsize)
    #terms = [i for i in islice(ansi_x9_17(seed, key), limit)]
    n_terms = limit
    for x in (ansi_x9_17(seed, key)):
        if(n_terms):
            n_terms -= 1
            terms.append(x)
        else:
            break

    bit_s = ''.join(str(t_ % 2) for t_ in terms)
    return terms, bit_s


if __name__ == '__main__':
    t = test()[0]
    print(t)
