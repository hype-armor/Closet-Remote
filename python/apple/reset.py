#!/usr/bin/python3.4
# -*- coding: ascii -*-
#
# create a better keyboard for appletv
#
# input: string or char.
# output: ir instructions to navigate the appletv keyboard.
#

import sys
from subprocess import call

# read input
inputString = sys.argv[1]

# if input is empty; return
if len(inputString)==0:
    sys.exit()

# make tuple table for all chars and their position.
# e.g. list of tuples
# list_of_tuples = [(1,2),(3,4)]
# six collumns a-z and 1-0
# format: char, col, row
# ~ == clear key
# } == send home key
# { == a
keyboardMap = [
    ('a', 0, 0),('b', 1, 0),('c', 2, 0),('d', 3, 0),('e', 4, 0),('f', 5, 0),
    ('g', 0, 1),('h', 1, 1),('i', 2, 1),('j', 3, 1),('k', 4, 1),('l', 5, 1),
    ('m', 0, 2),('n', 1, 2),('o', 2, 2),('p', 3, 2),('q', 4, 2),('r', 5, 2),
    ('s', 0, 3),('t', 1, 3),('u', 2, 3),('v', 3, 3),('w', 4, 3),('x', 5, 3),
    ('y', 0, 4),('z', 1, 4),('1', 2, 4),('2', 3, 4),('3', 4, 4),('4', 5, 4),
    ('5', 0, 5),('6', 1, 5),('7', 2, 5),('8', 3, 5),('9', 4, 5),('0', 5, 5),
    (' ', 0, 6),('~', 2, 6),('{', 0, 0),('}', 6, 6),
]


lastpos = [0, 0]

def sendIR(key):
#    print (key)
    call(["irsend", "SEND_ONCE", "appletv", key])

# returns the relative position of the char
def findPOS(c):
    for (l,x,y) in keyboardMap:
            if l==c:
                global lastpos
                rightCount = x - lastpos[0]
                downCount = y - lastpos[1]
                lastpos = [x,y]         
                print (l + " x:" + str(x) + " y:" + str(y))
                return [rightCount, downCount]
    
def move(rightCount, downCount):
    for left in range(0, downCount):
#       print "move down 1"
        sendIR("KEY_DOWN")
    for left in range(downCount, 0):
#       print "move up 1"
        sendIR("KEY_UP")
    for right in range(0, rightCount):
#       print "move right 1"
        sendIR("KEY_RIGHT")
    for right in range(rightCount, 0):
#       print "move left 1"
        sendIR("KEY_LEFT")
        
def sendHome():
    global lastpos
    move(-10, -10)
    move(0,2)
    lastpos = [0,0]

# add '{' so the cursor returns to start pos
inputString += '{'
for (c) in inputString:
    # if HOME_KEY then nav to top left and then down one
    if c=='{':
        pos = findPOS(c)
        move(pos[0], pos[1])
    # if send home KEY then pretend we are at the bottom most right most then continue on
    elif c=='}':
        sendHome()
    # if clear key then nav to clear, press it and then return to home
    # since clear will run alone, home first
    elif c=='~':
        # move to clear
        pos = findPOS(c)
        move(pos[0], pos[1])
        sendIR("KEY_OK")
        # go up one to make knowing the location easy
        move(0, -1)
        lastpos = [5,5]
    else:
        pos = findPOS(c)
        move(pos[0], pos[1])
        sendIR("KEY_OK")
            
                

# page three
#('{', 0, 0),
#('~', 1, 0),
#('!', 2, 0),
#('@', 3, 0),
#('#', 4, 0),
#('$', 5, 0),
#('%', 0, 0),
#('^', 1, 0),
#('&', 2, 0),
#('*', 3, 0),
#('(', 4, 0),
#(')', 5, 0),
#('-', 0, 0),
#('_', 1, 0),
#('=', 2, 0),
#('+', 3, 0),
#('[', 4, 0),
#('{', 5, 0),
#(']', 0, 0),
#('}', 1, 0),
#('\\', 2, 0),
#('}', 3, 0),
#(';', 4, 0),
#(':', 5, 0),
#('\'', 0, 0),
#('"', 1, 0),
#(',', 2, 0),
#('<', 3, 0),
#('.', 4, 0),
#('>', 5, 0),
#('/', 0, 0),
#('?', 1, 0)
