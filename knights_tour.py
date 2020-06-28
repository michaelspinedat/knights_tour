#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:41:53 2020

@author: michael
"""

import numpy as np
rows = 8
cols = 8

board = np.zeros((rows, cols))


# solves the Knight Tour problem using Backtracking.         
def find_tour(board, r, c, count):    
    if r < 0 or r >= board.shape[0] or c < 0 or c >= board.shape[1]:
        return False
    
    if board[r][c] != 0:
        return False
    
    board[r][c] = count
    
    if count == (board.shape[0] * board.shape[1]):
        return True
    
    # define next move of Knight.  
    moveR = np.array((2, 1, -1, -2, -2, -1, 1, 2))
    moveC = np.array((1, 2, 2, 1, -1, -2, -2, -1))

    # try all next moves from the current coordinate r, c
    for i in range(0, moveR.shape[0]):
        newR = r + moveR[i]
        newC = c + moveC[i]
        control = find_tour(board, newR, newC, count + 1)
        
        if control:
            return True
    
    board[r][c] = 0
    return False

def print_board(board):
    for r in range(0, board.shape[0]):
        for c in range(0, board.shape[1]):
            if board[r][c] < 10:
                print("0", int(board[r][c]), " ", end="", sep="")
            else:
                print(int(board[r][c]), " ", end="", sep="")
        print()

posR = 0
posC = 0
tour_found = find_tour(board, posR, posC, 1)

if tour_found:
    print_board(board)
else:
    print("Solution not found")


        