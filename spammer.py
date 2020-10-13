import keyboard
import mouse
import time

def spam_keyboard(message, times):
    for i in range(times+1):
        keyboard.write(message)
        keyboard.send('Return')
        time.sleep(0.1)
    return

def spam_mouse(message, times, pos1x, pos1y, pos2x, pos2y):
    for i in range(times+1):
        mouse.move(pos1x, pos1y)
        mouse.click()
        keyboard.write(message)
        mouse.move(pos2x, pos2y)
        mouse.click()
        time.sleep(0.1)
    return

print('''
AutoSpammer - Alexandre Silva
---------------------------------------------------------------
The author is not responsible for any actions performed with
the use of this program. 
By using this program, you're taking full responsibility of any
actions you perform with it.
---------------------------------------------------------------''')

checked = False
confirm = None

while not checked:
    confirm = input('Proceed? (Y/N)\n>>> ').strip()
    authorized = ["y", "n"]
    if confirm.lower() not in authorized:
        continue
    else:
        break

if confirm.lower() == 'n':
    print('\nUser disagreed to the terms. Closing program.')
    time.sleep(0.7)


elif confirm.lower() == 'y':
    print('''---------------------------------------------------------------
HOW TO USE:
Input the spam arguments. You will then be given 10 seconds to focus on whatever text box you need to want on.
(To focus on the spam box, for instance, go to WhatsApp Web, and click on the message box.)
After the 10s cooldown is over, the program will begin.

KEYBOARD MODE:
This will press the ENTER key to send a message.

MOUSE MODE:
This will press the LEFT-MOUSE key to send a message.
Follow the steps that will be given to use Mouse Mode, if you so desire.
---------------------------------------------------------------''')
    time.sleep(1)
    done = False
    mode = None
    while not done:
        mode = input('Select a mode (M/K):\n>>> ')
        authorized = ["m", "k"]
        if mode.lower() in authorized:
            done = True
    message = input('Type in the message to spam with:\n>>> ')
    done = None
    times = 20
    while not done:
        times = input('Type in the amount of times (M/K):\n>>> ')
        try:
            times = int(times)
        except:
            print('Invalid amount of times. Try again')
        if times > 0:
            done = True
        else:
            print('Invalid amount of times. Try again')
    if mode == 'm':
        print('---------------------------------------------------------------')
        print('MOUSE MODE\nSelect Pos1 (Position of the box.) To select, navigate to the text box, hover over it, and press ALT+S.\n')
        keyboard.wait('ALT+S')
        pos1 = mouse.get_position()
        pos1x = pos1[0]
        pos1y = pos1[1]
        print('---------------------------------------------------------------')
        print('Select Pos2 (Position of the send button.) To select, navigate to the send button, hover over it, and press ALT+S.\n')
        keyboard.wait('ALT+S')
        pos2 = mouse.get_position()
        pos2x = pos2[0]
        pos2y = pos2[1]
        print('---------------------------------------------------------------')
        print('Program in stand-by. Press SPACE to resume.')
        keyboard.wait('space')
        print('Spamming in 10 seconds. Close this tab to end the program.')
        time.sleep(10)
        spam_mouse(message, times, pos1x, pos1y, pos2x, pos2y)
        print('Spam successfull! (Restart the program to use it again.)')
        with True:
            pass
    elif mode == 'k':
        print('---------------------------------------------------------------')
        print('Spamming in 10 seconds. Close this tab to end the program.')
        time.sleep(10)
        spam_keyboard(message, times)
        print('Spam successfull! (Restart the program to use it again.)')
        with True:
            pass
    else:
        print('An unexpected error occured. Please restart the program.')
        while True:
            pass
elif confirm.lower() is None:
    print('An unexpected error occured. Please restart the program.')
    while True:
        pass
        
