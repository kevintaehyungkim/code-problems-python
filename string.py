

#####################
### DECODE STRING ###
#####################
'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
'''

def decode_string(s):
        stack, curNum, curString = [], 0, ''
        for c in s:
            if c == '[':
                stack.append((curString, curNum))
                curString, curNum = '', 0
            elif c == ']':
                prevString, num = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString



###################
### DECODE WAYS ###
###################
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2

Example 2:
Input: "226"
Output: 3
'''

# key idea: recursion w memoization
# time: O(N)
# space O(N)
def numDecodings(s):
    if not s:
        return 0
    
    code_set = set([str(i) for i in range(1,27)])
    seen = {}
    
    def decode(i):
        if i == len(s):
            return 1
        
        if i in seen:
            return seen[i]
        
        if s[i] in code_set:
        
            if i == len(s)-1:
                return 1
            
            res = decode(i+1)
            
            if i+1 < len(s) and s[i:i+2] in code_set:
                res += decode(i + 2)
                
            seen[i] = res
            return res

        return 0
    
    return decode(0)


##################
### IS ANAGRAM ###
##################
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Difficult: Easy
'''

# O(n) time
# O(1) space
def is_anagram(s,t):
	letter_dict = {}
	for letter in s:
		if letter in letter_dict:
			letter_dict[letter] = letter_dict[letter] + 1
		else:
			letter_dict[letter] = 1
	for letter in t:
		letter_dict[letter] = letter_dict[letter] - 1 
	for val in letter_dict.values():
		if val != 0:
			return False 
	return True


# O(nlogn) time
# O(1) space
def is_anagram(s,t):
	return sorted(s) == sorted(t)

if __name__ == '__main__':
  print is_anagram("anagram", "nagaram")




#####################################
### LONGEST PALINDROMIC SUBSTRING ###
#####################################
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
'''

# time: O(N^2)
# space: O(1)

class Solution(object):
    
    def longestPalindrome(self, s):
        longest_palindrome = ""
        for i in range(0,len(s)):
            single = self.palindrome_helper(i, i, s)
            double = self.palindrome_helper(i, i+1, s)
            
            current_longest = max(single, double, key=len)
            if len(current_longest) > len(longest_palindrome):
                longest_palindrome = current_longest
            
        return longest_palindrome
              

    def palindrome_helper(self, i1, i2, s):
        curr = ""
        while i1 >= 0 and i2 < len(s) and s[i1]== s[i2]:
            curr = s[i1:i2+1]
            i1 -= 1
            i2 += 1

        return curr



################################
### LONGEST UNIQUE SUBSTRING ###
################################
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# time: O(n)
# space: O(min(m,n))
def longest_unique_substring(s):
    start = end = 0
    max_length = 0
    alphabets = set()
    
    while end < len(s):
        if( s[end] not in alphabets ):
            alphabets.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            alphabets.remove(s[start])
            start += 1

    return max_length



################################
### MINIMUM WINDOW SUBSTRING ###
################################
'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''
# key idea: sliding window - if all char counts satisfied (all_present), remove from start 
# time: O(s+t)
# space: O(s+t)
def minWindow(self, s, t):
        
        dict_t = {} 
        for c in t: 
            dict_t[c] = dict_t.get(c,0) + 1
            
        temp_count = {} 
        start = end = 0
        all_present = False 
        shortest = ""
        
        def check_formed():
            for c in dict_t: 
                if temp_count[c] < dict_t[c]:
                    return False 
            return True 
        
        while end < len(s):
            s_end = s[end] 
            if s_end in dict_t:
                temp_count[s_end] = temp_count.get(s_end, 0) + 1
                if not all_present and len(temp_count.keys()) == len(dict_t.keys()):
                    all_present = check_formed()
                
            if all_present: 
                while start < end: 
                    s_start = s[start]
                    if s_start not in dict_t:
                        start += 1
                    elif temp_count[s_start] > dict_t[s_start]:
                        temp_count[s_start] -= 1
                        start += 1
                    else:
                        break

                if shortest == "": 
                    shortest = s[start:end+1]
                else: 
                    shortest = shortest if len(shortest) < (end-start+1) else s[start:end+1]
                
            end += 1    

        return shortest



###################################
### PALINDROMIC SUBSTRING COUNT ###
###################################
'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

# time: O(n^2)
# space: O(1)

class Solution(object):
    def countSubstrings(self, s):
        num_palindromes = 0
        for i in range(0,len(s)):
            num_palindromes += palindrome_helper(i, i, s)
            num_palindromes += palindrome_helper(i, i+1, s)
        return num_palindromes
              

def palindrome_helper(i1, i2, s):
    count = 0
    while i1 >= 0 and i2 < len(s) and s[i1]== s[i2]:
        i1 -= 1
        i2 += 1
        count += 1
        
    return count



##################
### WORD BREAK ###
##################
'''
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
# time: O(n^3) - recursion tree can go up to n^2, and substring computation O(n) space: O(n^2)
# space: O(n^2)
def wordBreak(s, wordDict):
    memo = {}

    def can_construct(s2):  
        
        if s2 in memo:
            return memo[s2]
        
        if s2 == "":
            return True
        
        for word in wordDict:
            if word == s2[0:len(word)]:
                suffix = s2[len(word):]
                
                if can_construct(suffix):
                    memo[s2] = True
                    return True
                
        memo[s2] = False
        return False

    return can_construct(s)



