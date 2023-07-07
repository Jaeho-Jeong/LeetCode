class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        # https://www.youtube.com/watch?v=157I9vQ_ZsM 참고
        n = len(answerKey)
        length_T = 0
        length_F = 0
        L = 0
        R = 0
        ans = 0
        
        while R < n:
            if answerKey[R] == 'T':
                length_T += 1
            else:
                length_F += 1
            
            while min(length_T, length_F) > k:
                if answerKey[L] == 'T':
                    length_T -= 1
                else:
                    length_F -= 1
                
                L += 1
            
            ans = max(ans, length_T + length_F)
            R += 1
        
        return ans
