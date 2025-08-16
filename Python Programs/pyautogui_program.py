
import pyautogui as p
import time
print("completed")
#os.system('cal')
time.sleep(10)
#print(p.position())
p.click(779,697)
p.typewrite("Mumbai")
#time.sleep(5)
#print(p.position())
p.click(1062,461)
p.hotkey('fn','F11')

buttonpos=p.locateOnScreen(r'/users/screenshot.png')
print(buttonpos)
bx,by=p.center(buttompos)
p.click(bx,by)
