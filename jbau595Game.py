import random
random.seed(30)
from Stock import Stock
from Foundation import Foundation
"""
Compsci130 Assignment 
Student ID: 701679660
Name: Ju-an
Username: jbau595
Description: Implementation of the Klondike Solitaire game
"""

def main():
    print_banner()
    number_of_cards = 6
    pile1 = Foundation()
    pile2 = Foundation()
    stock = Stock(number_of_cards)
    stock.display()
    piles = [pile1, pile2]
    #complete this
    while game_over(stock, piles, number_of_cards) == False:
        state = False
        source = get_pile_number("source")
        destination = get_pile_number("destination")
        if source == 0:
            if destination == 0:
                state = stock.move()
            elif destination == 1:
                state = stock.move(piles[0])
            elif destination == 2: 
                state = stock.move(piles[1])
        elif source == 1:
            if destination == 0:
                print("ERROR: Invalid move!")
            elif destination == 1:
                state = piles[0].move(piles[0])
            elif destination == 2: 
                state = piles[0].move(piles[1])
        elif source == 2:
            if destination == 0:
                print("ERROR: Invalid move!")
            elif destination == 1:
                state = piles[1].move(piles[0])
            elif destination == 2: 
                state = piles[1].move(piles[1])
        if state == True:
            print_all_piles(stock, piles)
    print("Congratulations!")

def print_banner():
    #complete this
    string = "CS130 Assignment - Simplified Klondike Solitaire"
    print(string)
    print("=" * len(string))

def print_all_piles(stock, piles):
    #complete this
    stock.display()
    print("1:", piles[0])
    print("2:", piles[1])

def get_pile_number(prompt):
    #complete this
    string = "Enter a {} pile: ".format(prompt)
    user_input = input(string)
    while user_input.isnumeric() == False or int(user_input) > 2 or int(user_input) < 0:
        print("Invalid pile number!")
        user_input = input(string).strip("0")
    return int(user_input)
    
def game_over(stock, piles, number_of_cards):
    #complete this
    if stock.is_empty() and piles[0].size() == number_of_cards or piles[1].size() == number_of_cards:
        return True
    else:
        return False

main()
