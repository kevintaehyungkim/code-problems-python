

'''
1. https://leetcode.com/discuss/interview-question/1655441/amazon-oa

-> keep track of only -1 indices 
-> if # -1's is even -> return original arr


-> get first and last indices of -1 
-> whichever side removing gives largest -> return spliced arr



2. rank imbalance if any pair in group has diff more than 1 

1223

12
13

123 



12
12
13 - 1




1355  -> 


13 - 1
15 - 1
15 - 1

35 - 1
35 - 1

55 - 0



1355 -> 4 

1357 -> 6 


dp[for 5] -> 3 

1 2 2 1 



13 3 
15
17 

35 2 
37


135 - 2 
137 - 2 
357 - 2 

1357 - dp[i]

ABC
BA, CA CB 


if curr == prev:
	dp[i] = dp[i-1] 
else: 
	dp[i] = dp[i-1] + 1 




i = 0 
-> [3, 2, 0, 0]




skip i = 1 




134 - 
135 - 
345 - 

1345 - 





dp[i] += 1



initial i = 0 
-> dp = [3, 1, 0, 0]

i = 1 
-> 







temp = [0, 1, 1]
'''



def zzz(ranks):

	result = 0  
	ranks = sorted(ranks)
	num_of_ranks = len(ranks)

	for index in range(num_of_ranks - 1):
		if ranks[index + 1] - ranks[index] > 1:
			result += num_of_ranks - index - 1
		elif ranks[index + 1] - ranks[index] == 1:
			result += num_of_ranks - index - 2

	return result


print(zzz([1,2,3,4,5]))

