class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        else:
            diff = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    diff.append(i)
                
            if len(diff) > 2:
                return False
            elif len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
                return True
            elif len(diff) == 0 and len(set(s)) < len(s):
                return True
