import numpy as np


def test(m=31, a=3, c=0, s=1, n_terms=300):
    def lcg(modulus, a, c, seed):
        while True:
            seed = (a * seed + c) % modulus
            yield seed

    terms = []
    for x in (lcg(m, a, c, s)):
        if(n_terms):
            n_terms -= 1
            terms.append(x)
        else:
            break

    #bit_s = (''.join(str(bin(t_)[2:]) for t_ in terms))
    bit_s = ''.join(str(t_ % 2) for t_ in terms)
    return terms, bit_s


if __name__ == '__main__':
    t = test()[0]
    print(t)
