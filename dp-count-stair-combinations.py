#Given n stairs to reach the top and you can take 1 or 2 steps at each stair . Find #ways a person can reach the top of the stairs. 
#n=4 result=5 variations=(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
#http://www.geeksforgeeks.org/count-ways-reach-nth-stair/

#Count stair combinations

#Solution 1: Recursive 
#Values are re-calcuated, not efficient
def countStairCombinationsRecursive(n):
	if n ==0:
		#top of the stairs
		return 1 #ONE PATH
	elif n < 0:
		return 0
	else:
		#take 1 step or two steps
		return countStairCombinationsRecursive(n-1) + countStairCombinationsRecursive(n-2)

'''
OBSERVATION:
1. At each stair you can take 1 step or 2 step
2. You reach top of stairs when #steps = 0
3. If you start top down, you can add already computer #combinations for n-1 and n-2
'''
#Solution 2: Dynamic Programming
def countStairCombinations(n):
	table = [0 for i in range(n+1)]
	table[0] = 0
	table[1] = 1
	table[2] = 2
	for i in range(3,n+1):
		table[i] = table[i-1] + table[i-2]
	return(table[n])

n = 4
print("n=%d #combinations=%d" % (n,countStairCombinations(n)))
