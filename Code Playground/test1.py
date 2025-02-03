class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1
        return ans, nums[:ans]
    
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))