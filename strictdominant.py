'''
Created on Feb 18, 2019

@author: Clay Hamilton

Creates three functions:

is_strictly_dominant takes in an action profile u1 and a strategy s1,
    and determines whether that strategy is strictly dominant.
    
is_strictly_dominant_second does the same, but for the second user (meaning 
    it goes by the columns, not the rows).
    
find_strictly_dominant_strategies takes in action profiles u1 and u2 and
    calculates what the strictly dominant strategy is for each (if they have one).
'''

#Prisoner's Dilemma
a = [[-1,-4],[0,-3]]
b = [[-1,0],[-4,-3]]

#Battle of Sexes
battlea = [[2,0],[0,1]]
battleb = [[1,0],[0,2]]

#Matching Pennies
penniesa = [[1,-1],[-1,1]]
penniesb = [[-1,1],[1,-1]]

#Rock, Paper, Scissors
rpsa = [[0,-1,1],[1,0,-1],[-1,1,0]]
rpsb = [[0,1,-1],[-1,0,-1],[1,-1,0]]

#Red, Blue
redbluea = [[0,1000],[-1000,0]]
redblueb = [[0,-1000],[1000,0]]

#Two-by-three
twobythreea = [[0,1,2],[1,0,3]]
twobythreeb = [[1,0,2],[1,0,3]]

"""
testa = [[1,1],[0,0],[2,3]]
testa2 =[[-1,-4],[0,-3]]
testb = [[1,0,2],[1,0,3]]
"""


def is_strictly_dominant(u1,s1):
    for a in range(len(u1[0])):
        for b in range(len(u1)):
            if u1[s1][a] < u1[b][a]:
                return False
    return True

print(is_strictly_dominant(a, 0))
print(is_strictly_dominant(a, 1))

def is_strictly_dominant_second(u2,s2):
    for a in range(len(u2)):
        for b in range(len(u2[0])):
            if u2[a][s2] < u2[a][b]:
                return False
    return True

print(is_strictly_dominant_second(b,0))
print(is_strictly_dominant_second(b,1))

def find_strictly_dominant_strategies(u1,u2):
    stdom = None
    stdom2 = None
    for c in range(len(u1)):
        if is_strictly_dominant(u1, c):
            stdom = str(c)
            break
        
    for d in range(len(u2[0])):
        if is_strictly_dominant_second(u2, d):
            stdom2 = str(d)
            break
    
    if stdom == None:
        print("The first player has no strictly dominant strategy")
        
    else:
        print ("The first player has strictly dominant strategy %s" % stdom)
    
    if stdom2 == None:
        print("The second player has no strictly dominant strategy")
        
    else:
        print ("The second player has strictly dominant strategy %s" % stdom2)


print("Prisoner's Dilemma: ")
find_strictly_dominant_strategies(a,b)

print("Battle of Sexes: ") 
find_strictly_dominant_strategies(battlea,battleb)

print("Matching Pennies: ") 
find_strictly_dominant_strategies(penniesa,penniesb)

print("Rock-Paper-Scissors: ")
find_strictly_dominant_strategies(rpsa,rpsb)

print("Red-Blue: ") 
find_strictly_dominant_strategies(redbluea,redblueb)

print("2x3: ") 
find_strictly_dominant_strategies(twobythreea,twobythreeb)

