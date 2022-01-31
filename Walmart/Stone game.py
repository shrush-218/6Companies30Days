'''
    Walmart Question 2: Stone Game

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number 
of stones piles[i]. The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there 
are no ties. Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning 
or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

'''
from collections import defaultdict
class Solution:
    def stoneGame(self, piles):       
        self.dp_table = defaultdict( int )       
        def maximize_score_gap( piles, left, right):            
            if left == right:
                return piles[left]            
            if (left, right) in self.dp_table:
                return self.dp_table[ (left, right)] 
            choose_left = piles[left] - maximize_score_gap( piles, left+1, right)
            choose_right = piles[right] - maximize_score_gap( piles, left, right-1)
            self.dp_table[ (left,right) ] = max( choose_left, choose_right )
            return self.dp_table[ (left,right) ]
        
        score_gap_for_alex = maximize_score_gap( piles, left = 0, right = len(piles)-1 )        
        return score_gap_for_alex > 0