class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        maxDiff = float('inf')
        ans = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]
                difference = abs(target - total)

                if difference < maxDiff:
                    maxDiff = difference
                    ans = total

                if total == target:
                    return total

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return ans