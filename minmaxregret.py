'''
Created on March 20, 2019

@author: Clay Hamilton

Creates four functions:
regret_matrix_second takes in an action profile u2,
    and returns that user's corresponding regret matrix.
regret_matrix_first the same with the second user's profile.

minmax_regret_first takes in an action profile u2,
    and returns that the first user's maxmin regret strategy.
maxmin_regret_second takes in an action profile u1,
    and returns that the second user's maxmin regret strategy.

'''

a = [ [1,2,3,4],
      [6,3,8,5],
      [7,9,3,7],
      [0,2,3,1]]

b = [[6,2,8,4],
     [5,3,4,5],
     [7,5,5,6],
     [4,2,5,1]]

def regret_matrix_second(u2):
    newmat = []

    for col in range(len(u2)):
        newmat.append([])
        maxnum = 0
        for num in range(len(u2[col])):
            if u2[col][num] > maxnum:
                maxnum = u2[col][num]
        for num in range(len(u2[col])):
            newmat[col].append(maxnum-u2[col][num])

    return newmat

print(regret_matrix_second(b))


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def regret_matrix_first(u1):
    return transpose(regret_matrix_second(transpose(u1)))

print(regret_matrix_first(a))

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

def minmax_regret_first(u1):
    newmat = regret_matrix_first(u1)
    return minmax_first(newmat)

print(minmax_regret_first(a))

def minmax_regret_second(u2):
    newmat = regret_matrix_second(u2)
    minmaxnum = 10 #the smallest maximum number
    tempmax = 0 #the maxnum of each column
    maxlist = []
    minmaxlist = []
    for col in range(len(newmat[0])):
        for row in range(len(newmat)):
            if newmat[row][col] > tempmax:
                tempmax = newmat[row][col]
        maxlist.append(tempmax)
        if tempmax < minmaxnum: #if it's less than the max of any other column make it the new min
            minmaxnum = tempmax
        tempmax = 0
    for num in range(len(maxlist)):
        if maxlist[num] == minmaxnum:
            minmaxlist.append(num)
    return minmaxlist

print(minmax_regret_second(b))

