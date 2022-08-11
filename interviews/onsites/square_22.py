'''

TPS 1
# morse code #

part 1: parsing signal arr of 0 and 1s to morse code 
part 2: getting signal arr (6 or more 0s indicate space) and then parsing the word


1. what would have been best way to split 6 or more 0s 

[0, 1, 0x6+, ... ]

start, curr = 0, 0
counter = 0

while curr < len(signal): 
	c = signal[curr]

	if c[curr] == 0:
		counter += 1

	else:
		if counter >= 6:
			word_arr.append(signal[start:curr-counter+1])
			start = curr
			counter = 0
		else:
			continue 

	curr += 1
	

TPS 2
# currency exchange # 

Implement methods: store, exchange 

-> storing all of them (nested dictionaries)
	-> key: currency code (from currency)
	-> values: nested dictionary with key: currency code (to currency) and value: exchange rate
-> finding if conversion (sometimes multiple) is possible 
	-> use BFS store tuples (curr_key, curr_amount) 
	-> visited_currencies (set) 








SYSTEMS DESIGN ROUND 
- design a hotel booking system 

- questions on features: 
	single hotel/airbnb/third-party booking? 
	trying to scale this globally? 
	do we retrieve the room availability ourselves or should the hotel/airbnb update themselves? 
	how many rooms total/what kind of rooms (single,double,triple)? 
	whats the expected traffic?
	expected mode of payments? or do we just book and hotel handles payments at arrival? 
	do we have a search/filter criteria? 

	** decorator pattern ** for services 
- let’s say you have this application, where would you put it, how would you set it up, which database you’d use, 
how would you set up database tables, how would you use load balancer for app servers
- I wrote a bit of pseudo code to explain how I'd handle reserving a room, though. Mostly around the transaction.
- extra ameneities? points member 


###############
### SCHEMAS ###
###############
 - booking (include bookingStatus in case cancelled)
 - room (room_id, user id, current price, original price, booking status, payment status, date from, date to)
 - user (user_id, name, email, phone, location)
 - hotel (hotel id, location, rating, amenities, ) 
 - transaction (transaction_id, booking_id, amount)
 
 - room type, room status, booking status, dates? 

 - extra: photos -> cache, load balancer 

### IMPORTANT ### 
low latencies and fast response times
high availability 
payments and booking will have to be ACID (consistent) 
scalable to x amount users and y amount hotels

### LOADBALANCING ###
- two tier round robin - first geographically, then divide up servers within regions
If the user can connect to the geographically nearest available application server, 
the latencies will consequently be much lower.


#####################
### MICROSERVICES ###
#####################
- hotel booking service <-> transaction service -> kafka consumer (notification service) 
- hotel management service 
- transaction service 
	kafka consumer (notifications) 
- user service 

- search service
	read heavy (not necessarily everyone books), complex if alot of filter criteria
	solution -> denormalization
	redundant copies of data written in multiple tables to avoid expensive joins 
	- or elasticsearch (nosql db)

- notification service 
	The notification service is fed by the Kafka queue. Whenever a booking is made, 
	the host will have to be notified. The guest will also need to be notified with an invoice, 
	so that the payment can be made. In case of cancellation of the booking from the host, 
	the guest will need to be notified. If the guest cancels a booking, the host will be informed. 
	These notifications are handled by the notification service.

################
### DATABASE ###
################
- cache photos video for rooms via CDN (any updates to DB) 
- sharding (Faster queries since index size reduced - perhaps based on geographical location) 
- store hotel id in relational db, but could leverage nosql such as cassandra 
  for hotel info such as name, location, etc... (not as crucial we maintain ACID)

### STREAMING ###
- kafka -> spark streaming service -> hadoop/hdfs


#################
### NEW HOSTS ###
################# 
- search microservice so that it’s visible to the users who search for lodging options in their vicinity. 
- We can use Kafka for this purpose. Each addition or modification occurring at the host microservice 
  can be pushed to the Kafka cluster. 
- From the Kafka cluster, these changes are pushed to all the search consumers 
  to become a part of the search traffic.



List<HotelDetails> search(String city, amenities, rating);




tps questions: 
- build a LRU-like system from scratch. 
- 2d grid traversal, trees, bit arithmetic, caching 
- select k random item from an arary of size n
- some gaming question 
- implement url shortening methods: shorten expand




https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/
https://dev.to/shivams136/leetcode-535-encode-and-decode-tinyurl-solution-and-discussion-22i0

'''


# min path sum
# have a sep 2d array keep track of min value it took to arrive there
def minPathSum(self, grid):

        rows, cols = len(grid), len(grid[0])
        
        dp = [[float("inf") for x in range(cols)] for y in range(rows)] 
        dp[0][0] = grid[0][0]
  
        for r in range(rows):
            for c in range(cols): 
                g_val = grid[r][c]
                dp[r][c] = min(dp[r][c], dp[r-1][c] + g_val, dp[r][c-1] + g_val)
        
        return dp[rows-1][cols-1]




# Instead of playing the game of tennis, Steve and Judy would rather simulate who wins when they play a match of tennis.  They have tired of the exercise but still have the competitive spirit pumping through their veins; the desperate desire to triumph.

# We will be creating a simulated version of tennis using the following rules:
# There are two players, player 1 and player 2
# The two players hit the ball back and forth (rally) until one of two things happen
#     One of the two players hits an unreturnable ball (a winner)
#     One of the two players hits a ball out of bounds (an error)
# When a player hits an error, the opposing player is awarded the point
# When a player hits a winner, that player is awarded the point
# Each rally always results in one of the two players winning the point
#####################################################################################################
############################################ Part 1 ################################################
#####################################################################################################
# Given the probability that each player hits an error 
# and the number of potential hits in a rally, determine which player wins! 
# Note that the given number of hits in a rally is a maximum possible number of hits in the rally.  
# If all the max number of hits is reached without either player making an error, 
# the player who hit last hit a winner!

# Example Input:
# probability that player1 misses a ball: 50%
# probability that player2 misses a ball: 80%
# potential hits in a series of rallies: 10

# Example Output:
# 'Player 1 Wins!'
#####################################################################################################
############################################# Part 2 ############################################
#####################################################################################################
# Now we want to determine which player has won after a series of rallies!

# Example Input:
# probability that player1 misses a ball: 5%
# probability that player2 misses a ball: 8%
# potential hits in a series of rallies: [5, 7, 1, 15, 20, 15]

# Example Output:
# 'Player 1 Wins!'


'''
player 1 would hit first 

player = 1|2
curr_turn = 0 

[50, 80] 


while curr_turn < max hits: 
    
    # if either player on any turn misses -> defeult win for other
    

'''
import random

def tennis_rallies(p1_miss, p2_miss, rally_series):
    p1_score, p2_score = 0, 0
    
    for rally in rally_series: 
        print("\n NEW GAME")
        w = parse_msg(tennis_simulation(p1_miss, p2_miss, rally))
        if w == '1':
            p1_score += 1 
        else:
            p2_score += 1
            
    if p1_score >= p2_score:
        return get_winner_string(0)
    
    return get_winner_string(1)



def tennis_simulation(p1_miss, p2_miss, rally_hits): 
    curr_turn = 0
    p_index = 0
    
    # int values of p1 and p2 for index 0 and 1 respectively 
    miss_probabilities = [p1_miss, p2_miss] 
    
    while curr_turn < rally_hits: 
        print("current turn: ", curr_turn)
        if is_miss(miss_probabilities[p_index]):
            print("miss ", p_index)
            return get_winner_string(switch_player(p_index))
        
        elif curr_turn == rally_hits-1:
            print ("winner ", p_index)
            return get_winner_string(p_index)
        
        curr_turn += 1
        p_index = switch_player(p_index) 
           
    return 
    
    
# anything less than rand_int -> miss  
def is_miss(p_miss):
    rand_int = random.randint(1, 100)
    print(rand_int)
    return p_miss >= rand_int
    
    
def get_winner_string(p_index): 
    return 'Player ' + str(p_index+1) + ' Wins!'


def switch_player(p_index): 
    return (p_index+1) % 2


def parse_msg(s):
    parsed_string = s.split(' ')
    return parsed_string[1] 



# print(tennis_simulation(0, 0, 6)) 

print (tennis_rallies(100, 0, [5, 6, 1, 17, 20, 14]))






'''

We've been hired by a local hotel to build an online booking system. The system we are going to design has two main requirements:

As a customer, I can search for available rooms
As a customer, I can make a room reservation

Different types of rooms? 
- 1 room type to start off
Modes of payment? 
- online credit card flow 
How many users? (tackle later…) 

Microservices 
-
Booking Service 
User Service -> it can either be a visitor, hotel management 
Hotel Management Service 
Payment Service 
- 
Search Service 


Database  
Booking Model
booking id -> primary key associated with the booking a user makes (long) 
user id -> long (user that made booking)
Transaction id -> long 
room id -> room that user booking
Date_from -> timestamp 
Date_to -> timestamp 
Booking status -> COMPLETED, CANCELED

User Model
User id (primary key - long) 
First name (string)
Last name (string) 
Email_address (string) 
Phone number (string) 
Modes of payment: optional empty array -> [ ] 

Room Model 
Room_id (primary id key long) 
Room_number (int) 

Transaction Model 
Transaction id (primary key - long)
user_id (long)
Booking_id (long) 
Payment_status: enum -> ACCEPTED, DECLINED, PENDING… 
Transaction token: (string) 

API
Booking Service 
- getBooking(booking_id) -> this will get the particular booking from booking id
- find(....) -> so kind of finder to get a collection of bookings
- createBooking(user id, room id, from, to, transaction id) 	
	-> construct the booking model and attempt to store it into MySQL 

User Service -> it can either be a visitor, hotel management 
Hotel Management Service 
Payment Service 

Search Service 
- find_rooms(date_from, date_to) - FINDER 
	-> filter out currently held rooms -> holding service 
	-> return all available room_ids in a collection 
- create_holding (roomid) 
	-> on failure -> find rooms (collection of this) 
- filter_for_holding_rooms() 



# what is we want to hold a booking for 10 minutes? 
# solution they wanted: add a PENDING booking status. all search/filter for rooms will withhold from returning PENDING rooms.... 
CLIENT 

SEARCH SERVICE <-> HOLDING SERVICE 

Holding Service 
- create_hold (user_id room_id, dates_from, dates_to) 
	-> from current timestamp until the next 10 mins
	-> create a producer event 
	-> kafka event stream -> check for current room ids 
- remove hold 

Apache Zookeeper 
Distributed synchronization, configurations 
Keep track of currently held room ids from the held events in the distributed cache



Note - notifications
'''





