class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occSet = set()
        for n in nums:
            if n in occSet:
                return True
            occSet.add(n)
        return False
