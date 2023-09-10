def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	left = 0
	right = 0
	checked = set()
	longest = 0
	
	for right in range(len(s)):
		s_right = str(right) + ": " +  s[right]
		s_left = str(left) + ": " +  s[left]
		while s[right] in checked:
			checked.remove(s[left])
			left +=1
		checked.add(s[right])
		longest = max(longest,len(checked))
	return longest
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
print(lengthOfLongestSubstring(s))