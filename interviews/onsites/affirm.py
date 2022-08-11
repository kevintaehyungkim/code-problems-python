

# ONSITE TECHNICAL ROUND 2

'''
Given an input list of names, for each name, 
find the shortest substring that only appears in that name.

Example:

Input: ["cheapair", "cheapoair", "peloton", "pelican"]
Output:
"cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
"cheapoair": "po" // "oa" would also be acceptable
"pelican": "ca"   // "li", "ic", or "an" would also be acceptable
"peloton": "t"    // this single letter doesn't occur in any other string

- store all of names in dictionary (N), key: name, value: name 
'''

def find_shortest_substrings(names): 
	res = {}
	for s in names: 
		res[s] = s

		def check_shortest(substr):
			if not substr:
				return 

			isvalid = True

			for s2 in names: 
				if s2 == s:
					continue

				if substr in s2:
					isvalid = False 
					break

			if isvalid and len(substr) < len(res[s]):
				res[s] = substr

			check_shortest(substr[1:]) 
			check_shortest(substr[:-1])

		check_shortest(s)

	return res

print(find_shortest_substrings(["cheapair", "cheapoair", "peloton", "pelican"]))



'''
TECHNICAL PHONE SCREEN - JAN 2022

Given an input list of strings, for each letter appearing anywhere 
in the list, find the other letter(s) that appear in the most 
number of words with that letter.

Example: 
['abc', 'bcd', 'cde'] =>
  {
	a: [b, c],	# b appears in 1 word with a, c appears in 1 word with a
	b: [c], 	# c appears in 2 words with b, a and d each appear in only 1 word with b
	c: [b, d], 	# b appears in 2 words with c, d appears in 2 words with c. But a and e each 
					  appear in only 1 word with c.
	d: [c],		# c appears in 2 words with d. But b and e each appear in only 1 word with d
	e: [c, d], 	# c appears in 1 word with e, d appears in 1 word with e
		
  }
'''
# O(N (Length of Array) * S(Length of longest word) * S(Length of longest word))
def letters_most_words(words):
	letter_count = {}

	for w in words:
		pair_set = set() # track of letter pairs already processed

		for i in range(len(w)-1): 
			for j in range(i+1, len(w)):
				c1, c2 = w[i], w[j]
				if c1 not in pair_set and c1 != c2: 
					pair_set.add(min(c1,c2) + max(c1,c2))
					
					# add count for c1
					inner_dict = letter_count.get(c1, {})
					inner_dict[c2] = inner_dict.get(c2, 0) + 1
					letter_count[c1] = inner_dict

					# add count for c2
					inner_dict = letter_count.get(c2, {})
					inner_dict[c1] = inner_dict.get(c1, 0) + 1
					letter_count[c2] = inner_dict

	res = {}

	for entry in letter_count.items():
		sorted_counts = sorted(entry[1].items(), key = lambda x: x[1], reverse=True)
		max_count = sorted_counts[0][1]

		for count in sorted_counts: 
			if count[1] == max_count:
				if entry[0] in res.keys():
					res[entry[0]].append(count[0])
				else: 
					res[entry[0]] = [count[0]]
			else:
				break 

	return res

print(letters_most_words(['abc', 'bcd', 'cde']))



'''
// Initial State:

//              ROOT
//          /     |    \
//         /      |     \
//       B       C        D
//    /   |            /  | \  \
//   /    |           /   |  \  \
// F      G      (POPUP)  I  J  (K)
//              /   |   \   / \
//             /    |    \  Z  Y
//            N     O    (P)


// After openPopup called:

//              ROOT
//          /     |    \
//         /      |     \
//      (B)      (C)      D
//    /   |            /  | \   \
//   /    |           /   |  \   \
// F      G       POPUP  (I)  (J) (K)
//              /   |   \
//             /    |    \
//            N     O     (P)

Find POPUP, make all the sibling of POPUP to hidden
Find out POPUP's parent, make all the sibling of parent to hidden

private static class DomNode {
        String id;
        boolean hidden;
        List<DomNode> children;

        public DomNode(String id, boolean hidden, List<DomNode> children) {
            this.hidden = hidden;
            this.id = id;
            this.children = children;
        }
    }
'''
def makeHidden(root):
    popupNode = findPopup(root)
    
    a = popupNode.parent
    b = a.parent 
    
    for child in b.children:
        if child != a:
            child.hidden = True
            
    for child in a.children:
        if popupNode != child:
            child.hidden = True
    
    
    

def findPopup(node, parent=None):
    if node.id == 'POPUP':
        node.parent = parent
        return node
    
    node.parent = parent
    for child in node.children:
        result = findPopup(child, node)
        if result:
            return result
        
    return None



'''
myObject.putItem('a', 5);
myObject.putItem('b', 6);
myObject.putItem('c', 5);

'a' : 5
'b': 6
'c' : 5

putItem() function should be O(1) and take a char and a int as the input
Delete() could be O(n)
getRandom() should have 2/3 chance return 5 and 1/3 chance return 6
'''
class RandomizedCollection(object):

    def __init__(self):
        self.store = collections.defaultdict(int)
        self.lst = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        a = self.store[val] == 0
        self.store[val] += 1
        return a 
    

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.store[val] == 0:
            return False

        self.lst.remove(val)
        self.store[val] -= 1
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        n = len(self.lst)
        pos = random.randint(0, n - 1)
        return self.lst[pos]


'''
Hit Counter

games question, players given with random card and compete.

Without being too specific about the tech question, 
it was a graph problem involving creating a class where one of the 
methods was finding a path inside the graph.

max area island
number of islands 

2/3 sum

*** word ladder (hard) *** 

lru/lfu cache

parse lisp expression 

insert delete getrandom O(1) duplicates allowed

kth smallest element in BST 


'''



'''

Round 1: (1 hour)
System Design-1: Design Whatsapp. Standard Sys design questions.

Round 2: (1 hour)
Create a dictionary with the methods add(), get() and delete() and deleteRandom(). The delete method needs to remove a random value from the dictionary every time the method is invoked. The deleteRandom() method should also adhere to constant time as opposed to O(n). i.e. it should not iterate over the entire list to get values in order to remove the random value. Each element must have the same probability of being returned.

Follow up: Modify the map such that each unique element has equal probability of being returned.
Ex: If values in map are [5,5,6,5,5] both 5 and 6 have 50% probability of being returned.

Similar LC qn: https://leetcode.com/problems/insert-delete-getrandom-o1/

Round 3: (1 hour)
Evaluate a Decision Tree. It was a modified Binary Tree and had two dimensions called Signals & Constants. Leaf nodes had boolean values. Given an expression had to evaluate to a boolean value. Had to code 3 separate methods(buildTree, evalTree, modifyLeaf).
It took me 25 - 30 mins just to understand the questions. By the time I completed implementing the methods we had run out of time and as such couldnt run/test it. The interviewer seemed happy & said the imlpementation was correct & it shld have worked if we had extra time.

Round 4: (1 hour)
System Design-2: Design a RPC based system for Client-Server communication. We have already released thousands of clients to customers and they cannot be modified. There is a queue between Server & Client, but it works as radio broadcasts. Everybody gets every msg & there is no persistence or ack capabilites in the queue. I was asked to code/pseudo-code publish, consume and subscribe methods.
I bombed this round. I couldnt figure-out what the interviewer wanted. I asked him multiple questions but all his responses sounded very vague to me. I am really interested to see how to handle these kind of sys design questions.

Round 5: (1 hour)
Chat with Hiring Mgr. Was routine behavioral questions.

'''




# num island 
# lowest common ancestor 







# AFFIRM ONSITE 2/10/22 (THURSDAY) # 

'''


tl;dr - 1. Implement methods to grow a decision tree incrementally. 2. Use these methods to construct a given decision tree. 3. Evaluate this decision tree over multiple sets of signals.

A decision tree is a data structure that can be evaluated on a set of signals and return a decision (e.g. Yes or No ("Y" or "N")). Each interior node of the tree is associated with a particular signal and a constant value against which to compare that signal, and each leaf node has a value which will be returned by the tree. To evaluate the tree on a set of signals we traverse the tree, starting at the root and comparing the appropriate signal value to the constant associated with each interior node. If the signal value evaluates to false we proceed down the left subtree and if it evaluates to true we proceed down the right subtree. We continue until we reach a leaf at which point we return the value associated with the leaf.

For example, suppose that we have a set of integer-valued signals {X1, X2, X3}. Consider the following decision tree:

           X1 < 3
        ------------
       |            |
    X2 < 1       X1 < 6
 -----------    ---------
|           |  |         |
N           Y  N      X3 > 2
                    ----------
                   |          |
                   Y          N

Example input:
{x1: 2, x2: 4, x3: 10}


1. Implement methods to grow a decision tree incrementally. 
2. Use these methods to construct a given decision tree. 
3. Evaluate this decision tree over multiple sets of signals.


["X1 < 3"    "X2 < 1"   "N"  "Y"     "X1 < 6" .... ]


class node(signal, lessthan, val, left=None, right=None)
    str signal
    bool lessthan 
    int val
    node left
    node right 
    str decision - None
    
    
# tree
{
    "node": type node 
}



{
    "node": "X1 < 3": 
    "left": {
        node
        left: {
            
        }
        rgith
    }
    "right": 

}

evaluates to true -> right node
evaluates to left -> left node
    
'''

class Tree: 
    
    # class node: 
    def serialize(node):
        
        
        
    def deserialize: 
        
        




# {x1: 2, x2: 4, x3: 10}
def evaluate_signal(root, signals): 
    if decision:
        return decision 
    
    curr_key = root.signal 
    
    if less_than:
        if signals[curr_key] < value:
            return evaluate_signal(node.right, signals)
        else:
            return evaluate_signal(node.left, signals)
    else:
        if signals[curr_key] > value:
            return evaluate_signal(node.right, signals)
        else:
            return evaluate_signal(node.left, signals) 





# AFFIRM SYSTEMS DESIGN #

'''
Venmo
- peer to peer, money in venmo or bank (3-5 buss days)
- 


A "service (or Venmo) balance", maintained on behalf of each user. When another user pays you, it is transfered to your Venmo balance.
One or more connected bank accounts per user which can be used as a destination to which to withdraw money out of the service, or as a source for payments to other users.
The ability to make payments to other users, either from one's Venmo balance or from an attached bank account.
The ability to withdraw money from one's Venmo balance to an attached bank account.
Payments between users to appear instantaneous from the user's perspective


The service (Venmo) will have its own bank account where it holds funds on behalf of each user, and through which all user payments are "proxied". I.e. funds never move directly from one user's bank account to another, they always go through the service's account.
Money moves between bank accounts via ACH, meaning each transfer takes 3-5 business days to complete. We do not know until the transfer is complete whether it has succeeded or failed (due to lack of funds, for example).
As a service we never want to expose ourselves to the risk that a particular bank transfer will fail. I.e. we should not allow a user to withdraw funds received from another user until those funds have cleared into the service's bank account.


Class BankAccount: 
- user_id, bank_account id -> primary key
- bank_id (float) 
- bank_name (string) 
- routing_number (float)
- bank_account_number (float)

Class User:
- userid (primary key: long)
- first name (string)
- last name (string) 
- associated bank accounts (array of BankAccounts, instantiated None) 
- withdrawable balance (float) 
- pending balance (float) 
- total balance (float) 

Class Transaction:
- transaction_id (primary key, long) 
- sender_id (long)
- recipient_id (long) 
- total_amount (float) 
- created_at: timestamp value.. long? 
- is venmo balance (optional boolean) 
- is bank balance (optional boolean) 
- transfer_id (optional long) 

Class Transfer: 
- transfer_id (primary key, long)
- user_id (long)
- bank account (BankAccount) 
- transfer_type: enum (WITHDRAWAL, DEPOSIT) 
- amount (float) 
- created_at: timestamp value.. long? 
- completion_status: enum (PENDING, FAILED, COMPLETE)


db -> all pending transfers -> run every hour, checks status 
-> update api and corresponding transactions


Services:

Bank Service 
-> 

UserService 

- getUser (userid) 
- getUsers (arr of user ids)
- updateUser, updateUsers (userid or userids)


TransactionService 

method getTransactionsForUser (userid) :


method create_payment(sender, recipient, amount, type_payment(venmo, bank)) 
    -> retrieve user data for both sender and recipient via user service (getUserInfo)
    -> deduct from sender amount (total balance, withdrawable balance)
    -> created_at = library to get ... 
    -> create transcation = call builder for transaction model (pass in all the parameters above))
    
    -> return task.par 
    atomic transaction(make_transaction, update_balances(transaction)
    
    -> return transaction object 
    
method update_balances(transaction object):  

    if transfer: 
        -> create transfer 
        -> update the db of transfers 
        -> update recipient pending balance 

    -> add to recipient amount (add to total balance, withdrawable balance the amount value) 
    -> store back via UserService -> updated balances for both users
    -> return either success or updated user objects 
    
    -> if 


Service -> some kind of job that checks periodically for pending transfers

    -> whole bunch of transfer_ids -> 
    -> 




1. User A makes a payment to user B with funds from their Venmo balance
2. User A makes a payment to user B with funds from their bank account. The bank transfer from user A succeeds
3. User A makes a payment to user B with funds from their bank account. The bank transfer from user A fails
'''









    
    
    

