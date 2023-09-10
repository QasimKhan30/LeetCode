import random

def lengthOfLongestSubstringKDistinct(s, k):
	"""
	string -> s
	int -> k
	"""

	left = 0
	longest = 0
	distinctChars = dict()
	longestSubstring = 0

	for right in range(len(s)):
		s_right = str(right) + ": " +  s[right]
		s_left = str(left) + ": " +  s[left]
		if s[right] in distinctChars.keys():
			distinctChars[s[right]] += 1
		else:
			distinctChars[s[right]] = 1
		
		while len(distinctChars) > k:
			if distinctChars[s[left]] != 0:
				distinctChars[s[left]] -= 1

			if distinctChars[s[left]] == 0:
				distinctChars.pop(s[left])
				
			left +=1
		curSubstingLen = 0
		for value in distinctChars.values():
			curSubstingLen  += value
		longestSubstring = max(longestSubstring,curSubstingLen)
	return longestSubstring


"""
e c e b a
^
^

distinctChars = {e}
"""

s = "eceba"
k = 4

print(lengthOfLongestSubstringKDistinct(s,k))

nums = []

for i in range(10**3):
	nums.append(random.randint(0,1))
print(nums)