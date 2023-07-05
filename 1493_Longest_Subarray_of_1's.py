class Solution(object):
    def longestSubarray(self, nums):
        current_length = 0
        prev_length = 0
        max_length = 0
        has_zero = False

        for num in nums:
            if num == 1:
                current_length += 1
                prev_length += 1
            else:
                has_zero = True
                max_length = max(max_length, prev_length)
                prev_length = current_length
                current_length = 0

        max_length = max(max_length, prev_length)

        if not has_zero:
            return len(nums) - 1
        elif max_length == len(nums):
            return max_length - 1
        else:
            return max_length

"""
문제는.. 0이 예시보다 여러 번 나올 경우ㅠ

다른 실패한 시도..
class Solution(object):
    def longestSubarray(self, nums):
        current_length = 0
        zero_count = 0
        lengths = []
        max_sum = 0

        for num in nums:
            if num == 1:
                current_length += 1
            else:
                zero_count += 1
                if zero_count % 2 == 0:
                    lengths.append(current_length)
                    current_length = 0

        if zero_count % 2 == 1:
            lengths.append(current_length)

        if zero_count == 0:
            return len(nums) - 1
        else: 
            max_sum = lengths[0] + lengths[1]

            for i in range(1, len(lengths) - 1):
                current_sum = lengths[i] + lengths[i + 1]
                if current_sum > max_sum:
                    max_sum = current_sum

            return max_sum
"""
