'''
Created on Oct 29, 2018

@author: sypat
'''
import time
import random

sum=0
for i in range(10):
    sum += i
print(sum)

def map_sqr(lst):
    """Assume lst is a list. Return map(sqr, lst)"""
    result = []
    for x in lst:
        result.append(x + x)
    return result

def spamify(word):
    vowels = ['a','e','i','o','u']
    for i in range(len(word)):
        if word[i] not in vowels:
            return word[0:i] + 'spam' + word[1+i:]
    return word

print(spamify("aardvark"))    

def map_sqr_lst_comprehension(lst):
    return [x*x for x in lst]

print(map_sqr([1,2,3,4]))

print(map_sqr_lst_comprehension([1,2,3,4]))


def find_max(lst):
    """Returns the maximum element in a list"""
    if lst == []:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

print(find_max([1,2,3,4,5]))

def find_min_max(lst):
    """returns a tuple of both the min and max values in the list"""
    if lst == []:
        return None
    max_val = lst[0]
    min_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
        elif x < min_val:
            min_val = x
    return (min_val, max_val)
    
print(find_min_max([1,2,3,4,5]))


#Shallow Copy:
L = [1,2,3,4]
L[2] = 4
M= list(L) # Same as: M = shallow_copy(L) OR M= L[:]
M[0] = 12
print(L)
print(M)

L = [1,2,[3,4]]
M= list(L) # Same as: M = shallow_copy(L) OR M= L[:]
M[2][0] = 12
print(L)
print(M)

def shallow_copy(lst):
    new_list = []
    for x in lst:
        new_list.append(x)
    return new_list

def shallow_copy_list_comprehension(lst):
    return [x for x in lst]

L = [1,2,[3,[4,5]]]
M = shallow_copy_list_comprehension(L)
L[2] = 4
print(M)
print(L)

def deep_copy(lst):
    new_list = []
    for x in lst:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

L = [1,2,[3,[4,5]]]
M= deep_copy(L)
L[2][1][0] = 14
print(M)
print(L)

def sequential_search(key, lst):
    """Returns the index of key in lst, if it exists, and -1 otherwise."""
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

"""lo + (hi-lo)/2 == (hi+lo)/2"""
start_time = time.time()
print(sequential_search(99909,range(100001)))
print('sequential_search fast: %.2f' % (time.time() - start_time))


def binary_search(lst, key):
    """Searches the lst for key.
    Returns the index of key in lst, or -low - 1, if key is not present."""
    low =0
    high = len(lst) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if key < lst[mid]:
            high = mid -1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    return -low - 1

start_time = time.time()
print(binary_search(range(100001), 99909))
print('binary_ search fast: %.2f' % (time.time() - start_time))

i=0
while i < 2:
    i += 1
    print(i)

i = 0
while True:
    i += 1
    if i == 3:
        break
    print(i)
    
def mean(lst):
    total=0
    for i in lst:
        total += i
    return total / len(lst)

print(mean([1,2,3,4,5]))

def swap(lst, i, j):
    """Swaps lst[a] with lst[b]. a and b are indexes"""
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def selection_sort(lst):
    """Sorts the list using the O(n^2) selection sort algorithm. selection sort always makes n*(n-1)/2 comparisons and at most n-1 swaps...On^2"""
    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)
    return lst

print(selection_sort([1,5,4,6,6]))

"""random_list = [random.randint(1, 10000) for _ in range(20000)]
copy_list = list(random_list)
 
start = time.clock()
selection_sort(random_list)
print('Elapsed time: %.2f seconds' % (time.clock() - start)) 

start = time.clock()
copy_list.sort()
print('Elapsed time: %.2f seconds' % (time.clock() - start))
        """

def sort(a):
    count = 0
    for i in range(1, len(a)):
        count += 1
        current = a[i]
        j= 0
        while a[j] < current:
            j += 1
        for k in range(i, j,-1):
            a[k] = a[k-1]
        a[j] = current
        print(a, count)
    return a

a = [24,16,68,56,32]
print(sort(a))
        
print(list(range(3,1,-1)))  
        
def sortinsert(data):
    n = len(data)
    sum = 0
    for row in range(1,n,1):
        for col in range(1,n,1):
            while row == col:
                sum += data[row][col]
    return sum 
