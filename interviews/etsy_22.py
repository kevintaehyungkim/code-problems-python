

'''


priority queue implementation push method and a pop method.

Reverse linkedlist between two indices 

asked to design a messaging feature to a website, debugging a flask application, general behavioural questions like Tell me about a time you have to deal with difficult employee etc.

dfs leetcode

print fibonacci sequence at number n

From a database design perspective, walk through your approach to building a messaging feature into the application.

'''

def reverseBetween(self, head, m, n):
    # Empty list
    if not head:
        return None

    # Move the two pointers until they reach the proper starting point
    # in the list.
    cur, prev = head, None
    while m > 1:
        prev = cur
        cur = cur.next
        m, n = m - 1, n - 1

    # The two pointers that will fix the final connections.
    tail, con = cur, prev

    # Iteratively reverse the nodes until n becomes 0.
    while n:
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        n -= 1

    # Adjust the final connections as explained in the algorithm
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    return head