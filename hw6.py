'''
Created on October 15, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
#00111001001111
#white=0
#black=1
def isOdd(n):
    '''Returns whether or not the integer argument is odd. 42 -> 101010'''
    return n % 2 != 0

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    pass  # TODO
    if n ==0:
        return ''
    if isOdd(n):
        return numToBinary(int(n/2)) + '1'
    else:
        return numToBinary(int(n/2)) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def numToBinaryPadded(n):
    """Returns a string of the non-negative representation of n with 5 bits."""
    s = numToBinary(n)
    return '0' * (COMPRESSED_BLOCK_SIZE - len(s)) + s

def prefixLen(s):
    """Returns the number of times that the first digit of the binary sequence repeats before changing."""
    if len(s) == 1:
        return 1
    if s[1] == s[0]:
        return 1 + prefixLen(s[1:])
    return 1

def compress(s):
    """Inputs a 64-bit binary sequence and returns a run-length encoding of the string."""
    def compressHelp(s, b):
        if s == '':
            return ''
        if s[0] != chr(b + ord('0')):
            return numToBinaryPadded(0) + compressHelp(s, 1 - b)
        prefix_len = min(prefixLen(s), MAX_RUN_LENGTH)
        return numToBinaryPadded(prefix_len) + compressHelp(s[prefix_len:], 1 - b)
    return compressHelp(s, 0)
#325 because 64*5 = 320, then you add 5 when the bits start with 1.

def uncompress(s):
    """Inputs a run-length encoding and returns its represented binary sequence.
    It "inverts" or "undoes" the compressing in the compress function."""
    def uncompressHelp(s, b):
        if s == '':
            return ''
        n = binaryToNum(s[:COMPRESSED_BLOCK_SIZE])
        return chr(b + ord('0')) * n + uncompressHelp(s[COMPRESSED_BLOCK_SIZE:], 1 - b)
    return uncompressHelp(s, 0)

def compression(s):
    """Returns the ratio of the compressed size to the original size for image s."""
    return len(compress(s))/len(s)

#Tested s = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100". The ratio is 1.484375.
#Tested s = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0". The ratio is 1.0156.
#Tested s = "1001" * 16. The ratio is 2.539.

#Professor Lai's algorithm does not always return a shorter string. 
#In the case where the block size is one, the string will be the same.
#This is because block sizes are always greater than or equal to one.
#Therefore, the ratio of the compressed size to the original will always be > or = to 1.