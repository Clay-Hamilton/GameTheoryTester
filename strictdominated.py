'''
Created on Feb 27, 2019

@author: Clay Hamilton

Creates five functions:

is_strictly_dominated_first takes in an action profile u1 and two strategies w1 and s1,
    and determines whether w1 is strictly dominated by s1.
is_strictly_dominated_second does the same with the second user's profile.

remove_one_strictly_dominated_first takes in action profiles u1 and u2 looks for one
    of u1's strategies that is strictly dominated and removes it (if one exists).
remove_one_strictly_dominated_second does the same for u2.

remove_all_strictly_dominated iteratively removes strictly dominated strategies
    until there are none left for u1 or u2.
'''

#Prisoner's Dilemma
a = [[-1,-4],[0,-3]]
b = [[-1,0],[-4,-3]]

def is_strictly_dominated_first(u1, w1, s1):
    for i in range(len(u1[w1])):
        if u1[w1][i] >= u1[s1][i]:
            return False
    return True

print (is_strictly_dominated_first(a,0,1))
print(is_strictly_dominated_first(a,1,0))

def is_strictly_dominated_second(u2, w2, s2):
    for i in range(len(u2)):
        if u2[i][w2] >= u2[i][s2]:
            return False
    return True

print(is_strictly_dominated_second(b,0,1))
print(is_strictly_dominated_second(b,1,0))

def remove_one_strictly_dominated_first(u1,u2):
    for w1 in range(len(u1)):
        for s1 in range(len(u1)):
            if (is_strictly_dominated_first(u1,w1,s1)):
                #print("%d dominated by %d" % (w1,s1))
                del u1[w1]
                del u2[w1]
                return True
    return False

print(remove_one_strictly_dominated_first(a,b))
print(a)
print(b)

c = [[-1,-4],[-1,-3]]
d = [[-1,0],[-4,-3]]

print(remove_one_strictly_dominated_first(c,d))
print(c)
print(d)


def remove_one_strictly_dominated_second(u1,u2):
    for w2 in range(len(u2[0])):
        for s2 in range(len(u2[0])):
            if (is_strictly_dominated_second(u2,w2,s2)):
                #print("%d dominated by %d" % (w2,s2))
                for i in range(len(u2)):
                    del u1[i][w2]
                    del u2[i][w2]
                return True
    return False

print(remove_one_strictly_dominated_second(a,b))
print(a)
print(b)

#Problem 5 3x3:
c = [[13,1,7], [4,3,6], [-1,2,8]]
d = [[3,4,3], [1,3,2], [9,8,-1]]

def remove_all_strictly_dominated(u1,u2):
    notover = True
    while (notover == True):
        notover = remove_one_strictly_dominated_first(u1,u2)
        notover = remove_one_strictly_dominated_second(u1,u2)


remove_all_strictly_dominated(c,d)
print(c)
print(d)

c = [[1,1,1], [2,2,2], [2,2,1]]
d = [[3,2,2], [1,0,2], [2,1,1]]

remove_all_strictly_dominated(c,d)
print(c)
print(d)
