class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        runningSum = 0
        finalSum = 0
        maxSum = 0
        prevSum = 0
        for i in range(0,len(nums)):
            runningSum += nums[i]
            if runningSum == prevSum or i==len(nums)-1:
                finalSum = runningSum
                runningSum = 0
            if finalSum > maxSum:
                maxSum = finalSum
            prevSum = runningSum
        return maxSum

        