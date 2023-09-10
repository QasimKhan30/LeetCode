"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
After flipping, the maximum number of consecutive 1s is 4.
"""

def findMaxConsecutiveOnes(nums):
	left = 0
	zeroCount = 0
	longest = 0
	
	for right in range(len(nums)):
		if nums[right] == 0:
			zeroCount +=1
		while zeroCount > 1:
			if nums[left] == 0:
				zeroCount -=1
			left +=1
		longest = max(longest,(right - left + 1))
	return longest
nums = [1,0,1,1,1,0]

nums = [1,1,1,0,1,1,1,1,0]
print(findMaxConsecutiveOnes(nums))
