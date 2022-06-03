class Foundation:
    def __init__(self):
        self.foundation_pile = []
    
    def push_list(self, values):
        for item in values:
            self.foundation_pile.append(item)
    
    def is_empty(self):
        if len(self.foundation_pile) == 0:
            return True
        else:
            return False
            
    def size(self):
        return len(self.foundation_pile)
    
    def __str__(self):
        string = "["
        if len(self.foundation_pile) == 0:
            return ""
        for item in self.foundation_pile[:-1]:
            string += str(item) + ", "
        string += str(self.foundation_pile[-1]) + "]"
        return string
            
    def add_front(self, item):
        self.foundation_pile.append(item)
    
    def add_rear(self, item):
        self.foundation_pile.insert(0, item)
    
    def remove_front(self):
        try:
            popped = self.foundation_pile.pop()
            return popped
        except:
            raise IndexError("ERROR: The foundation pile is empty!")
            
    def remove_rear(self):
        try:
            popped = self.foundation_pile.pop(0)
            return popped
        except:
            raise IndexError("ERROR: The foundation pile is empty!")
            
    def peek_front(self):
        try:
            return self.foundation_pile[-1]
        except:
            raise IndexError("ERROR: The foundation pile is empty!")
    
    def peek_rear(self):
        try:
            return self.foundation_pile[0]
        except:
            raise IndexError("ERROR: The foundation pile is empty!")
    
    def move(self, pile):
        if len(self.foundation_pile) == 0:
            print("ERROR: The foundation pile is empty!")
            return False
        elif pile.is_empty():
            pile.push_list(self.foundation_pile)
            self.foundation_pile = []
            return True
        elif int(self.peek_rear()) == (int(pile.peek_front())-1):
            pile.push_list(self.foundation_pile)
            self.foundation_pile = []
            return True
        else:
            print("ERROR: Invalid move!")
            return False

