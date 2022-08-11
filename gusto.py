# import requests
# import mysql.connector
# import pandas as pd

print 'Hello'

'''
we're only concerned about player and card 


class card 
- point_val
- price 
- card_color 

class game 
- array of players
-> {
    p1: 
    {
        'resources': {
        
        }, 
        'cards': set()
    },
    p2... 
}
'''



class Card: 
    
    def __init__(self, point_val, price, color): 
        self.point_val = point_val # int 
        self.price = price # key-> color, value -> amount for color 
        self.color = color #str 
        
        def to_string(self):
            return self.color + ' ' + str(self.point_val)



class Player: 
    def __init__(self, name):
        self.name = name # str
        self.resources = {}
        self.cards = [] 

    def to_string(self):
        return self.name + ' has resources: ' + str(self.resources) + ' and cards: ' + str(self.cards)

    def get_resources(self):
        return self.resources
        
    def set_resources(self, new_resources):
        self.resources = new_resources

    def add_card(self, card):
        self.cards.add(card)
        

class Game: 
    # p1 -> single player 
    # player_names - an arr of str player names 
    def __init__(self, player_names):
        self.players = {} #dict of player_name -> player objects 
        for p_name in player_names: 
            new_p = Player(p_name) 
            self.players[p_name] = new_p 
            print "new player: " + new_p.to_string()
        print "Game started with players: " + str(self.players)
        
        
    def purchase_card(self, p_name, card): 
        
        player = self.players.get(p_name)
        
        p_resources = player.get_resources()
        print p_resources
        can_purchase = True 
        
        for col in card.price: 
            col_val = card.price[col]
            if col not in p_resources or p_resources[col] < col_val:
                can_purchase = False 
                
        if can_purchase: 
            new_resources = self.make_transaction(p_resources, card.price)
            self.update_player_resources(p_name, new_resources) 
            self.add_purchased_card(p_name, new_resources)
            print (p_name + ' was able to purchase ') 

        else:
            print (p_name + ' was not able to purchase ') 
        
        return 
        
    # def update_player_resources(self, p_name, new_resource_count): 
        
    #     player = self.players[p_name]
    #     player.set_resources(new_resource_count)

    def update_player_resources(self, p_name, new_resource_count):
        p1 = self.players[p_name]
        p1.set_resources(new_resource_count)
        print p1.to_string() 
        self.players[p_name] = p1 

    def add_purchased_card(self, p_name, card):
        p1 = self.players[p_name]
        p1.add_card(card)
        self.players[p_name] = p1 
        
                
    # only call when we can make a card purchase 
    def make_transaction(self, p_resources, c_price):
        for c in c_price: 
            c_val = c_price[c] 
            p_resources[c] -= c_val 
            
        return p_resources 
        
        
        
        
        
       
new_game = Game(["p1"])  
p1 = new_game.update_player_resources("p1", {'Blue': 4, 'Red': 3})
# new_game.players["p1"] = {'Blue': 4, 'Red': 3}

c1 = Card(2, {'Blue': 2, 'Red': 2}, 'G')
 
new_game.purchase_card("p1", c1)

