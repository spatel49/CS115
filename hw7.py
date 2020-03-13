'''
Created on October 23, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

CS115 - Hw 7
'''
FullAdder = {
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1')
}

def numToBaseB(N, B):
    """converts decimal number to number in Base B"""
    if N == 0:
        return "0"
    return str(int(numToBaseB(int(N / B), B) + str(N % B)))

#print(numToBaseB(10,2))

def baseBToNum(S, B):
    """Converts number in base B to number in decimal"""
    if S == "":
        return 0
    return baseBToNum(S[:-1], B) * B + int(S[-1])

#print(baseBToNum('1000', 2))

def baseToBase(B1, B2, SinB1):
    """converts SinB1 from base B1 to B2"""
    return numToBaseB(baseBToNum(SinB1, B1), B2)

#print(baseToBase(2, 10, '10'))

def add(S,T):
    """Adds two binary strings, S and T, by converting to decimal, adding them, and reversing back to binary"""
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)
#print(add('1101', '1101'))

def addB(X,Y):
    pad = len (X) - len(Y)
    if len(X) > len(Y):
        Y = "0" * pad + Y
    if len(X) < len(Y):
        X = "0" * pad + X
    def addB_helper(carryout, X, Y):
        if X == "":
            return "" if carryout == '0' else '1'
        return addB_helper(FullAdder[(carryout, X[-1], Y[-1])][1], X[:-1], Y[:-1]) + FullAdder[(carryout, X[-1], Y[-1])][0]
    return addB_helper('0', X, Y)

#print(addB('011', '100'))
