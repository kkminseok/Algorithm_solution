class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid+1

        return -1