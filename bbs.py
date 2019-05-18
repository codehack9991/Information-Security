def test(p=383, q=503, s=101355, n_terms=300):

    def bbs(n, seed):
        while True:
            seed = ((seed % n) * (seed % n)) % n
            yield seed, seed % 2

    # p is prime
    # q is prime
    n = p * q
    # s = seed: coprime with n i.e., p,q aren't factors of s
    # n_terms = no. of terms
    x0 = ((s % n) * (s % n)) % n
    terms = []

    for x in (bbs(n, x0)):
        if(n_terms):
            n_terms -= 1
            terms.append(x)
        else:
            break

    #terms_ = [t_[0] for t_ in terms]
    return x0, terms


if __name__ == '__main__':
    t = test()[0]
    print(t)
    t = test()[1]
    for t_ in t:
        print(t_[0], "--", t_[1])
