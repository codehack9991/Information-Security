from math import sqrt
from collections import Counter
import lcg
import bbs
import ansi
import numpy as np
import matplotlib.pyplot as plt


def is_random(random_nums):
    # Calculate the number of samples - n
    n = len(random_nums)
    r = 10  # no. of classes
    # According to Sedgewick:
    # This is valid if n is greater than about 10r
    # if n <= 10 * r:
    #    return False

    n_r = n / r     # expected frquency
    # PART A: Get frequency of randoms
    ht = []
    mn = min(random_nums)
    mx = max(random_nums)
    diff = (mx - mn) // r
    while mn <= mx:
        ht.append(len(list(x for x in random_nums if mn <= x <= mn + diff)))
        mn = mn + diff + 1
    print(ht)
    # PART B: Calculate chi-square - this approach is in Sedgewick
    chi_square = sum((v - n_r)**2 for v in ht) / (n_r * 1.0)
    print(chi_square)
    # PART C: According to Sedgewick:
    # The statistic should be within 2(r)^1/2 of r
    # This is valid if N is greater than about 10r
    return abs(chi_square - r) <= 2 * sqrt(r)


if __name__ == '__main__':

    n_terms_bbs = 1000
    n_terms_lcg = 1000
    n_terms_ansi = 1000

    terms = bbs.test(n_terms=n_terms_bbs)[1]  # terms - tuple
    terms_bbs = [t_[0] for t_ in terms]
    terms_lcg = lcg.test(2**12, 125, 1, 1, n_terms_lcg)[0]
    terms_ansi = ansi.test(limit=n_terms_ansi)[0]

    print("test_lcg: ", is_random(terms_lcg))
    print("test_bbs: ", is_random(terms_bbs))
    print("test_ansi: ", is_random(terms_ansi))
