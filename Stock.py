import random

class Stock:
    def __init__(self, number_of_cards = 0):
        self.number_of_cards = number_of_cards
        items = []
        if number_of_cards != 0:
            for value in range(self.number_of_cards):
                items.append(value)
        random.shuffle(items)
        self.stock_pile = items
    
    def push_list(self, values):
        for item in values:
            self.stock_pile.append(item)
    
    def is_empty(self):
        if len(self.stock_pile) == 0:
            return True
        else:
            return False
            
    def size(self):
        return len(self.stock_pile)
    
    def __str__(self):
        string = "["
        if len(self.stock_pile) <= 0:
            return ""
            
        else:
            for item in self.stock_pile[:-1]:
                string += str(item) + ", "
            string += str(self.stock_pile[-1]) + "]"
            return string
        
    def display(self):
        if len(self.stock_pile) != 0:
            print("S: {} ".format(self.stock_pile[0]) + "* " * (len(self.stock_pile) - 1))
        else:
            print("S:")
            
    def add_front(self, item):
        self.stock_pile.append(item)
     
    def add_rear(self, item):
        self.stock_pile.insert(0, item)
        
    def remove_front(self):
        try:
            popped = self.stock_pile.pop(-1)
            return popped
        except:
            raise IndexError("ERROR: The stock pile is empty!")
    
    def remove_rear(self):
        try:
            popped = self.stock_pile.pop(0)
            return popped
        except:
            raise IndexError("ERROR: The stock pile is empty!")
    
    def peek_front(self):
        try:
            return self.stock_pile[-1]
        except:
            raise IndexError("ERROR: The stock pile is empty!")
    
    def peek_rear(self):
        try:
            return self.stock_pile[0]
        except:
            raise IndexError("ERROR: The stock pile is empty!")
    
    def move(self, pile = None):
        if pile == None and self.is_empty() == False:
            popped = self.remove_rear()
            self.add_front(popped)
            return True
        elif pile != None and pile.is_empty():
            popped = self.remove_rear()
            pile.add_front(popped)
            return True
        elif self.is_empty():
            print("ERROR: The stock pile is empty!")
            return False
        elif int(self.peek_rear()) == (int(pile.peek_front()) -1):
            popped = self.remove_rear()
            pile.add_front(popped)
            return True
        else:
            print("ERROR: Invalid move!")
            return False

    

