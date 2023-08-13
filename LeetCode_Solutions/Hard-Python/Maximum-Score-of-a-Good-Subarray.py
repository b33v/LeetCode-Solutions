class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_score = 0
        min_val = nums[k]

        i = j = k
        while True:
            while i > 0 and nums[i-1] >= min_val:
                i -= 1
            while j < n-1 and nums[j+1] >= min_val:
                j += 1

            max_score = max(max_score, min_val * (j - i + 1))

            if i == 0 and j == n-1:
                break

            if i > 0 and (j == n-1 or nums[i-1] > nums[j+1]):
                min_val = min(min_val, nums[i-1])
                i -= 1
            else:
                min_val = min(min_val, nums[j+1])
                j += 1

        return max_score
