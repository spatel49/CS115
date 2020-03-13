'''
Created on Nov 9, 2018

@author: sypat
'''
def num_matches(list1,list2):
    """Returns the number of elements that the two lists have in common"""
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
            matches +=1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

print(num_matches(['A','B','D'], ['A','B','C','D']))
print(num_matches([1,2,3,5,7,8,3,7,8,8,12,15,26], [1,2,5,7,8,3,7,8,8,12,14,26]))

def keep_matches(list1, list2):
    """Returns a list of the elements that the two lists have in common."""
    list1.sort()
    list2.sort()
    i = j = 0
    list = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            list.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return list

print(keep_matches(['A','C','D','F','F'], ['A','B','C','D','F','F',]))
print(keep_matches([1,2,3,5,7,8,3,7,8,8,12,15,26], [1,2,5,7,8,3,7,8,8,12,14,26]))

def drop_matches(list1, list2):
    """Returns a list of the elements that the two lists have not in common."""
    list1.sort()
    list2.sort()
    i = j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

print(drop_matches(['A','B','F','D'], ['A','B','C','D']))
print(drop_matches([1,2,3,5,7,8,3,7,8,8,12,15,26], [8]))
    