from pyautogui import *
import time

PAUSE = 1
time.sleep(4)

click(x=365, y=27)
click(x=430, y=83)
write('hashtagtreinamentos.com')
press('enter')

time.sleep(3)

moveTo(x=480, y=169)
click(x=777, y=375, duration=0.5)

time.sleep(2)

click(x=380, y=752)
write('Jo~ao')

click(x=380, y=818)
write('Joao123@gmail.com')

click(x=380, y=882)
write('12345678901')

click(x=380, y=953)