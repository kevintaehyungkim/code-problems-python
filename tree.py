
'''
Print a binary tree row-by-row, printing left-to-right for even numbered rows and right-to-left for odd numbered rows.
'''


#####################
### BST SER/DESER ###
#####################
'''
Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string 
can be deserialized to the original tree structure.

Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.
'''

# preorder(root, left, right) DFS to serialize
def serialize(node, ser_arr=None):
	if not node:
		return ser_arr.append("None")

	ser_arr.append(node.val)
	ser_arr = serialize_bst(node.left, ser_arr)
	ser_arr = serialize_bst(node.right, ser_arr)

	return ser_arr

def deserialize(data):
	if not data: 
		return None

	node = TreeNode(data[0])
	node.left = self.deserialize(data[1])
	node.right = self.deserialize(data[2])

	return node
		


###########################
### CALENDAR SCHEDULING ###
###########################
'''
Implement a MyCalendar class to store your events. 
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). 
Formally, this represents a booking on the half open interval [start, end), 
the range of real numbers x such that start <= x < end.
'''

# key: events conflict when s1 < e2 AND s2 < e1.
class TreeNode():
	def __init__(self, s, e):
		self.s = s
		self.e = e
		self.left = None
		self.right = None

class MyCalendar:

	def __init__(self):
		self.root = None

	def book(self, start: int, end: int) -> bool:
		if not self.root:
			self.root = TreeNode(start, end)
			return True
		else:
			return self.insert(start, end, self.root)

	# try to decide where I can go
	# if my start is greater than or equal to end then go to the right
	# equal is allowed as "end" is not part of the interval

	# if my end is less than or equal to the start then go to the left
	# equal is allowed as "end" is not part of the interval
	def insert(self, s, e, node):
		if s >= node.e: 
			if node.right:
				return self.insert(s, e, node.right)
			else:
				node.right = TreeNode(s, e)
				return True
		elif e <= node.s: 
			if node.left:
				return self.insert(s, e, node.left)
			else:
				node.left = TreeNode(s, e)
				return True
		else:
			return False



###################################
### CLOSEST LEAF IN BINARY TREE ###
###################################
'''
We use a depth-first search to record in our graph each edge travelled from parent to node.

After, we use a breadth-first search on nodes that started with a value of k, 
so that we are visiting nodes in order of their distance to k. 
When the node is a leaf (it has one outgoing edge, where the root has a "ghost" edge to null), 
it must be the answer.
'''

# key idea: treat as undirected graph -> DFS then BFS 
# time: O(N)
# space: O(N)
def findClosestLeaf(self, root, k):

	if not root or not k:
		return

    def find_edges(node, parent = None):
        if node:
            graph[node].append(parent)
            graph[parent].append(node)
            find_edges(node.left, node)
            find_edges(node.right, node)

	graph = collections.defaultdict(list)
    find_edges(root)
    queue = collections.deque(n for n in graph if n and n.val == k)
    seen = set(queue)

    while queue:
        node = queue.popleft()
        if node:
            if len(graph[node]) <= 1:
                return node.val
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    queue.append(n)


##########################
### INVERT BINARY TREE ###
##########################
'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Time: O(n)
Space: O(n)
'''

# Recursive Solution
def invert_binary_tree(root):
	if root:
		root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
	return root

# Iterative Solution
def invert_binary_tree(root):
if not root:
	return None

	q = Queue()
	q.enqueue(root)

	while q:
		node = q.pop()
		if node.right:
			q.enqueue(node.right)
		if node.left: 
			q.enqueue(node.left)
		node.left, node.right = node.right, node.left

	return root



#########################
### IS BINARY SUBTREE ###
#########################
'''
Create an algorithm to determine if T2 is a subtree of T1. 
A tree T2 is a subtree of T1 if there exists node n in T1 such that the subtree of n is identical
to T2. That is, if you cut off the tree at node n, the two trees would be identical.
'''

def binary_subtree(t1, t2):
	if not t2:
		return False
	return contains_tree(t1,t2)


def contains_tree(r1, r2):
	if not r1:
		return False
	elif r1.val == r2.val and same_tree(r1,r2):
		return True
	else:
		return contains_tree(r1.left, r2) or contains_tree(r1.right, r2)


def same_tree(node1, node2):
	if not node1 and not node2:
		return True
	elif node1 and node2 and node1.val == node2.val:
		return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)
	else:
		return False



###########################
### IS SAME BINARY TREE ###
###########################
'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Time: O(n)
Space: O(logn) best case and O(n) worst case if tree is completely unbalanced
'''

def same_tree(r1, r2):
	if not r1 and not r2:
		return True
	if not r1 or not r2:
		return False
	if r1.val != r2.val:
		return False
	return same_tree(r1.left, r2.left) and same_tree(r1.right, r2.right)



############################
### K_TH SMALLEST IN BST ###
############################
'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
- add a variable to the TreeNode to record the size of the left subtree
- insert or delete a node in the left subtree, we increase or decrease it by 1
'''

# time: O(n)
# space: O(n)
def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    
    def inorder(root):
        if root==None:
            return []

        left_list = inorder(root.left)
        right_list = inorder(root.right)
        return left_list + [root.val] + right_list 
    
    arr = inorder(root)
    return arr[k-1]



##############################
### LOWEST COMMON ANCESTOR ###
##############################
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Explanation: The LCA of nodes 5 and 1 is 3.
'''
def lowestCommonAncestor(self, root, p, q):
    # Stack for tree traversal
    stack = [root]

    # Dictionary for parent pointers
    parent = {root: None}

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:

        node = stack.pop()

        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
        ancestors.add(p)
        p = parent[p]

    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q



#################
### MAX DEPTH ###
#################
'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# time: O(n)
# space: O(n) worst case, O(logN) best case if balanced tree
def maxDepth(root):
    if not root: 
        return 0
    return max(1+maxDepth(root.left), 1+maxDepth(root.right))



####################
### MAX PATH SUM ###
####################
'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree 
along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

'''
using recursion, keep track of: 

1. just node
2. node + left child
3. node + right child
4. left child + node + right child

pick the path which provides max sum
'''

def max_path_sum(root):
	max_sum = float('-inf')
	max_gain(root)
	return max_sum

	



def max_gain(node):
	nonlocal max_sum
	if not node:
		return 0
	
	left = max_sum(root.left, 0)
	right = max_sum(roof.right, 0)
	entire = node.val + left + right
	
	max_sum = max(max_sum, entire)

	return node.val + max(left, right)



#################
### VALID BST ###
#################
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

'''
Explanation:

Every node to the left of root has to be less than root.
Every node to the right of root has to be greater than root.

That means one should keep both upper and lower limits for each node while traversing the tree, 
and compare the node value not with children values but with these limits.

If we traverse left, upper limit is root -> every node has to be less than root
It we traverse right, lower limit is root -> every node has to be greater than root
'''

# main method
def check_bst(root):
	if root:
		return verify_node(root)
	return True

# helper recursive method
def verify_node(node, lower=float('-inf'), upper=float('inf')):
	if node:
		if node.val >= upper or node.val <= lower:
			return False
		return verify_node(node.left, lower, node.val) and verify_node(node.right, node.val, upper)
	return True



############################################
### BINARY TREE VERTICAL ORDER TRAVERSAL ###
############################################
'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
'''

# key idea: pre-order traversal using queue and keep track of min and max cols.
# time: O(N)
# space: O(N)
def verticalOrder(root):
    if not root:
        return []
    
    col_nodes = collections.defaultdict(list)
    min_col, max_col = 0, 0
    queue = [(root, 0)]
    
    for node, col in queue:
        if node:
            col_nodes[col].append(node.val)
            min_col, max_col = min(min_col, col), max(max_col, col)
            queue += (node.left, col-1), (node.right, col+1)
            
    return [col_nodes[col] for col in range(min_col, max_col+1)]



