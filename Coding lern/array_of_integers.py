# Problem: Given an array of n integers, generates an int not in the input.
# Use a minimum amount in memory.
# Constraints
#
# Are we working with non-negative ints?
# Yes
# What is the range of the integers?
# Discuss the approach for 4 billion integers
# Implement for 32 integers
#     Can we assume the inputs are valid?
# No
#
#
# Test Cases
#
# None -> Exception
# [] -> Exception
# General case
# There is an int excluded from the input -> int
# There isn't an int excluded from the input -> None
# Algorithm
# # The problem states to use a minimal amount of memory. We'll use a bit vector to keep track of the inputs.
# # Say we are given 4 billion integers, which is 2^32 integers.
# The number of non-negative integers would be 2^31.
# With a bit vector, we'll need 4 billion bits to map each integer to a bit.
# Say we had only 1 GB of memory or 2^32 bytes. This would leave us with 8 billion bits.
# # To simplify this exercise, we'll work with an input of up to 32 ints that we'll map to a bit vector of 32 bits.
# # input = [0, 1, 2, 3, 4...28, 29, 31]
# #
# bytes          [         1          ]  [          2         ] [          3          ] [          4          ]
# # index       =  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
# # bit_vector  =  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  0  1
# # result = 30
# # * Loop through each item in the input, setting bit_vector[item] = True.
# # * Loop through the bit_vector, return the first index where bit_vector[item] == False.
# # Complexity:
# # Time: O(b), where b is the number of bits
# Space: O(b)
# # Code
from bitstring import BitArray
from nose.tools import assert_equal, assert_raises


class Bits(object):
    def new_int(self, array, max_size):
        if not array:
            raise TypeError("array cannot be non or empty")
        bit_vector = BitArray(max_size)
        for item in array:
            bit_vector[item] = True
        for index, item in enumerate(bit_vector):
            if not item:
                return index
        return None


class TestBits(object):
    def test_new_int(self):
        bits = Bits()
        max_size = 32
        assert_raises(TypeError, bits.new_int, None, max_size)
        assert_raises(TypeError, bits.new_int, [], max_size)
        data = [item for item in range(30)]
        data.append(31)
        assert_equal(bits.new_int(data, max_size), 30)
        data = [item for item in range(32)]
        assert_equal(bits.new_int(data, max_size), None)
        print('Success: test_find_int_excluded_from_input')


def main():
    test = TestBits()
    test.test_new_int()


if __name__ == '__main__':
    main()
