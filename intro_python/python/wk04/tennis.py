def score(pl_one, pl_two):
    names = ['Player 1', 'Player 2']
    scores = ['love', '15', '30', '40', 'set']
    eq   = ['Love all', '15 all', '30 all']
    if pl_one == pl_two:
        return [eq[pl_one], False ]


    # Starting (Zero Zero)
    #if (pl_one == 0) and ( pl_two == 0):
    #    return ['Love all', False ]
    

print(score (0,0)[0]) # returns Love all
print(score (0,0)[1]) # returns False
print(score (1,1)[0]) # 
#print(score (2,2)[0]) # 


