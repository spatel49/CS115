'''
Created on Sep 19, 2018
@author: Siddhanth Patel
username: spate144
I pledge my honor that I have abided by the Stevens Honor System.
'''
import time
import turtle

def fib(n):
    if n<= 1:
        return n
    return fib(n-1) + fib(n-2)

start_time = time.time()
#print(fib(27))
#print('Computation time without memoization: %.2f' % (time.time() - start_time))

"""Memoization:
1. If key is in the dictionary return the value associated with the key.
2. Do work! = Use cw_recursion to do the work but store the results in a local variable.
3. Store the results in the dictionary and return the result."""
    

def fib_memo(n):
    def fib_helper(n, memo):
        # if key is in memo, return memo[n]
        if n in memo:
            return memo[n]
        # Do work!
        # Recursively compute the next fibonacci number.
        # Store the result in a local variable.
        if n <= 1:
            result = n
        else:
            result = fib_helper(n-1, memo) + fib_helper(n-2, memo)

        # Store result in memo and return result.
        memo[n] = result
        return result
    return fib_helper(n, {})


#start_time = time.time()
#print(fib_memo(40))
#print('Computation time with memoization: %.2f' % (time.time() - start_time))

def LCS(s1, s2):
    """Returns the length of the longest common subsequence in strings s1 and s2"""
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))

start_time = time.time()
#print(LCS("qwekfe", "qweksdadb"))
#print('LCS Computation time with memoization: %.2f' % (time.time() - start_time))


def fast_LCS_with_values(s1, s2):
    def fast_LCS_helper(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1, s2)]
        if s1 == '' or s2 == '':
            result = [0, '']
        elif s1[0] == s2[0]:
            lose_both = fast_LCS_helper(s1[1:], s2[1:], memo)
            result = [1 +lose_both[0], s1[0] + lose_both[1]]
        else:
            useS1= fast_LCS_helper(s1, s2[1:], memo)
            useS2= fast_LCS_helper(s1[1:], s2, memo)
            if useS1[0]>useS2[0]:
                result = useS1
            else:
                result= useS2
                memo[(s1,s2)] = result
        return result
    return fast_LCS_helper(s1, s2, {})

start_time = time.time()
print(fast_LCS_with_values("qwekfhwe", "qweksdb"))
print('LCS Computation time with memoization: %.2f' % (time.time() - start_time))

def subset_with_values(target, lst):
    """Determines whether or not it is possible to create the target sum using values in the list. Values in the list
    can be positive, negative, or zero. The function returns a tuple of exactly two items. The first is a Boolean that indicates
    True if the sum is possible and False if it's not.
    The second element in the tuple is a list of all the values that add up to make the target sum."""
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0] == True:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

start_time = time.time()
print(subset_with_values(5,[3,1,5,6,7,8,9,4,3,2]))
print('subset Computation time with memoization: %.2f' % (time.time() - start_time))


