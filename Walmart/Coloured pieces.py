'''
    Walmart Question 3: Stone Game

There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] 
is the color of the ith piece. Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice 
moves first. Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces 
that are colored 'B'. Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove 
pieces that are colored 'A'. Alice and Bob cannot remove pieces from the edge of the line. If a player cannot make a move on their turn, that player 
loses and the other player wins. Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
            a = b = cnt = 0
            prev = 'C' 
            for cur in colors:
                if cur == prev:
                    cnt += 1
                    if cnt > 2:
                        if cur == 'A':
                            a += 1
                        else:
                            b += 1
                else:
                    cnt = 1
                prev = cur
            return a > b 