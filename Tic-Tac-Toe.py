"""
Created on Mon Jun  8 18:03:24 2020

@author: Arvind Singh
"""
def printboard(board: list):
    #Just to print out the board everytime the user gives their input
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
    print('---+---+---')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6])
    print('---+---+---')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3])
    print('---+---+---')
    
def take_input(filled: list, board: list, count: int, player: chr) -> int :
    #takes in input and returns the "count" which is how many moves are done
    Input = int(input(f'Enter number to insert {player} in: '))
    confirm = 0
    
    while Input > 9:
        Input = int(input('Number is out of range. Enter another number in the range 1-9: '))
        
    if Input in filled:
        confirm = 1
        
    while confirm == 1:
        Input = int(input('This position is already occupied, enter another position: '))
        if Input not in filled:
            confirm = 0
    
    filled.append(Input)
    board.pop(Input)
    board.insert(Input, player)
    printboard(board)
    return count + 1
    
def main():
    #so this is gonna be the main function which I'll call at the starting so I can 
    #feel familiar with python (cause I'm) used to having a main function because of C++.
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    print('Do you want to be X or O?')
    player1 = input()
    player2 = ' '
    if player1 == 'X':
        player2 = 'O'
    else : 
        player2 = 'X'
    
    count = 0; #to count how many moves are done
    filled = [] #to see what all numbers are already in so it won't be put in again
    
    #alright remember that pop(index_number) removes an element from that index number and
    #insert(index_number, element) adds an element to entered index_number
    
    while count < 9: #there can't be greater than 9 moves, sooo...
        #let's assume that X always starts
        count = take_input(filled, board, count, player1)
        
        if count == 9: #the board is full and maximum number of moves have been done.
            break
        
        #let's work on player 2s' input now
        count = take_input(filled, board, count, player2)
        
main()