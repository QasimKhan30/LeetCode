"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
After flipping, the maximum number of consecutive 1s is 4.
"""

def findMaxConsecutiveOnes(nums):
	left = 0
	n = len(nums)
	flips_available = 1
	count = 0
	longest = 0
	for right in range(n):
		numsRight = nums[right]
		numsLeft = nums[left]

		if nums[right] == 0:
			while flips_available == 0:
				if nums[left] == 0:
					flips_available +=1
				count -=1
				left +=1
			
		count +=1
		longest = max(longest,count)
	return longest



nums = [1,0,1,1,1,0]
# nums = [1,1,1,0,0,0,1,1,1,1,0]
print("-0s")
print(findMaxConsecutiveOnes(nums))