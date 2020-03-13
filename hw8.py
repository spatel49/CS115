'''
Created on October 29, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

CS115 - Hw 8
'''
def TcToNum(S):
    """Returns an integer that corresponds with an input string of 8 bits representing an integer's two's complement"""
    def TcToNum_Helper(S):
        if S == "":
            return 0
        else:
            return TcToNum_Helper(S[:-1]) * 2 + int(S[-1])
    if S[0] == '0':
        return TcToNum_Helper(S[1:])
    return TcToNum_Helper(S[1:]) - 128

print(TcToNum('10000010'))
# === 01111110 -> 126

def NumToTc(n):
    """Returns a string representing the two's complement of an integer"""
    def numToBinary(n):
        """Returns the binary representation of an integer"""
        if n ==0:
            return ''
        return numToBinary(int(n/2)) + str(n % 2)
    def padder(string):
        """Pads a binary string to 7 bits if it is originally less than 7"""
        return (7-len(string))*'0' + string
    if n > 127 or n <-128:
        return 'Error'
    if n >=0:
        return '0' + padder(numToBinary(n))
    return '1' + padder(numToBinary(n+128))

print(NumToTc(5))
    
    