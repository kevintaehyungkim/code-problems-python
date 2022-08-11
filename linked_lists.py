
####################
### DETECT CYCLE ###
####################
'''
Given a linked list, determine if it has a cycle in it.
'''
def has_cycle(head):
	slow = fast = head
	while fast:
		slow = slow.next
		if fast.next:
			fast = fast.next.next
		else: 
			return False
		if slow is fast:
			return True
	return False



#####################################
### INTERSECTION TWO LINKED LISTS ###
#####################################
'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# only 2 ways to get out of the loop, they meet or the both hit the end=None
# time: O(m+n) worst case
# space: O(1)
def getIntersectionNode(headA, headB):
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = headB if not p1 else p1.next
        p2 = headA if not p2 else p2.next
            
    return p1
    

##############################
### PALINDROME LINKED LIST ###
##############################
'''
Cracking the Coding Interview
2.6: Implement a function to check if a linked list is a palindrome.
'''
def is_palindrome(head):
    if not head:
        return True
    stack = Stack()
    slow = fast = head
    while fast and fast.next:
        stack.push(slow.val)
        slow = slow.next
        fast = fast.next.next
    # odd nodes
    if fast: 
        slow = slow.next
    # even nodes
    else:
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
    return True


#####################################
### MERGE TWO SORTED LINKED LISTS ###
#####################################
'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''

# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2



# only 2 ways to get out of the loop, they meet or the both hit the end=None

###########################
### REVERSE LINKED LIST ###
###########################
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

def reverse_linked_list(head, last=None):
	if 
	p1 = head
	p2 = head.next

#Iteratively
# Time Complexity - O(n), Space Complexity - O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur_node = head
        while cur_node:
            cur_node.next, prev, cur_node = prev, cur_node, cur_node.next
        return prev

#Recursively
#Time Complexity - O(n), Space Complexity - O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversedList = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return reversedList
















