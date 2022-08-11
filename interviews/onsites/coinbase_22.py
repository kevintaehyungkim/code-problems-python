'''

https://leetcode.com/discuss/interview-question/1198505/coinbase-onsite-swe-reject

Round 1 : System Design. (1 hr)
I was asked to design a trading website. we delved into the depth of database schemas, inconsitencies etc.




QUESTION BASE
'''
"""
Moving Average, Median from a data stream. 
Bonus questions - find n percentile value from the stream

If the following conditions are met:

Both the heaps are balanced (or nearly balanced)
The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers
then we can say that:

All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it xx)
All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it yy)
Then xx and/or yy are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is the definition of median elements.

This leads us to a huge point of pain in this approach: balancing the two heaps!

Algorithm

Two priority queues:

A max-heap lo to store the smaller half of the numbers
A min-heap hi to store the larger half of the numbers
The max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed kk elements:

If k = 2*n + 1 \quad (\forall \, n \in \mathbb{Z})k=2∗n+1(∀n∈Z), then lo is allowed to hold n+1n+1 elements, while hi can hold nn elements.
If k = 2*n \quad (\forall \, n \in \mathbb{Z})k=2∗n(∀n∈Z), then both heaps are balanced and hold nn elements each.
This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap lo holds the legitimate median.

Adding a number num:

Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi. So remove the largest element from lo and offer it to hi.
The min-heap hi might end holding more elements than the max-heap lo, after the previous operation. We fix that by removing the smallest element from hi and offering it to lo.
The above step ensures that we do not disturb the nice little size property we just mentioned.

A little example will clear this up! Say we take input from the stream [41, 35, 62, 5, 97, 108]. The run-though of the algorithm looks like this:

Adding number 41
MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
Median is 41
=======================
Adding number 35
MaxHeap lo: [35]
MinHeap hi: [41]
Median is 38
=======================
Adding number 62
MaxHeap lo: [41, 35]
MinHeap hi: [62]
Median is 41
=======================
Adding number 4
MaxHeap lo: [35, 4]
MinHeap hi: [41, 62]
Median is 38
=======================
Adding number 97
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97]
Median is 41
=======================
Adding number 108
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97, 108]
Median is 51.5
"""

import heapq
class MedianFinder(object):

    def __init__(self):
        self.low_nums = [] # Max Heap
        self.high_nums = [] # Min Heap
        

    def addNum(self, num):
        heapq.heappush(self.low_nums, -1*num)
        highest_low = heapq.heappop(self.low_nums) * -1
        heapq.heappush(self.high_nums, highest_low)
        
        # Maintain size step?
        if len(self.low_nums) < len(self.high_nums):
            lowest_high = heapq.heappop(self.high_nums)
            heapq.heappush(self.low_nums, lowest_high*-1)
            
        

    def findMedian(self):
        if len(self.low_nums) > len(self.high_nums):
            return self.low_nums[0]*-1
        else:
            return (self.low_nums[0]*-1 + self.high_nums[0]) / 2

from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)

"""
Technical interview: design an iterator which can output infinity even number
two api: next/hasNext
1,3,5,7,...,inf


"""

"""
Simulate a File system. Basically a trie question. You can add a file or directory. 
But you can't add an invalid path for /a/b/c/d.txt can not be added unless you have a, b, c as directories.

https://leetcode.com/problems/design-in-memory-file-system/
Design this in an Object Oriented manner.
Include error checking for when creating a file in a non existent directory.

add('/a/b/c')
add('/a/b/c/d.txt')
"""

class File(): # OPTIONAL?
    def __init__(self, name, content = None):
        self.content = content

class Directory():
    def __init__(self, name):
        self.name = name
        self.dirs = {}
        self.files = {}

class FileSystem():
    def __init__(self):
        self.root = Directory('/')

    def add_directory(self, file_path):
        dirs = file_path.split('/')[1::]

        curr = self.root
        for dir_path in dirs:

            if dir_path not in curr.dirs:
                curr.dirs[dir_path] = Directory(dir_path)
            
            curr = curr.dirs.get(dir_path)
            
    def add_file(self, file_path):
        dirs = file_path.split('/')[1::]

        curr = self.root    
        for i in range(len(dirs)):
            path = dirs[i]
            file_found = False
            if '.' in path:
                file_found = True

            if file_found:
                # Handle File
                curr.files[path] = File(path)
            else:
                # Handle Directory
                if path not in curr.dirs:
                    print('cannot add file. Directory does not exist for', path)
                    return
                curr = curr.dirs.get(path)



test = FileSystem()
test.add_directory('/a/b/c')
test.add_file('/a/b/c/d.txt')

"""
########################################################
#################### ONSITE CONNECT 4  #################
########################################################

Implement for winning the game in horizontal and vertical manner.
Follow up: implement to winning diagonals
Follow up: implement a rudimentary AI to play with (select random spot to place move)
How will you make the game generic so that it can check for 16 points in a row/column/diagonal
How will you handle a huge grid
Optimize to find best column?
"""
from enum import Enum

class GameStatus(Enum):
    NOT_STARTED = 'not_started'
    ENDED = 'ended'

class PlayerPieceColor(Enum):
    RED = 'R'
    BLUE = 'B'

class ConnectFour():
    def __init__(self):
        self.board = [['_' for _ in range(7)] for _ in range(6)]
        self.status = GameStatus.NOT_STARTED 
        self.player_turn = PlayerPieceColor.RED

    def print_board(self):
        print('---------------------')
        for row in self.board:
            print(row)

    def add_piece(self, col):
        new_piece = self.player_turn.value
        row_added = -1
        for r in reversed(range(len(self.board))):
            if self.board[r][col] == '_':
                self.board[r][col] = new_piece
                row_added = r
                break

        if row_added >= 0:
            game_won = self.check_for_win(row_added, col)
            if game_won:
                self.status = GameStatus.ENDED
                print('GAME OVER. Winner:', self.player_turn.name)
            self.change_player_turn()
        else:
            print('Cannot add for column', col, 'for player', new_piece)


    def check_for_win(self, row, col):
        # Iterative check vertical, horizontal, diagonal
        len_rows = len(self.board)
        len_cols = len(self.board[0])

        color = self.player_turn.value

        # Scan Horizontal
        for c in range(len_cols-3):
            if self.board[row][c] == color and self.board[row][c+1] == color and self.board[row][c+2] == color and self.board[row][c+3] == color: 
                return True
        
        # Scan Vertical
        for r in range(len_cols-3):
            if self.board[r][col] == color and self.board[r+1][col] == color and self.board[r+2][col] == color and self.board[r+3][col] == color: 
                return True

        # Scan Descending Diagonal (bottom half)
        for r_start in range(len_rows):
            count = 0
            c = 0
            for r in range(r_start,len_rows):
                if self.board[r][c] == color:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0
                c += 1

        # Scan Descending Diagonal (top half)
        for c_start in range(1, len_cols):
            count = 0
            r = 0
            for c in range(c_start,len_cols):
                if self.board[r][c] == color:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0
                c += 1


        # Scan Ascending Diagonal
        

        return False

    def change_player_turn(self):
        if self.player_turn == PlayerPieceColor.BLUE:
            self.player_turn = PlayerPieceColor.RED
        else:
            self.player_turn = PlayerPieceColor.BLUE

    def reset_game(self):
        self.board = [['_' for _ in range(7)] for _ in range(6)]
        self.status = GameStatus.NOT_STARTED 
        self.player_turn = PlayerPieceColor.RED

test = ConnectFour()
test.print_board()
test.add_piece(0)
test.add_piece(0)
test.add_piece(0)
test.add_piece(0)
test.add_piece(0)
test.add_piece(1)
test.add_piece(1)
test.add_piece(1)
test.add_piece(1)
test.add_piece(1)
test.add_piece(2)
test.add_piece(2)
test.add_piece(2)
test.add_piece(3)
test.add_piece(3)
test.add_piece(4)
test.add_piece(4)
test.print_board()

# https://stackoverflow.com/questions/32770321/connect-4-check-for-a-win-algorithm

"""

Currency Exchange

a list of currency relationships with exchange values. (BTC - USD)
find the best exchange rate from currency1 to currency2

they expect it to be done OOP style. It's not difficult, just make a class with some methods to
1. add new currency pairs and 
2. a method to compute path given two currencies. 

It eventually does involve making some API calls. 
I recommend knowing how to make a GET request and parsing the returned data (json). I recommend Python


BID: highest a buyer is willing to buy
ASK: lowest a seller is willing to sell

{'USD', {'EUR', 0.8, 'CAD', 1.3}}

Notes:
- best exchange rate = highest exhange rate 

follow up - Rather than hardcoding the data use two apis - 
1.) https://api.pro.coinbase.com/products to get the id like USD-EUR aka currency pair 
2.) https://api.pro.coinbase.com/products/" + id + "/book to fetch the ask and bid price for each one of them. 

response = request.get(url) is enough to handle the GET calls + response.json() is enough to parse the response.

rolling basis:
- 
March 21
- 

Formal letter
"""
data = [
    {"source": "USD", "target": "BTC", "bid": 99, "ask": 100}, # Costs 100 USD to buy 99 BTC?? -> 99/100 = 0.99
    {"source": "EUR", "target": "BTC", "bid": 115, "ask": 120},
    {"source": "USD", "target": "ETH", "bid": 98, "ask": 100},
    {"source": "EUR", "target": "ETH", "bid": 400, "ask": 420}
]

import requests
from collections import defaultdict

class CurrencyExchange():
    def __init__(self):
        self.graph = {
            "A": {"B": 6, "D": 1},
            "B": {"A": 6, "D": 2, "E": 2, "C": 5},
            "D": {"A": 1, "B": 2, "E": 1},
            "E": {"B": 2, "D": 1, "C": 5},
            "C": {"B": 5, "E": 5}
        }
        self.temp_graph = {}

    def add_new_currency_pair(self, source, target, bid, ask):
        # Calculate exchange rate
        exchange_rate = ask / bid

        if source in self.temp_graph:
            self.temp_graph[source][target] = exchange_rate
        else:
            self.temp_graph[source] = {}
            self.temp_graph[source][target] = exchange_rate
        print(self.temp_graph)


    def get_currency_exchange_path_bfs(self, source, target):
        
        max_rate = 0
        queue = [(source, 1, set())]
        while queue:
            curr_node, accum_rate, visited = queue.pop(0)

            if curr_node == target:
                max_rate = max(max_rate, accum_rate)

            for next_node, next_rate in self.graph[curr_node].items():
                if next_node not in visited:
                    visited.add(next_node)
                    new_rate = accum_rate * next_rate
                    new_state = (next_node, new_rate, visited)
                    queue.append(new_state)

        return max_rate

    def get_currency_exchange_path_dfs(self, source, target):
        visited = set()

        def get_exchange_rate_helper(curr):
            # Base case: target found
            if curr == target:
                return 1
            if curr not in self.graph:
                return 0

            # Compare and get highest exchange rate from all children nodes
            max_prod = 0
            for next_node, next_rate in self.graph[curr].items():
                if next_node not in visited:
                    visited.add(next_node)
                    new_rate = next_rate * get_exchange_rate_helper(next_node)
                    max_prod = max(max_prod, new_rate)
                    visited.remove(next_node)
            return max_prod

        return get_exchange_rate_helper(source)

    def get_currency_exchange_rate_w_API(self, source, target):
        url = 'https://api.pro.coinbase.com/products'

        res = requests.get(url)
        # print(res.json())

test = CurrencyExchange()
print(test.get_currency_exchange_path_dfs('A', 'C'))
print(test.get_currency_exchange_path_bfs('A', 'C'))
test.add_new_currency_pair('A', 'B', 6, 1)
test.add_new_currency_pair('A', 'D', 1, 1)
test.add_new_currency_pair('B', 'A', 6, 1)
test.get_currency_exchange_rate_w_API('USD', 'EUR')


"""
System Design

design slack and slack related features (show "some one is typing" etc)

Core features:
- Group messaging
- sent + delivered + read receipts
- Image sharing
- Online last seen
- Someone is typing
- Chats are temporary / permanent

Characteristics:

#########################################################
One-to-one messaging & sent + delivered + read:
- Gateway 
- some Database to store User to gateway mapping. can be duplicated or central
    key - user
    value - box
- We can set up Microservice to handle sessions (indireclty a router, user A send message to B, service will route to correct gateway)
- two ways for user b to get message: 
    - long polling from via HTTP (client to server only)
    - websockets TCP. allows server to send message to client. need to reduce memory footprint
- session can send parallel message to user A that message was sent
- once b received message, we can send to session service and notifies A
- A gets delivery receipt
- Read receipts work the same way

Session service:
"to": B
"from": A


#################
Someone type:
"Someone is typing" becomes just one new type of event, it has a SRC and a DST and the Backend infrastructure takes care of routing the event to the correct websocket for the DST client.

I imagine as others mentioned that the clients will throttle the events as to avoid network traffic on every key press.

###################
Online last seen microservice:
either "online" or "last seen at <timestamp>"
- microservice should do activity tracking. should be able to distinguish when client messages are user based. 
- send it to last seen service if it's from user (deliveverd receipts should not count)

DB
- user
- last online

###################
GROUP SERVICE:
- since sessions store information all the user
- we can decouple that information with a group service, 
- client might check in with group message which can respond by saying which users are in the same group chat
- a lot of hcat applications limit number of people in group (i.e. 200)
"""







# TPS 
# Offers to BUY: 100, 100, 99, 99, 97, 90
# Offers to SELL: 109, 110, 110, 114, 115, 119
# Enter your code here. Read input from STDIN. Print output to STDOUT
"""

Notes:
- Interface
- Core functionalities:
    - store of current offers to buy and sell
        - buy offers (sorted) <- maxHeap
        - sell offers (sorted) <- minHeap
    - buy offer (offer price)
        - Check if offer price is num and above 0
        - if there are no current sell ofers
            - append it to buy_offers
            - return -1
        - take the first of the sell offers and check if lesser or equal than buy offer
            - return price if there is match
        - else 
            - update the buy_offers
            - return -1
    - sell offer (offer price)
        - Check if offer price is num and above 0
        - if there are no current buy ofers
            - append it to sell_offers
            - return -1
        - take the last of the buy offers and check if greater or equal to than sell offer
            - return price if there is match
        - else 
            - update the sell_offers
            - return -1
        
# Offers to BUY: 100, 100, 99, 99, 97, 90
# Offers to SELL: 109, 110, 110, 114, 115, 119

##########################
# Test Cases 1
#########################
sell(150) // no match
add_buy_offer(120) // match 109 
sell(99) // match 100
buy(114) // match 110
sell(99) // match 100

"""

import heapq
class MarketplaceInterface():
    def __init__(self):
        self.buy_offers = [-100, -100, -99, -99, -97, -90] # MaxHeap [ (price, BuyerOffer) ]
        self.sell_offers = [109, 110, 110, 114, 115, 119] # MinHeap
    
    class BuyOffer(self, price, timestamp, params=[]):
        self.buy_offer_id = 'offer_id' #hashing
        self.price = price
        self.timestamp = timestamp
        
    class SellOffer(self, price, timestamp, params=[]):
        self.sell_offer_id = 'offer_id' #hashing
        self.price = price
        self.timestamp = timestamp
        # assign self.field by iterating through params and add each
    
    def add_buy_offer(self, buy_offer, timestamp):
        if type(buy_offer) is not int or buy_offer < 0:
            return -1
        self.sell_offers and self.sell_offers[0] <= buy_offer
        
        if self.sell_offers and self.sell_offers[0] <= buy_offer:
            for i in range(len(self.sell_offers)):
                if self.sell_offers[i].timestamp >= Time.now:
                    sell_offer = heapq.heappop(self.sell_offers)
                    return sell_offer
                else:
                    # has expired so remove from heap
                    sell_offer = heapq.heappop(self.sell_offers)
        else:
            buy_offer_obj = BuyOffer(buy_offer, timestamp)
            heapq.heappush(self.buy_offers, (-1*buy_offer, buy_offer_obj))
            return -1
        
    def add_sell_offer(self, sell_offer, timestamp):
        if type(sell_offer) is not int or sell_offer < 0:
            return -1
        
        if self.buy_offers and -1*self.buy_offers[0] >= sell_offer:
            buy_offer = -1*heapq.heappop(self.buy_offers)
            return buy_offer
        else:
            sell_offer_obj = SellOffer(sell_offer, timestamp)
            heapq.heappush(self.sell_offers, (sell_offer, sell_offer_obj))
            return -1

marketplace = MarketplaceInterface()            
print(marketplace.add_sell_offer(150)) #// no match
print(marketplace.add_buy_offer(120)) #// match 109 
print(marketplace.add_sell_offer(99)) #// match 100
print(marketplace.add_buy_offer(114)) #// match 110
print(marketplace.add_sell_offer(99)) #// match 100







# ONSITE 1

"""
I: HashMap of tickers, String of Base curr, Int of amount
O: Int

BTC-USD bid: 990 ask: 1000 -> Exchange rate bid / ask

x BTC:USD -> bid / ask
x USD:BTC -> ask / bid

1 BTC = 990 USD BTC -> BID / 1
1 USD = 1/1000 BTC -> 1 / ASK

Step 1: Create graph of adj relationships
exchange_map = {
    USD: {
        BTC: 1/ASK,
        ETH: xxx
    }
    BTC: {
        USD: BID / 1
    }    
}

Step 2: Traverse to find maximum exchange rate

Step 3: Use exchange rate to compute the final amount

tickers = {
  'BTC-USD': { 'ask': 1000, 'bid': 990 },
  'BTC-EUR': { 'ask': 1200, 'bid': 1150 },
  'ETH-USD': { 'ask': 200, 'bid': 180 },
  'ETH-EUR': { 'ask': 220, 'bid': 210 }
}

https://api.pro.coinbase.com/products
https://api.pro.coinbase.com/products/BTC-USD/ticker
"""
import requests
class CurrencyExchange():
    def __init__(self):
        self.max_prod = 0
        
    def maximum_amount_exchange_w_api():
        url = 'https://api.pro.coinbase.com/products'
        res = requests.get(url)
        formatted = res.json()
        print('formatted', formatted)
        return formatted
        
    def maximum_amount_exchange(self, tickers, base_curr = None, quote_curr = None, amount = 0):
        # Step 1: build adj map
        exchange_map = {} 
        for ticker, value in tickers.items():
            ask = value.get('ask')
            bid = value.get('bid')
            base, quote = ticker.split('-')
            
            # Handle base
            if base in exchange_map:
                exchange_map[base][quote] = bid
            else:   
                exchange_map[base] = { quote: bid }
                
            # Handle quote
            if quote in exchange_map:
                exchange_map[quote][base] = 1 / ask
            else:
                exchange_map[quote] = { base: 1 / ask }
                
        # Step 2: Traverse map
        visited = set()
        
        print('exchange_map', exchange_map)

        def max_exchange_rate(curr):
            # Base Case
            if curr == quote_curr:
                return 1
            
            # Get max prod of all edges
            max_prod = 0
            if curr in exchange_map:
                for next_ticker, rate in exchange_map[curr].items():
                    # Plug second API to get that exchange rate
                    if next_ticker in visited:
                        continue
                        
                    visited.add(next_ticker)  
                    new_rate = rate * max_exchange_rate(next_ticker)
                    max_prod = max(max_prod, new_rate)
                    visited.remove(next_ticker)
                    
            return max_prod
                            
        temp_rate = max_exchange_rate(base_curr)
        print('rate', temp_rate)
        
        # Step 3: Compute amount
        return amount * temp_rate
            
tickers = {
  'BTC-USD': { 'ask': 1000, 'bid': 990 },
  'BTC-EUR': { 'ask': 1200, 'bid': 1150 },
  'ETH-USD': { 'ask': 200, 'bid': 180 },
  'ETH-EUR': { 'ask': 220, 'bid': 210 },
  'BTC-ETH': { 'ask': 5.6, 'bid': 5.5 }
}          
test = CurrencyExchange()
print(test.maximum_amount_exchange(tickers, 'USD', 'EUR', 1000))
print(test.maximum_amount_exchange_w_api)






# ONSITE 2

```python
"""

I: List of Lists with integers
O: List of integers <- values to be interleaved amongst the lists in input list

[1, 2, 3, 7, 8, 9]  [4, 5] [6] [] [7, 8, 9]
                  ^ 
[1, 4, 6, 7, 2, 5, 8, 3, 9]

Notes:
- size of list of lists can be dynamic
- Skip empty lists

Impl:
- listCounter = len(input list) ex) 5 -> 0 to 4

- initialize counter = 0 <- [1, 2, 3]
- idx = 0
- while there are nums in input list
    - check if list[idx] is within bounds of input_list[counter]
        - output.append(input_list[counter][idx])
    counter += 1
    - update idx when counter reches len of input list
"""

def interleave(input_list):
    output = []
    
    counter = 0
    idx = 0
    idx_in_bound = False
    while (True):
        inside_list = input_list[counter]
        if idx < len(inside_list):
            output.append(inside_list[idx])
            idx_in_bound = True
        
        # Handle incrementing idx and counter
        if counter < len(input_list)-1:
            counter += 1
        else:
            counter = 0
            
        if counter == 0: 
            # Check for flag since new round has begun
            if not idx_in_bound:
                return output
            # Round has finished so increment idx
            idx += 1
            idx_in_bound = False # Reset flag
            
    return output

print(interleave([[1, 2, 3], [4, 5], [6], [], [7, 8, 9]]))
# Expected: [1, 4, 6, 7, 2, 5, 8, 3, 9]

# Build an Iterator interface that supports the following functions:
# `int getNext()` returns the next value in the iterator and shifts it forward, and
# `bool hasNext()` that lets you know if there is a value left in the iterator.
# If hasNext() returns true, getNext() must return a value. Additionally, hasNext() must
# be idempotent and multiple calls returns the same result.
# [1,2,3] -> 1,2,3
# hasNext() -> True
# getNext() -> 1
# hasNext() -> True
# getNext() -> 2
# hasNext() -> True
# getNext() -> 3
# hasNext() -> False
"""

"""

class Iterator():
    def __init__(self, nums):
        self.store = nums # [1, 2, 3]
        self.idx = 0
        
    def has_next(self): # Returns boolean
        if self.idx < len(self.store):
            return True
        return False
    
    def get_next(self): # Returns value
        
        val = self.store[self.idx]
        self.idx += 1
        return val
    
def test(nums):
    iterator = Iterator(nums)
    while iterator.has_next():
        print('Next value: ', iterator.get_next())
    
test([1,2,3])

# start: 0, stop: 5, step: 1
# 0, 1, 2, 3, 4, 5

class IteratorRange():
    def __init__(self, start, stop, step):
        if (step < 0 and stop > start) or (step > 0 and start > stop): # negative
            # throw exception
            raise Exception('Range not applicable for step')
            
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
        
    def has_next(self): # Returns boolean
        if self.step > 0 and self.current <= self.stop:
            return True
        elif self.step < 0 and self.current >= self.stop:
            return True
        return False
    
    def get_next(self): # Returns value
        val = self.current
        self.current += self.step
        return val

test = IteratorRange(0, 5, 1)
while test.has_next():
    print('get next: ', test.get_next())

test = IteratorRange(0, -5, -2)
while test.has_next():
    print('get next: ', test.get_next())
    
# InterleavedIterator([Iterator([1,2,3]), Iterator([5])])
# has_next() - bool
# get_next() - int
# -> 1,5,2,3
# InterleavedIterator([Iterator([1,2,3]), Iterator([]), Iterator([5])])
# -> 1,5,2,3

class InterleaveIterator():
    def __init__(self, iterators):
        self.iterators = iterators
        self.num_iterators = len(iterators)
        self.iterator_idx = 0
    
    def has_next(self):
        for iterator in self.iterators:
            if iterator.has_next():
                return True
        return False
    
    def get_next(self): 
        iterator = self.iterators[self.iterator_idx]
        while self.has_next():
            if iterator.has_next():
                val = iterator.get_next()
                print('val', val)
                return val
            else:
                # If empty iterator
                # Check if iterator needs to be reset
                if self.iterator_idx < self.num_iterators:
                    self.iterator_idx += 1
                else:
                    self.iterator_idx = 0

iter1 = Iterator([1, 2, 3])
iter2 = Iterator([])
iter3 = Iterator([5, 6])

input_iters = [iter1, iter2, iter3]
test = InterleaveIterator(input_iters)
print('Interleave Iterator: ')
while test.has_next():
    print('get next: ', test.get_next())




################################
# CODE SIGNAL (TPS) MARCH 2022 #
################################

'''
Task 1 of 1

Scenario
Your task is to implement a simplified version of text editor.

All operations that should be supported are listed below. Partial credit will be given for each implemented operation. Please submit often to ensure partial credits are captured.

Implementation tips

Implement operations and provided steps one by one, and not all together, keeping in mind that you will need to make refactors to support each additional step. In the first three levels you can assume that only one text document is modified.

Note

After every operation, add the current state of the text to the resulting array. The returning array should consist of all the states after each operation is applied and have the same length as the # of input queries.


Level 1
The editor starts with a blank text document, with the cursor at initial position 0.

1. APPEND <text> should append the inputted string text to the document starting from the current position of the cursor. After the operation, the cursor should be at the end of the added string.

queries = [
    ["APPEND", "Hey"],                | "" -> "Hey"
    ["APPEND", " there"],             | "Hey" -> "Hey there"
    ["APPEND", "!"]                   | "Hey there" -> "Hey there!"
]

// returns: [ "Hey",
//            "Hey there",
//            "Hey there!" ]
2. MOVE <position> should move the cursor to the specified position. The cursor should be positioned between document characters, and are enumerated sequentially starting from 0. If the specified position is out of bounds, then move the cursor to the nearest available position.

queries = [
    ["APPEND", "Hey you"],            | "" -> "Hey you"
    ["MOVE", "3"],                    | moves the cursor after the first "y"
    ["APPEND", ","]                   | "Hey you" -> "Hey, you"
]

// returns: [ "Hey you",
//            "Hey you",
//            "Hey, you" ]
3. FORWARD_DELETE should remove the character right after the cursor, if any.

queries = [
    ["APPEND", "Hello! world!"],      | "" -> "Hello! world!"
    ["MOVE", "5"],                    | moves the cursor before the first "!"
    ["FORWARD_DELETE"],               | "Hello! world!" -> "Hello world!"
    ["APPEND", ","]                   | "Hello world!" -> "Hello, world!"
]

// returns: [ "Hello! world!",
//            "Hello! world!",
//            "Hello world!",
//            "Hello, world!" ]
and

queries = [
    ["APPEND", "!"],                  | "" -> "!"
    ["FORWARD_DELETE"],               | "!" -> "!"
    ["MOVE", "0"],                    | moves the cursor before the first symbol
    ["FORWARD_DELETE"],               | "!" -> ""
    ["FORWARD_DELETE"]                | "" -> ""
]

// returns: [ "!",
//            "",
//            "",
//            "",
//            "" ]


Level 2
Introduce methods to copy a part of the document text.

4. SELECT <left> <right> should select the text between the left and right cursor positions. Selection borders should be returned to the bounds of the document. If the selection is empty, it becomes a cursor position. Any modification operation replace the selected text and places the cursor at the end of the modified segment.

Additionally,

SELECT and APPEND should replace the selected characters with the appended characters
SELECT and FORWARD_DELETE should delete the selected characters
SELECT and MOVE deselects characters if there were any and moves the cursor
For example, the following operations

queries = [
    ["APPEND", "Hello cruel world!"], | "" -> "Hello cruel world!"
    ["SELECT", "5", "11"],            | selects " cruel"
    ["APPEND", ","],                  | "Hello cruel world!" -> "Hello, world!",
                                      | as " cruel" has been replaced with "," by APPEND
    ["SELECT", "5", "12"],            | selects ", world"
    ["FORWARD_DELETE"],               | "Hello, world!" -> "Hello!",
                                      | as ", world" has been deleted by FORWARD_DELETE
    ["SELECT", "4", "6"],             | selects "o!"
    ["MOVE", "1"]                     | moves cursor before "e", deselects "o!"
]

// returns: [ "Hello cruel world!",
//            "Hello cruel world!",
//            "Hello, world!",
//            "Hello, world!",
//            "Hello!",
//            "Hello!",
//            "Hello!" ]
produce "Hello!" with the cursor positioned after letter H.

5. CUT should remove the selected text and save it to the clipboard, if there is an active non-empty selection.
6. PASTE should append the text from the clipboard. If clipboard is empty, does nothing. The current selected text (if any) is overwriten with the clipboard value after the operation, and the cursor is placed at the end of the pasted text.

For example, the following operations

queries = [
    ["APPEND", "Hello, world!"],      | "" -> "Hello, world!"
    ["SELECT", "5", "12"],            | selects ", world"
    ["CUT"],                          | "Hello, world!" -> "Hello!",
                                      | as ", world" has been deleted by CUT and saved to clipboard
    ["MOVE", "4"],                    | moves the cursor between "l" and "o": "Hell|o!"
    ["PASTE"],                        | "Hello!" -> "Hell, worldo!",
                                      | as ", world" has been pasted from the clipboard
    ["PASTE"],                        | "Hell, worldo!" -> "Hell, world, worldo!"
                                      | as ", world" has been pasted from the clipboard
    ["SELECT", "4", "19"],            | selects ", world, worldo"
    ["PASTE"]                         | "Hell, world, worldo!" -> "Hell, world!",
                                      | as selected ", world, worldo" has been replaced
                                      | with ", world" from the clipboard
]

// returns: [ "Hello, world!",
//            "Hello, world!",
//            "Hello!",
//            "Hello!",
//            "Hell, worldo!",
//            "Hell, world, worldo!"
//            "Hell, world, worldo!" 
//            "Hell, world!" ]


Level 3
The text editor should allow document changes to be tracked and reverted. Consider only operations that actually modify the contents of the text document.

7. UNDO should restore the document to the state before the previous modification or REDO operation. The selection and cursor position should be also restored to the state they were before.

For example,

queries = [
    ["APPEND", "Hello, world!"],      | "" -> "Hello, world!"
    ["SELECT", "7", "12"],            | selects "world"
    ["FORWARD_DELETE"],               | "Hello, world!" -> "Hello, !",
                                      | as "world" has been deleted by FORWARD_DELETE
    ["UNDO"],                         | restores "Hello, world!" with "world" selected
    ["APPEND", "you"]                 | "Hello, world!" -> "Hello, you!",
                                      | as "world" has been replaced with "you"
]

// returns: [ "Hello, world!",
              "Hello, world!",
              "Hello, !",
              "Hello, world!",
              "Hello, you!" ]
8. REDO can only be performed if the document has not been modified since the last UNDO operation. REDO should restore the state before the previous UNDO operation, including the selection and cursor position. Multiple UNDO and REDO operations can be performed in a row.

For example,

queries = [
    ["APPEND", "Hello, world!"],      | "" -> "Hello, world!"
    ["SELECT", "7", "12"],            | selects "world"
    ["FORWARD_DELETE"],               | "Hello, world!" -> "Hello, !",
                                      | as "world" has been deleted by FORWARD_DELETE
    ["MOVE", "6"],                    | moves the cursor after the comma 
    ["UNDO"],                         | restores "Hello, world!" with "world" selected
    ["UNDO"],                         | restores initial ""
    ["REDO"],                         | restores "Hello, world!" with "world" selected
    ["REDO"]                          | restores "Hello, !" with the cursor after the comma
]

// returns: [ "Hello, world!",
              "Hello, world!",
              "Hello, !",
              "Hello, !",
              "Hello, world!",
              "",
              "Hello, world!",
              "Hello, !" ]
Level 4
The text editor should support multiple text documents with a common clipboard.

9. CREATE <name> should create a blank text document name. If such a file already exists, ignore the operation and return empty string. Modification history is stored individually for each document.
10. SWITCH <name> should switch the current document to name. If there is no such file, ignore the operation and return empty string. When switching to a file, the position of the cursor and selection should return to the state in which they were left.

Note: it is guaranteed that all operations from previous levels will be executed on the active document. For backward compatibility, assume for Levels 1-3 there is a single, initially active document.

For example,

queries = [
    ["CREATE", "document1"],          | creates document1
    ["CREATE", "document2"],          | creates document2
    ["CREATE", "document1"],          | raises a runtime exception
    ["SWITCH", "document1"],          | switches to document1
    ["APPEND", "Hello, world!"],      | document1: "" -> "Hello, world!"
    ["SELECT", "7", "12"],            | selects "world"
    ["CUT"],                          | cuts "world" to the clipboard
    ["SWITCH", "document2"],          | switches to document2
    ["PASTE"],                        | document2: "" -> "world"
    ["SWITCH", "document1"],          | switches to document1
    ["FORWARD_DELETE"]                | document1: "Hello, !" -> "Hello,!"
]

// returns: [ "",
              "",
              "",
              "",
              "Hello, world!",
              "Hello, world!",
              "Hello, !",
              "",
              "world",
              "Hello, !",
              "Hello,!" ]
Example

For

queries = [
    ["APPEND", "Hey"],
    ["APPEND", " you"],
    ["APPEND", ", don't"],
    ["APPEND", " "],
    ["APPEND", "let me down"]
]
the output should be

solution(queries) = [
    "Hey",
    "Hey you",
    "Hey you, don't",
    "Hey you, don't ",
    "Hey you, don't let me down"
]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string queries

An array of operations need to be applied to the text editor. It is guaranteed that each operation is one of the operations described in the description, all operation parameters are given in correct format, and the text editor will never be in an incorrect state that is not described in the description.

Guaranteed constraints:
1 ≤ queries.length ≤ 250.

[output] array.string

After every operation, add the current state of the text to the resulting array. The returning array should consist of all the states after each operation is applied and have the same length as the # of input queries.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

123
def solution(queries):


TESTS
CUSTOM TESTS
MORE
0/1000

'''


