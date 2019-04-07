'''
Created on April 4, 2019

@author: Clay Hamilton

This function uses backward induction algorithm to find
the pay-off in a subgame perfect equilibrium of a given centipede game.
It returns the tuple representing the pay-offs of the two players.
'''

l = [(1,2), (3,4), (15,5), (7,8), (9,10)]


def centipede (list):
    list.reverse()
    print(list)
    next = list[0]
    whoseturn = 0
    finalchoice = 0
    for tup in range(len(list)-1):
        if whoseturn%2 == 0:
            if list[tup+1][1] > next[1]:
                next = list[tup+1]
        else:
            if list[tup+1][0] > next[0]:
                next = list[tup+1]
        whoseturn+= 1
    
    return next

print(centipede(l))
