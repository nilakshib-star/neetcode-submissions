class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=1 # becz is list is not empty then the 1st element is considered unique
        for i in range(1,len(nums)):  #(taking 1 instead of 0 bcz index 0 is already unique)
            if nums[i] != nums[i-1]:  #sorted array so duplicates are next to each other.
               nums[k] = nums[i]
               k += 1
        return k
