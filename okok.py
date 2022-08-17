import win32api, win32con
import time
from keyboard import is_pressed

time.sleep(2)
def click(rx,ry):
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
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        if is_pressed('q'):
            break

