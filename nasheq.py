'''
Clay Hamilton

Creates two functions:

check_nash takes in two users' action profiles and the choice for each one,
    and returns whether the result is a Nash Equilibrium.

find_nash takes in two users' action profiles and finds any Nash Equilibria
    using check_nash.

Then tests these functions using several popular Game Theory example games.
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
twobythreea = [[0,1,0],[0,1,0]]
twobythreeb = [[1,0,1],[1,0,1]]


def check_nash(u1,u2,s1,s2):
    isnash = True
    testspot = u1[s1][s2]
    for row in range(len(u1)):
        if testspot < u1[row][s2]:
            isnash = False
            break
    testspot = u2[s1][s2]
    for col in range(len(u2[0])):
        if testspot < u2[s1][col]:
            isnash = False
            break
    
    return isnash

print("[0,0] = ", check_nash(a,b,0,0))
print("[1,1] = ",check_nash(a,b,1,1))

def find_nash(u1,u2):
    nelist = []
    testspot = 0
    for row in range(len(u1)):
        for col in range(len(u1[0])):
            if check_nash(u1,u2,row,col):
                nelist.append([row,col])

    return nelist

print("Prisoner's Dilemma: ", find_nash(a,b))
print("Battle of Sexes: ", find_nash(battlea,battleb))
print("Matching Pennies: ", find_nash(penniesa,penniesb))
print("Rock-Paper-Scissors: ", find_nash(rpsa,rpsb))
print("Red-Blue: ", find_nash(redbluea,redblueb))
print("2x3: ", find_nash(twobythreea,twobythreeb))
                
    
    
