'''
Created on March 7, 2019

@author: Clay Hamilton

Creates four functions:
maxmin_first takes in an action profile u1,
    and returns that user's maxmin strategy.
maxmin_second does the same with the second user's profile.

maxmin_first takes in an action profile u2,
    and returns that the first user's maxmin strategy.
maxmin_second takes in an action profile u1,
    and returns that the second user's maxmin strategy.

'''

a = [ [1,2,3,4],
      [6,3,8,5],
      [7,9,3,7],
      [1,2,3,1] ]

b = [ [6,2,8,4],
      [5,3,4,5],
      [7,6,5,6],
      [4,2,5,1] ]

def maxmin_first(u1):
    minlist = []
    for row in range(len(u1)):
        minlist.append(min(u1[row]))
    finlist = []
    maxnum = max(minlist)
    for i in range(len(minlist)):
        if minlist[i] == maxnum:
            finlist.append(i)
    return finlist

print(maxmin_first(a))


def maxmin_second(u2):
    minlist = []
    for col in range(len(u2[0])):
        minval = 100
        for row in range(len(u2)):
            if u2[row][col] < minval:
                minval = u2[row][col]
        minlist.append(minval)
    finlist = []
    maxnum = max(minlist)
    for i in range(len(minlist)):
        if minlist[i] == maxnum:
            finlist.append(i)
    return finlist

print(maxmin_second(b))

def minmax_first(u2):
    maxlist = []
    for row in range(len(u2)):
        maxlist.append(max(u2[row]))
    finlist = []
    minnum = min(maxlist)
    for i in range(len(maxlist)):
        if maxlist[i] == minnum:
            finlist.append(i)
    return finlist

print(minmax_first(b))

def minmax_second(u1):
    maxlist = []
    for col in range(len(u1[0])):
        maxval = 0
        for row in range(len(u1)):
            if u1[row][col] > maxval:
                maxval = u1[row][col]
        maxlist.append(maxval)
    finlist = []
    minnum = min(maxlist)
    for i in range(len(maxlist)):
        if maxlist[i] == minnum:
            finlist.append(i)
    return finlist

print(minmax_second(a))
