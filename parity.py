import unittest
import random

""" The parity of a binary word is 1 if the number of Is in the word is odd; otherwise, it is 0. For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word. """

#Brute force
def parity (x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

#O(n) time complexity n word size.


#improve best and average case.
#ease lowest set bit in a word.

#x & (x-1) = x with lowest set bit erased
#& is bitwise AND

#Let k be the number of bits set to 1 in a particular word.
#O(k) time complexity

def  parity_k(x):
    odd_parity = True
    result = 0
    while x:
        odd_parity != odd_parity
        result ^= 1
        x &= x - 1 #Drop lowest set bit of x
    return result




class ParityTestCase(unittest.TestCase):
    def test_odd(self):
        a = 1011
        result = parity(a)
        self.assertEqual(result, 1)
    def test_even(self):
        a = 10001000
        result = parity(a)
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
