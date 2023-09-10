"""
Longest Substring with at most two distinct characters
given a string s find the length of the longest substring t that contains at most 2 distinct characters 

"eceba" -> 3 because  t = "ece"
"ccaabbb" -> aabbb
"""
def lengthOfLongestSubstringTwoDistinct(s):
	left = 0
	right = 0
	distinctChars = dict()

	longestSubstring = -1

	while right < len(s):
		if s[right] in distinctChars:
			distinctChars[s[right]] += 1
			
		else:
			
			distinctChars[s[right]] = 1
			
		while len(distinctChars) > 2:
			#slide left pointer
			

			distinctChars[s[left]] = distinctChars[s[left]] - 1

			if distinctChars[s[left]] == 0:
				
				distinctChars.pop(s[left])

				
			left +=1

		curSubstingLen = 0
		for value in distinctChars.values():
			curSubstingLen  += value
		longestSubstring = max(longestSubstring,curSubstingLen)
		right +=1
	return longestSubstring


s = "ccaabbb"
s = "eceba"
print(lengthOfLongestSubstringTwoDistinct(s))

"""
01234
eceba
^
   ^


distinctChars = { e:2,c:1 }
"""