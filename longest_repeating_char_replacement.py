def characterReplacement(s, k):
	"""
	:type s: str
	:type k: int
	:rtype: int
	""" 
	left = 0
	characterCounts = {}
	replacementsNeeded = 0
	mostFrequentCount = 0
	longest = 0
	for right in range(len(s)):

		currentLen = (right - left + 1)

		if s[right] in characterCounts:
			characterCounts[s[right]] +=1
		else:
			characterCounts[s[right]] =1
		#keep track of the character that appears the most times in the substring
		mostFrequentCount = max(mostFrequentCount,characterCounts[s[right]])

		while currentLen - mostFrequentCount > k:
			#there are too many differing characters
			#we need to lower the amount of characters in the substring
			characterCounts[s[left]] -=1
			left +=1
			currentLen = (right - left + 1)
		longest = max(longest,currentLen)
	return longest
s = "ABABBA"
print(characterReplacement(s,2))