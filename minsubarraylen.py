def minSubArrayLen(target, nums):
	"""
	:type target: int
	:type nums: List[int]
	:rtype: int
	"""

	start = 0
	end = 0
	total = 0
	smallest = 10**9
	while end < len(nums):
		total += nums[end]
		
		if total >= target:
			smallest = min(smallest,(end+1)-start)
			start +=1
			end = start
			total = 0
			continue
		end +=1
	return smallest


target = 7
nums = [2,3,1,2,4,3]
#             ^
#           ^
# nums = [1,1,1,1,1,1,1,1]

x  = minSubArrayLen(target,nums)
print(x)