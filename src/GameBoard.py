#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author George Dittmar copywrite 2013
"""
import numpy as np


# python class that holds the current state of the game board for minitchess

class Game_Board:
  """ PIECE REPRESENTATIONS
      1 = pawn
      2 = rook
      3 = bishop
      4 = knight
      5 = queen
      6 = king
  """
  
  #game_board =  None
  #game_over = False
  #on_move = 0
  # player piece counts dictionary
  #white = {}
  #black = {}
  
  """
  Initialize game board and class variables.
  """
  def __init__(self,width,height):
    self.game_board = np.zeros(shape=(height,width))
    self.game_over = False
    self.on_move = 0
    self.white = {1:5,2:2,3:2,4:2,5:1,6:1}
    self.black = {1:5,2:2,3:2,4:2,5:1,6:1}
    
    
    # generate default board state with pieces in place
  # move_to and move_from are tuples in the form of (y,x) due to how numpy creates multidimensional arrays  
  def move_piece(self,move_to,move_from):
     """
     Test if a move is valid. First grab the from and to positions on the board and make sure it is actually on the board and that there is a piece to move.
     """
     
     y = move_from[0]
     x = move_from[1]
     
     yd = move_to[0]
     xd = move_to[1]
     
     
     print self.game_board.shape
     # make sure move is within bounds  of the gameboard
     
       
       if( self.game_board[y][x] != 0 ):
        pass  
  
  #scan moves from start position to end. Check at each iteration if row,col are within bounds 
  # return a tuple of moves  
  def move_scan(self,piece,row,col,drow,dcol,isSingle):
    rowBack = row
    colBack = col
    
    while(in_bounds(row,col)):
      
      #move the piece at least 1 space.
        pass
      row = row+drow
      col = col+dcol
      
      if isSingle:
        break

  # check that pieces are still within the boundaries of the game board
  def in_bounds(self,row,col):
    
    if row < self.game_board.shape[0] or col < self.game_board.shape[1] or row >= 0 or col >= 0:
      return True
    return False
    
    
  #remove a piece,p1, from its location on the board and replace it with p1
  # location is a tuple in the form of (y,x)
  def remove_piece(self,p1,p2,location):
    self.game_board[location[0]][location[1]] = p1
    
  def get_board(self):
    return game_board
    
  def is_over(self):
    return game_board
  def start_game(self):
    pass
      
board = Game_Board(5,6)

board.move_piece((2,1),(1,2))

    
