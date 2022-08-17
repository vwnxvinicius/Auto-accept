'''

from pyautogui import click
from keyboard import is_pressed
import pyautogui
import os
import time
#1366x768 -> x=679 y=533


#Main click
def accept_match(rx, ry):
    x=679
    y=533

    # Verificando os valores da resolução X
    if rx > 1366:
        x += (rx - 1366)/2
    elif rx < 1366:
        x += (1366 - rx)/2

    #Verificando os valores da resolução Y
    if ry > 768:
        y += (ry - 768)/2
    elif ry < 768:
        y += (768 - ry)/2

    # Loop do clique
    while True:
        click(x,y)
        if is_pressed('q'):
            break



def string_separator(string, n):
    x = string.find(' ')
    str_1 = string[0:x]
    str_2 = string[-x:]
    if n == 1:
        return str_1
    else:
        return str_2

'''