from math import fabs as fabs
from math import floor as floor
from math import sqrt as sqrt
from scipy.special import erfc as erfc
from scipy.special import gammaincc as gammaincc
import lcg
import bbs
import ansi


def monobit_test(binary_data, verbose=False):
    """
    The focus of the test is the proportion of zeroes and ones for the entire sequence.
    The purpose of this test is to determine whether the number of ones and zeros in a sequence are approximately
    the same as would be expected for a truly random sequence. The test assesses the closeness of the fraction of
    ones to 陆, that is, the number of ones and zeroes in a sequence should be about the same.
    All subsequent tests depend on the passing of this test.
    if p_value < 0.01, then conclude that the sequence is non-random (return False).
    Otherwise, conclude that the the sequence is random (return True).
    :param      binary_data         The seuqnce of bit being tested
    :param      verbose             True to display the debug messgae, False to turn off debug message
    :return:    (p_value, bool)     A tuple which contain the p_value and result of frequency_test(True or False)
    """

    length_of_bit_string = len(binary_data)

    # Variable for S(n)
    count = 0
    # Iterate each bit in the string and compute for S(n)
    for bit in binary_data:
        if bit == '0':
            # If bit is 0, then -1 from the S(n)
            count -= 1
        elif bit == '1':
            # If bit is 1, then +1 to the S(n)
            count += 1

    # Compute the test statistic
    sObs = count / sqrt(length_of_bit_string)

    # Compute p-Value
    p_value = erfc(fabs(sObs) / sqrt(2))

    if verbose:
        print('Frequency Test (Monobit Test) DEBUG BEGIN:')
        print("\tLength of input:\t", length_of_bit_string)
        print('\t# of \'0\':\t\t\t', binary_data.count('0'))
        print('\t# of \'1\':\t\t\t', binary_data.count('1'))
        #print('\tS(n):\t\t\t\t', count)
        #print('\tsObs:\t\t\t\t', sObs)
        #print('\tf:\t\t\t\t\t', fabs(sObs) / sqrt(2))
        #print('\tP-Value:\t\t\t', p_value)
        #print('DEBUG END.')

    # return a p_value and randomness result
    return (p_value, (p_value >= 0.01))


if __name__ == '__main__':

    n_terms_bbs = 1000
    n_terms_lcg = 1000
    n_terms_ansi = 1000

    terms = bbs.test(n_terms=n_terms_bbs)[1]  # terms - tuple
    terms_bbs = ''.join(str(t_[1]) for t_ in terms)
    terms_lcg = lcg.test(2**12, 125, 1, 1, n_terms_lcg)[1]
    #terms_ansi = ansi.test(limit=n_terms_ansi)[1]

    print("test_lcg: ", monobit_test(terms_lcg, True), "\n\n")
    print("test_bbs: ", monobit_test(terms_bbs, True), "\n\n")
    #print("test_ansi: ", monobit_test(terms_ansi, True), "\n\n")
