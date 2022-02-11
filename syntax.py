
#########
# ARRAY #
#########

# The zip() function takes iterables (can be zero or more), 
# aggregates them in a tuple, and returns it.
for c,d in zip(first, second):

# splice
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[1:]    # everything except the first item
a[:-1]   # everything except the last item

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

# sort by key (largest first)
sorted_counts = sorted(entry[1].items(), key = lambda x: x[0], reverse=True)

# sort by values (largest first)
sorted_counts = sorted(entry[1].items(), key = lambda x: x[1], reverse=True)

# arr to string
list1 = ['1', '2', '3']
str1 = ''.join(list1)

# random range
random.randrange(len(aux))
aux.pop(remove_idx)

###########
## CLASS ## 
###########
# A Sample class with init method
class Person:
   
    # init method or constructor 
    def __init__(self, name):
        self.name = name
   
    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', self.name)
   
p = Person('Nikhil')
p.say_hi()


################
## DICTIONARY ##
################

# python3
import collections 
collections.Counter(nums)

# setting up counter
num_count = {}
for num in nums:
    num_count[num] = num_count.get(num,0) + 1

# dictionary values -> {}
inner_dict = letter_count.get(c1, {})
inner_dict[c2] = inner_dict.get(c2, 0) + 1
letter_count[c1] = inner_dict

######################
## HEAPQ - MIN HEAP ##
######################
heap = []
    
# push
heapq.heappush(heap, k)
heapq.heappush(heap, (k, v))

# pop
heapq.heappop(heap)

# max heap
heapq.heappush(heap, -1*k)


#########
## SET ##
#########
my_set = {1, 2, 3}

# add an element
my_set.add(2)

# remove an element
my_set.remove(3)

# intersection (elements in both): O(min(s1,s2))
set1.intersection(set2)

# union (all elements derived from both): O(s1+s2)
set1.union(set2)


############
## STRING ##
############
str1 = ""

str1.isalpha()

str1.toupper()
str1.tolower()

# add how to go string -> array 
str1.split(' ')
str1.split(', ')

# find index 
index = str1.index(str2)

###########
## STACK ##
###########

# Last In First Out (DFS)
stack = []

stack.append('A')
stack.append('B')

stack.pop()


###########
## QUEUE ##
###########

# First In First Out (BFS)
queue = []

queue.append('A')
queue.pop(0)



##################################
############## ALGO ##############
##################################


#########
## BFS ## 
#########
# time: O(N) for tree, O(V+E) for graph
# queue implementation

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue


def iter_bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


def recursive_bfs(graph, q, discovered):
 
    if not q:
        return
 
    # dequeue front node and print it
    v = q.popleft()
    print(v, end=' ')
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            # mark it as discovered and enqueue it
            discovered[u] = True
            q.append(u)
 
    recursiveBFS(graph, q, discovered)

#########
## DFS ## 
#########
# time: O(N) for tree, O(V+E) for graph
# stack implementation 

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)



###################
## BINARY SEARCH ##
###################

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


###########
## GRAPH ##
###########

# cycle
 # base state: visit[i] = 0
 # if visited: visit[i] = -1
 # if visiting: visit[i] = 1
def is_cycle(i):
    if visit[i] == 1:
        return False
    if visit[i] == -1:
        return True
    visit[i] = -1
    for j in graph[i]:
        if is_cycle(j):
            return True
    visit[i] = 1
    return False


############
### TREE ### 
############
'''
If the given Binary Tree is Binary Search Tree:
- we can store it by either storing preorder or postorder traversal.
- inorder traversal of BST is an array sorted in the ascending order.
'''

# Pre-order Serialiation
def serialization(node, path):
    if node is None: return '#'
    
    path = ','.join([str(node.val), 
        serialization(node.left, path), 
        serialization(node.right, path)])
    
    return path
    
serialization(root,'')


###############
## RECURSION ## 
###############

def main(stones):
    visited = set()
    ...
    def helper(value,k):
        ...
        visited.add((value,k))
        ...
        return goFurther(value+k,k) or goFurther(value+k,k+1)
    
    return helper(stones[0],1)


MoneyMoney3238!

MoneyBunny1234!

Science4life!

