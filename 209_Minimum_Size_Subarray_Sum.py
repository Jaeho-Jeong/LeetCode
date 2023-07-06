class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        minLength = n+1  # (최대+1)값으로 initialize -> 줄여나가기
        Sum = 0
        Left = 0

        for Right in range(n):
            Sum += nums[Right]  # 하나씩 더해서 Sum에 저장

            while Sum >= target:  # Sum이 target값 이상이 될 때까지,
                minLength = min(minLength, Right - Left + 1)  # 현재까지의 길이 update
                Sum -= nums[Left]  # Sum에서 왼쪽부터 하나씩 값 빼기
                Left += 1  # 왼쪽 포인터를 하나씩 늘리기
        
        if minLength == n+1:  # Sum이 target값 이하일 경우
            return 0
        else:
            return minLength
