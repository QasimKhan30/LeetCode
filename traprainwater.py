def trap(height):
	"""
	:type height: List[int]
	:rtype: int
	"""
	total = 0
	leftptr = 0
	rightptr = len(height) - 1
	max_wall_left = height[leftptr]
	max_wall_right = height[rightptr]
	while leftptr < rightptr:
		max_wall_left = max(max_wall_left,height[leftptr])
		max_wall_right = max(max_wall_right,height[rightptr])
		
		
		if max_wall_left <= max_wall_right:
			leftptr +=1
			if max_wall_left - height[leftptr] >= 0:
				total += max_wall_left - height[leftptr]
		else:
			rightptr -=1
			if max_wall_right - height[rightptr] >= 0:
				total += max_wall_right - height[rightptr]
	return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]

trap(height)