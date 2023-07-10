class Solution(object):
    def findTheWinner(self, n, k):
        k = k-1
        index = 0
        circle = [i for i in range(1,n+1)]
        def winner(k,index):
            if len(circle) == 1:
                return circle[0]
            index = (index + k)% len(circle)
            del circle[index]
            return winner(k,index)
        return winner(k,index)
