from pyautogui import click
from keyboard import is_pressed
#1366x768 -> x=679 y=533

#Main click
def clicker():
    while True:
        click(x=679, y=533)
        if is_pressed('q'):
            break
